# Ferramentas

## Disponível

### `gatito-probe.sh`

Coleta informações úteis do Linux handheld em modo somente leitura e imprime para stdout:

- kernel e arquivos de identificação do sistema;
- modelo/compatibles do device tree, quando acessíveis;
- nodes `/dev/dri` e `/dev/fb*`;
- variáveis SDL/display selecionadas;
- nomes de bibliotecas EGL/GLES/Mali/SDL em diretórios comuns;
- presença de helpers PortMaster no `PATH`.

Execute com shell POSIX:

```sh
sh tools/gatito-probe.sh > gatito-system-report.txt 2>&1
```

O probe não instala bibliotecas, não força backend, não inicia o jogo e não envia o relatório. Os caminhos e valores de ambiente podem identificar sua instalação; revise o arquivo antes de compartilhar. Arquivos encontrados são candidatos, não prova do driver ativo.

## Planejadas

| Ferramenta | Objetivo | Estado |
|---|---|---|
| `gatito-profile` | Resolver perfis por fingerprint exato do aparelho/CFW/runtime, com fallback para o ambiente padrão | Planejamento; aguarda relatórios reais de vários aparelhos |
| `gatito-extract` | Instalar dados BYO a partir de receitas, com staging, validação, retomada e rollback | Planejamento; escolher primeiro port com extração necessária |
| `gatito-pack` | Validar arquivos, licenças, ABI, permissões, logs e checksums antes de gerar release | Planejamento |
| `catalog-builder` | Gerar página de ports e feed PortMaster a partir de uma fonte única | Planejamento; requer confirmação do schema PortMaster atual |

## Regras

- Não enviar pacote ou log para serviço remoto automaticamente.
- Não embutir conteúdo de jogo nem executar shell arbitrário vindo de uma receita.
- Ferramentas futuras precisam ter modo diagnóstico claro, logs revisáveis e uma opção de rollback quando alterarem dados.
- Não anunciar suporte até haver evidência na combinação publicada.
