# Port — The Sims 3 🚧

> Fonte do catálogo: `catalog/ports.json` (`the-sims-3`) · memória técnica: [Lembra-e-Aprendizado-com-IA / Ports/The-Sims-3](https://github.com/OlhaGatito/Lembra-e-Aprendizado-com-IA)

| Campo | Valor |
|---|---|
| Plataforma | Android → handheld ARM |
| Runtime | Marmalade S3E · ARM32 hard-float |
| Extração | NXExtract (stage → hooks → validation → commit) **validado** |
| Status | 🚧 loader validado; gameplay depende de validação gráfica/dispositivo |
| Evidência | RG351MP/dArkOSRE — log parcial ("incomplete-log") |
| Engine ficha | [Engine/Marmalade-S3E](../../Engine/Marmalade-S3E/README.md) |

## Requisitos
- APK/OBB próprio + launcher NXExtract com dados BYO
- Aparelho com GLES (HW support) — veja problema abaixo

## Passo a passo (resumo)
1. NXExtract na receita do port (transacional, com validação por etapa).
2. Gate pré-loader → validação da extração → runtime.
3. Launcher único (runtime) — ver Guia de Compilação `projetos/The-Sims-3/NXEXTRACT-LAUNCHER.md`.

## Problemas conhecidos
- `This build does not support SW rendering, and the device does not have HW support.` — ambiente sem GLES; **não é bug do loader**.
- Áudio: precisa manter o ambiente de áudio conhecido do NFS enquanto revisa o launcher (próxima etapa).

## Correções aplicadas
- Extração transacional validada (logs completos exigidos no catálogo: `evidence_level: incomplete-log` até ter re-teste).
