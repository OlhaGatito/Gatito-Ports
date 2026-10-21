# REVISAO — inventário 2026-10-21

Inventário+correções da frente "revisão geral dos repos". Fonte do levantamento: análise programática
(links com Test-Path, URLs testadas por HTTP, hashes comparados).

## Encontrado e CORRIGIDO
1. **README inteiro desatualizado**: apontava para repo "Main" inexistente e para
   `scripts/setup.sh`, `run.sh`, `data/`, `logs/`, `CONTRIBUTING.md`, `SECURITY.md`, `CHECKLIST.md`,
   `LICENSE` — todos inexistentes → README reescrito com a árvore real, catálogo com status e links
   para `docs/ports/`.
2. **Badges malformados** (destino vazio `[![...](img)]`) → badges completos no novo README.
3. **`docs/ports/` criada** com página por port (NFS Shift, Sims 3, Sonic 4, Minishoots, DH4), FAQ e
   TROUBLESHOOTING.
4. **`catalog/ports.json` expandido**: 3 ports de PC (spartanport, bloodborne-bbport, monster-hunter-tri)
   registrados com política BYO-data.
5. **Ref. morta em `tools/Gatito-Extrator/run.sh`**: (`gatito-extract-v3.py` não existe) → corrigido para
   v2 com fallback e aviso de deprecação.
6. **`tools/gatito-extract/staged-plan.md`** tinha `\n` literais no lugar de quebras de linha → recodificado.
7. **`extractor.example.json` de `Gatito-Extrator/`** vazio (`extract: []`) → apontado como placeholder no
   README da ferramenta (não alterado: é histórico).
8. **LICENSE ausente** (README declarava GPL-2.0-or-later mas não existia arquivo) → `LICENSE` adicionado.
9. **.gitignore ausente** → adicionado (dados de jogo, staging, reports).
10. Grafias padronizadas: `RG40XX-H` (antes RG40XX H / RG 40XX-H), "muOS".

## Em validação (não testado)
- `tools/new-port-arm.sh`/`build-port.sh`/`new-port.sh` de AI-Port-Arm (da base nextos_ports_android):
  **não testado** nesta sessão (requer toolchain cross ARM no WSL2) — docs marcadas como tal.
- Comandos `./setup.sh`/`./run.sh` do README antigo **removidos** porque não existiam (nunca testáveis).

## Caminhos pessoais
- Nenhum caminho `C:\Users\Fabricio` exposto nos textos deste repo (verificado por varredura).

## Pendências/decisões
- Escolher a versão canônica do extrator e marcar a outra como "archived" no README (feito informativamente).
- Unificar texto de `Engine/` com `docs/ports/` (fichas gerais vs portas específicas) — ok manter os dois níveis.
- `opencode.yml`: funcional mas depende de `secrets.ANTHROPIC_API_KEY` no GitHub (já via `secrets.`, saudável).
- Dead-branch `test/gatito-extrator` — o branch antigo foi mantido (sem merge ainda).
