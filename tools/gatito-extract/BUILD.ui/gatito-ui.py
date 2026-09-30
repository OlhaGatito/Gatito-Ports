#!/usr/bin/env python3
"""Controller-friendly UI for Gatito Extractor."""
import argparse,os,subprocess,sys
from pathlib import Path
BAR=36
def draw(pct,stage):
    sys.stdout.write("\033[2J\033[H")
    print("+"+"-"*60+"+")
    print("|"+"GATITO EXTRACTOR".center(60)+"|")
    print("|"+"".center(60)+"|")
    n=max(0,min(BAR,int(BAR*pct/100)))
    print("|"+("["+"█"*n+"░"*(BAR-n)+"] %3d%%"%pct).center(60)+"|")
    print("|"+stage[:60].center(60)+"|")
    print("+"+"-"*60+"+")
    sys.stdout.flush()
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("recipe")
    ap.add_argument("--game-dir",required=True)
    ap.add_argument("--abi")
    ns=ap.parse_args()
    root=Path(__file__).resolve().parents[1]
    engine=root/"gatito-extract-v2.py"
    cmd=[sys.executable,str(engine),ns.recipe,"--game-dir",ns.game_dir,"--validation-delay","0.35"]
    if ns.abi: cmd += ["--abi",ns.abi]
    draw(0,"Iniciando")
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
    last=0
    for line in p.stdout:
        line=line.rstrip()
        if line.startswith("GATITO_STAGE|"):
            _,pct,msg=line.split("|",2)
            last=int(pct); draw(last,msg)
        else:
            print(line)
    rc=p.wait()
    if rc:
        draw(100,"Falha — consulte o log")
    else:
        draw(100,"Extração concluída e validada")
    return rc
if __name__=="__main__":
    raise SystemExit(main())
