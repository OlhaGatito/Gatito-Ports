#!/usr/bin/env python3
"""Standalone Gatito-Extrator visual test UI."""
import argparse, os, platform, shutil, subprocess, sys, time
from pathlib import Path

BAR=42
WIDTH=68

def clear():
    sys.stdout.write("\033[2J\033[H")

def bar(pct):
    pct=max(0,min(100,int(pct)))
    filled=int(BAR*pct/100)
    return "["+"#"*filled+"-"*(BAR-filled)+f"] {pct:3d}%"

def draw(pct,stage,details="",log_path=""):
    clear()
    print("+"+"-"*WIDTH+"+")
    print("|"+"GATITO-EXTRATOR".center(WIDTH)+"|")
    print("|"+"Standalone diagnostic / extraction test".center(WIDTH)+"|")
    print("|"+"".center(WIDTH)+"|")
    print("|"+bar(pct).center(WIDTH)+"|")
    print("|"+("ETAPA: "+stage)[:WIDTH].center(WIDTH)+"|")
    print("|"+"".center(WIDTH)+"|")
    recent=details.splitlines()[-4:]
    for line in recent:
        print("|"+line[:WIDTH].center(WIDTH)+"|")
    for _ in range(4-len(recent)):
        print("|"+"".center(WIDTH)+"|")
    print("|"+("LOG: "+log_path)[:WIDTH].center(WIDTH)+"|")
    print("+"+"-"*WIDTH+"+")
    sys.stdout.flush()

def command_output(cmd):
    try:
        p=subprocess.run(cmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=3)
        return p.stdout.strip()[:500]
    except Exception as exc:
        return f"<erro: {exc}>"

def collect_data(game_dir,recipe,engine,log):
    lines=[
        "Host: "+platform.platform(),
        "Kernel: "+command_output(["uname","-a"]),
        "Python: "+sys.version.split()[0],
        "GAMEDIR: "+str(game_dir),
        "Recipe: "+str(recipe),
        "Engine: "+str(engine),
        "CFW: "+os.environ.get("CFW_NAME","unknown"),
        "DEVICE: "+os.environ.get("DEVICE_NAME","unknown"),
        "ARCH: "+os.environ.get("DEVICE_ARCH",platform.machine()),
        "DISPLAY: "+os.environ.get("DISPLAY","<none>"),
        "WAYLAND_DISPLAY: "+os.environ.get("WAYLAND_DISPLAY","<none>"),
        "TERM: "+os.environ.get("TERM","<none>"),
        "PATH: "+os.environ.get("PATH","<none>"),
        "Disk: "+command_output(["df","-h",str(game_dir)])
    ]
    for path in ("/dev/fb0","/dev/dri","/dev/mali0","/dev/snd"):
        lines.append(f"{path}: {'present' if os.path.exists(path) else 'missing'}")
    for tool in ("python3","bash","sh","unzip","xz","7z","dialog"):
        lines.append(f"tool {tool}: {'yes' if shutil.which(tool) else 'no'}")
    Path(log).parent.mkdir(parents=True,exist_ok=True)
    with open(log,"a",encoding="utf-8") as f:
        f.write("\n=== Gatito-Extrator diagnostics ===\n")
        f.write("\n".join(lines)+"\n")
    return lines

def demo(log):
    for pct,stage in [(0,"Inicializando interface"),(15,"Coletando ambiente"),
                      (35,"Detectando ferramentas"),(55,"Simulando staging"),
                      (75,"Validando artefatos"),(92,"Preparando publicação"),
                      (100,"Teste visual concluído")]:
        draw(pct,stage,"Interface ativa — fluxo ainda não encerrado",log)
        time.sleep(0.45)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--game-dir",required=True)
    ap.add_argument("--recipe",required=True)
    ap.add_argument("--engine",required=True)
    ap.add_argument("--log",required=True)
    ap.add_argument("--input")
    ap.add_argument("--abi")
    ap.add_argument("--demo",action="store_true")
    ap.add_argument("--no-pause",action="store_true")
    a=ap.parse_args()
    game_dir=Path(a.game_dir).resolve()
    recipe=Path(a.recipe).resolve()
    engine=Path(a.engine).resolve()
    details=collect_data(game_dir,recipe,engine,a.log)
    draw(5,"Ambiente detectado","\n".join(details[-4:]),a.log)

    if a.demo:
        demo(a.log)
        rc=0
    else:
        cmd=[sys.executable,str(engine),str(recipe),"--game-dir",str(game_dir),"--validation-delay","0.15"]
        if a.input: cmd += ["--input",a.input]
        if a.abi: cmd += ["--abi",a.abi]
        draw(8,"Iniciando extrator","Interface permanece aberta durante o processo",a.log)
        with open(a.log,"a",encoding="utf-8") as logf:
            logf.write("\n=== Gatito-Extrator run ===\n")
            logf.write("CMD: "+" ".join(cmd)+"\n")
            p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
            last="Executando..."
            pct=8
            for raw in p.stdout:
                line=raw.rstrip()
                logf.write(line+"\n")
                if line.startswith("GATITO_STAGE|"):
                    try:
                        _,value,msg=line.split("|",2)
                        pct=int(value); last=msg
                    except ValueError:
                        last=line
                elif line:
                    last=line[:WIDTH]
                draw(pct,last,"Processo ativo — saída também registrada no log",a.log)
            rc=p.wait()
        draw(100 if rc==0 else pct,
             "CONCLUÍDO — artefatos validados" if rc==0 else "ERRO — processo terminou",
             f"exit={rc}\nLog preservado para análise",a.log)

    if not a.no_pause:
        try:
            input("\nPressione ENTER para fechar o Gatito-Extrator...")
        except EOFError:
            time.sleep(2)
    return rc

if __name__=="__main__":
    raise SystemExit(main())
