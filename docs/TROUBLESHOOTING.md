# TROUBLESHOOTING (ports ARM do Gatito)

| Sintoma | Causa provável | Caminho |
|---|---|---|
| `This build does not support SW rendering...` | aparelho/CFW sem GLES (SW render ausente) | verificar driver Mali ativo (`gatito-probe.sh`); não é bug do loader |
| `SDL2_mixer unavailable` | SDL do aparelho sem mixer/sem backend | provar backend real (recusar `dummy`); bypass Oboe/wrapper (receita em AI-Port-Arm `docs/RECEITAS-MALI450.md`) |
| Áudio funciona, tela preta | depth/shader/Z-clipping | prova por pixel antes do `present` (receitas Mali-450) |
| Parser/mapping OK mas SIGSEGV em QEMU | differência QEMU vs hardware | sempre validar em físico primeiro (regra do projeto) |
| launcher retorna sem log | fronteira pré-runtime | separar log de bootstrap do log do jogo; `tee run.log` sempre |
| `Undefined Symbol` / crash em init_array | imports incompletos; PT_LOAD parcial | pipeline do AI-Port-Arm `new-port.sh` + docs/TROUBLESHOOTING.md do framework |
| eventos A/B invertidos no Trimui/dPad | layout Nintendo duplicado | mapa independente por aparelho (banco GPTK) |
| Extração "trava" e não marca stage | validação por arquivo pendente (só etapa confirmada avança) | conferir `extractor.json` e log das etapas (função `BUILD.ui`) |

Fontes de receitas detalhadas: [AI-Port-Arm/docs/TROUBLESHOOTING.md](https://github.com/OlhaGatito/AI-Port-Arm) e [RECEITAS-MALI450.md](https://github.com/OlhaGatito/AI-Port-Arm).
