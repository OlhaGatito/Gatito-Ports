#!/usr/bin/env python3
"""Gatito Extractor: small, auditable BYO-data extraction core."""
import argparse, hashlib, json, os, shutil, tempfile, zipfile
from pathlib import Path, PurePosixPath

VERSION = "0.1.0"

class ExtractError(Exception): pass

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""): h.update(chunk)
    return h.hexdigest()

def safe_rel(value):
    p = PurePosixPath(value)
    if p.is_absolute() or ".." in p.parts: raise ExtractError("unsafe recipe path")
    return Path(*p.parts)

def recipe(path):
    try: data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e: raise ExtractError("invalid recipe: %s" % e)
    for key in ("id", "version", "extract", "commit"):
        if key not in data: raise ExtractError("recipe missing %s" % key)
    return data

def inputs(game_dir, explicit):
    if explicit: found = [Path(x).expanduser().resolve() for x in explicit]
    else:
        root = game_dir / "gamedata"
        found = [p for p in sorted(root.iterdir()) if p.is_file()] if root.is_dir() else []
        if not found: found = [p for p in sorted(game_dir.iterdir()) if p.is_file()]
    if not found: raise ExtractError("no user-provided data found")
    return found

def members(path):
    try:
        with zipfile.ZipFile(path) as z:
            return [x.filename for x in z.infolist() if not x.is_dir()]
    except zipfile.BadZipFile: return []

def find_source(paths, patterns, abi):
    patterns = [str(x).replace("{abi}", abi) for x in patterns]
    for src in paths:
        names = members(src)
        for pattern in patterns:
            for name in names:
                if PurePosixPath(name).match(pattern): return src, name
        if src.name in patterns: return src, ""
    raise ExtractError("required source not found")

def copy_entry(src, member, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if member:
        with zipfile.ZipFile(src) as z, z.open(member) as inp, dst.open("wb") as out:
            shutil.copyfileobj(inp, out)
    else: shutil.copy2(src, dst)

def validate(stage, rules):
    for rule in rules:
        path = stage / safe_rel(rule["path"])
        if not path.is_file(): raise ExtractError("missing output: %s" % rule["path"])
        if "size" in rule and path.stat().st_size != int(rule["size"]):
            raise ExtractError("size mismatch: %s" % rule["path"])
        if "min_size" in rule and path.stat().st_size < int(rule["min_size"]):
            raise ExtractError("minimum size failed: %s" % rule["path"])
        if "sha256" in rule:
            allowed = rule["sha256"] if isinstance(rule["sha256"], list) else [rule["sha256"]]
            if digest(path) not in allowed: raise ExtractError("sha256 mismatch: %s" % rule["path"])

def main():
    p = argparse.ArgumentParser(description="Gatito Extractor — BYO-data")
    p.add_argument("--version", action="version", version=VERSION)
    p.add_argument("recipe", type=Path); p.add_argument("--game-dir", type=Path, required=True)
    p.add_argument("--input", action="append", default=[]); p.add_argument("--abi")
    a = p.parse_args(); r = recipe(a.recipe)
    abi = a.abi or (r.get("abi_order") or [""])[0]
    if a.abi and a.abi not in r.get("abi_order", []): raise ExtractError("ABI not allowed")
    paths = inputs(a.game_dir, a.input)
    work = a.game_dir / ".gatito-extract"; work.mkdir(exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix="stage-", dir=work))
    try:
        for rule in r["extract"]:
            src, member = find_source(paths, rule["source"]["patterns"], abi)
            copy_entry(src, member, stage / safe_rel(rule["destination"].replace("{abi}", abi)))
        validate(stage, r.get("validate", []))
        target = a.game_dir / safe_rel(r["commit"].get("root", "game"))
        old = target.with_name(target.name + ".gatito-old")
        if old.exists(): shutil.rmtree(old)
        if target.exists(): target.rename(old)
        try: stage.rename(target)
        except Exception:
            if target.exists(): shutil.rmtree(target)
            if old.exists(): old.rename(target)
            raise
        if old.exists(): shutil.rmtree(old)
        (target / ".gatito-extract.json").write_text(
            json.dumps({"recipe": r["id"], "version": r["version"], "abi": abi}, indent=2) + "\n",
            encoding="utf-8")
        print("GATITO EXTRACT OK: %s %s" % (r["id"], r["version"]))
    except Exception as e:
        shutil.rmtree(stage, ignore_errors=True); print("GATITO EXTRACT ERROR: %s" % e, file=os.sys.stderr); return 1
    return 0

if __name__ == "__main__": raise SystemExit(main())
