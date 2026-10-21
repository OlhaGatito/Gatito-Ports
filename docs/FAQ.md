# FAQ

## Geral

**Este repositório distribui jogos?**
Não. Nenhuma APK, OBB, BIOS, save, asset ou biblioteca proprietária. Só código próprio, scripts, documentação e catálogo. Você fornece os arquivos da sua cópia legal.

**Qual handhelds são alvo?**
RG40XX-H (muOS), R36S, RG351MP (dArkOSRE) e outros RK3326/Mali-450 com CFWs muOS/ROCKNIX/ArkOS/Knulli. Ports de PC (SpartanPort/Bloodborne) rodam em Windows/Linux x86-64.

**Onde está o código do loader/framework?**
No [AI-Port-Arm](https://github.com/OlhaGatito/AI-Port-Arm): a base `.so` Android e o suíte NextOS V5 (referência metodológica).

**Qual a diferença entre `tools/gatito-extract/` e `tools/Gatito-Extrator/`?**
`gatito-extract` é a implementação atual (v2 maior, UI em `BUILD.ui/`). `Gatito-Extrator` é a **geração anterior** mantida por histórico de debug — prefira `gatito-extract`.

## Procedimentos

**Como registro evidência de teste de aparelho?**
1. `sh tools/gatito-probe.sh > gatito-system-report.txt 2>&1` (revise antes de compartilhar);
2. Anexe o report + launcher log à issue/PR;
3. Atualize `catalog/ports.json` com `result` e `evidence_level`.

**Posso abrir PR adicionando um port?**
Sim, seguindo o modelo dos campos de `ports.json` (id, runtime, status, next_step) e criando `docs/ports/<NOME>.md`.

## Erros comuns
Ver [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md).
