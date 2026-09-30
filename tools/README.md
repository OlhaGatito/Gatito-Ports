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



### `gatito-extract`

Extrator BYO-data baseado nos princípios do fluxo público do NXExtract: descoberta por conteúdo, receita declarativa, seleção de ABI, staging, validação e publicação segura.

Arquivos:
- [README](gatito-extract/README.md)
- [gatito-extract.py](gatito-extract/gatito-extract.py)
- [receita de exemplo](gatito-extract/extractor.example.json)

A implementação do Gatito é própria. O NXExtract serve como referência arquitetural; não copiamos o código do NextOS. APK/OBB e dados proprietários continuam sendo fornecidos pelo usuário.

Fluxo atual: `descoberta` → `extração` → `validação da etapa` → `validação final` → `publicação`.

A pasta `BUILD.ui/` recebe eventos reais do motor e mantém uma barra central de progresso. Cada etapa só avança depois que o arquivo produzido foi confirmado. A pausa de validação é configurável e não representa progresso falso.

## Planejadas

| Ferramenta | Objetivo | Estado |
|---|---|---|
| `gatito-profile` | Resolver perfis por fingerprint exato do aparelho/CFW/runtime, com fallback para o ambiente padrão | Planejamento; aguarda relatórios reais de vários aparelhos |
| `gatito-extract` | Instalar dados BYO a partir de receitas, com staging, validação por etapa e UI de progresso | Implementação inicial; integração por port em andamento |
| `gatito-pack` | Validar arquivos, licenças, ABI, permissões, logs e checksums antes de gerar release | Planejamento |
| `catalog-builder` | Gerar página de ports e feed PortMaster a partir de uma fonte única | Planejamento; requer confirmação do schema PortMaster atual |

## Regras

- Não enviar pacote ou log para serviço remoto automaticamente.
- Não embutir conteúdo de jogo nem executar shell arbitrário vindo de uma receita.
- Ferramentas futuras precisam ter modo diagnóstico claro, logs revisáveis e uma opção de rollback quando alterarem dados.
- Não anunciar suporte até haver evidência na combinação publicada.
