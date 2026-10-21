# Port — The Sims 3 ✅

> Fonte do catálogo: `catalog/ports.json` (`the-sims-3`) · **repositório do port: [The-Sims-3-Android-port](https://github.com/OlhaGatito/The-Sims-3-Android-port)**

| Campo | Valor |
|---|---|
| Plataforma | Android → handheld ARM (muOS / PortMaster / R36S) |
| Runtime | Marmalade S3E · ARM32 hard-float |
| Extração | NXExtract (stage → hooks → validation → commit) validada |
| Status | ✅ **TOTALMENTE JOGÁVEL em muOS, sem falhas** (confirmação do usuário, 2026-10-21) |
| Engine ficha | [Engine/Marmalade-S3E](../../Engine/Marmalade-S3E/README.md) |

## Requisitos
- APK/OBB do seu backup próprio (BYO-data; nada é distribuído)
- muOS/PortMaster no aparelho; ~2 GB para dados extraídos

## Passo a passo (resumo)
1. Baixar o ZIP do [repositório do port](https://github.com/OlhaGatito/The-Sims-3-Android-port) (botão Code → Download ZIP).
2. Copiar a pasta do port para a pasta de ports do firmware.
3. Preparar os arquivos do jogo conforme `INSTAL.md` do port.
4. Abrir **The Sims 3** pelo PortMaster.

Reconstrução a partir do APK (opcional):
```sh
bash Sims3/scripts/reconstruct-port.sh [CAMINHO_DO_APK]
```

## Problemas históricos (resolvidos)
- `This build does not support SW rendering...` — ambiente sem GLES no início da investigação; superado com validação no aparelho.
- Gate pré-loader / extração transacional — validados e consolidados no launcher nxbootstrap do port.

## Problemas conhecidos
- Extensão de primeira execução depende da receita de extração reconhecer a cópia do APK do usuário (por versão).

## Logs/evidências
- RE de S3E: plugin Ghidra `S3ELoader/` no repositório do port.
- Relatório de acesso ao aparelho (R36S via USB) sanitizado no repo do port.
