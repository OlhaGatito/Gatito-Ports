# Roadmap

Este roadmap começa pelas necessidades comprovadas nos ports do Gatito. Itens marcados como planejados ainda não são ferramentas disponíveis.

## Fase 0 — Base do repositório

- [x] Criar catálogo inicial dos cinco projetos registrados.
- [x] Definir política BYO-data e estados de evidência.
- [x] Criar o primeiro coletor read-only de sistema.

## Fase 1 — Coletar evidência reproduzível

- [ ] Rodar `gatito-probe.sh` em aparelhos/CFWs diferentes e guardar relatórios sem dados de jogo.
- [ ] Preencher relatórios para RG40XX-H/muOS, RG351MP/dArkOSRE e os aparelhos usados nos próximos ports.
- [ ] Identificar driver/backend realmente carregados e registrar logs do loader.
- [ ] Vincular cada resultado ao commit do port e à versão do firmware.

**Saída:** matriz real aparelho × CFW/release × arquitetura × SDL/vídeo/áudio/input, com `PASS`, `PARTIAL`, `FAIL` ou `UNKNOWN` por etapa.

## Fase 2 — Launcher por perfil seguro

- [ ] Especificar assinatura de sistema com modelo/revisão, CFW/release, SoC/GPU, kernel, ABI e SDL/runtime.
- [ ] Criar perfis por combinação comprovada, mantendo `system-default` como fallback.
- [ ] Preservar os ambientes conhecidos de áudio de Sims 3 e NFS Shift.
- [ ] Fazer o launcher localizar symlinks, dados e `run.sh`; gerar log antes de operações frágeis; supervisionar o PID próprio.

**Saída:** componente compartilhado somente depois de validar o contrato em pelo menos dois ports.

## Fase 3 — Instalador BYO-data

- [ ] Reconhecer fontes Android escolhidas pelo usuário (APK/splits/APKM/APKS/XAPK/OBB/arquivos soltos) conforme cada jogo.
- [ ] Validar package/version/ABI/arquivos sentinela antes de instalar.
- [ ] Extrair para staging na mesma partição, validar e publicar atomicamente com backup/rollback.
- [ ] Nunca apagar o pacote de entrada ou substituir dados ativos antes da validação.
- [ ] Manter as regras do jogo em receitas pequenas e revisáveis, sem shell arbitrário embutido no manifesto.

**Saída:** primeira receita baseada em um port que realmente precise de instalação, com fixtures sintéticas e teste físico.

## Fase 4 — Empacotamento e releases

- [ ] Empacotar apenas código de compatibilidade e dependências redistribuíveis com licença verificada.
- [ ] Gerar checksum, notas de versão, controles, instruções BYO-data e matriz de compatibilidade por artefato.
- [ ] Validar estrutura, permissões, ABI e limite de glibc automaticamente.
- [ ] Fazer teste limpo no aparelho antes de declarar a release pronta.

## Fase 5 — Catálogo e ferramentas de publicação

- [ ] Usar `catalog/ports.json` como fonte única.
- [ ] Gerar uma página simples com capas autorizadas, gênero, estado e download; imagens de jogo ficam fora até ter fonte/licença verificada.
- [ ] Gerar o feed de PortMaster somente depois de validar o formato com a documentação atual e testar instalação real.
- [ ] Publicar release estável e canal rolante apenas quando houver automação reproduzível.

## Critério de conclusão de um port

Um port só recebe `release-ready` quando o artefato exato passa instalação limpa e teste físico da cadeia necessária: launcher, dados, loader, primeiro frame, gameplay, áudio, controles, saves e saída. O estado de cada etapa permanece visível mesmo quando uma parte falha.
