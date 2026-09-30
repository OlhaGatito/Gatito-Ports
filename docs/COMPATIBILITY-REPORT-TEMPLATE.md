# Relatório de compatibilidade — modelo

Copie este arquivo para cada execução importante. Um relatório descreve uma combinação específica; ele não cria suporte geral para o CFW ou o modelo.

## Identificação

- Port / ID:
- Commit do port:
- Artefato do port e SHA-256 (se aplicável):
- Data:
- Responsável pelo teste:

## Aparelho e sistema

- Fabricante/modelo/revisão:
- SoC / GPU:
- CFW e versão/build:
- Kernel (`uname -a`):
- ABI do userspace:
- Display/saída:
- Relatório do `gatito-probe.sh`:

## Entrada do usuário

- Versão/build legal do jogo:
- Tipo de pacote (APK/split/XAPK/OBB/arquivo solto):
- ABI detectada:
- Validação usada (hash/tamanho/arquivos sentinela):
- Dados instalados e local:
- Nenhum dado proprietário foi anexado ao relatório: sim/não

## Perfil de execução

- Perfil escolhido (`system-default` ou nome):
- Motivo da seleção:
- `SDL_VIDEODRIVER` antes/depois:
- `LD_LIBRARY_PATH` antes/depois:
- EGL/GLES/GL e SDL identificados:
- Bibliotecas gráficas realmente carregadas (por log ou `/proc/<pid>/maps`):
- Configuração de áudio:
- Configuração de input:

## Resultado por etapa

| Etapa | PASS / PARTIAL / FAIL / UNKNOWN | Evidência ou log |
|---|---|---|
| Localizou launcher e pasta do port | UNKNOWN | |
| Encontrou e validou os dados | UNKNOWN | |
| Loader executou | UNKNOWN | |
| Dependências e símbolos resolveram | UNKNOWN | |
| SDL inicializou | UNKNOWN | |
| EGL/contexto foi criado | UNKNOWN | |
| Primeiro frame foi apresentado | UNKNOWN | |
| Gameplay e transições | UNKNOWN | |
| Áudio audível | UNKNOWN | |
| Controles | UNKNOWN | |
| Saves e reload | UNKNOWN | |
| Saída limpa / retorno ao menu | UNKNOWN | |

## Observações e próxima ação

- O que mudou desde a última execução:
- Primeiro estágio que falhou ou ficou parcial:
- Uma hipótese por testar:
- Resultado que faria essa hipótese ser aceita/rejeitada:
- Configuração conhecida para rollback:

## Privacidade

Anexe somente logs necessários e revise caminhos, nomes de usuário, identificadores e tokens antes de publicar. Nunca anexe APK, XAPK, IPA, OBB, assets, saves ou bibliotecas proprietárias.
