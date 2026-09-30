# Arquitetura inicial

Gatito Ports separa o pacote de cada jogo das ferramentas compartilhadas e dos dados que o usuário fornece.

## Componentes

```text
catalog/ports.json
  ├─ estado, runtime, ABI e evidência por port
  ├─ futura página de catálogo
  └─ futuro feed PortMaster, após validar o formato

PortMaster / frontend
  └─ launcher do jogo
      ├─ identifica a combinação de sistema
      ├─ aplica um perfil validado ou usa system-default
      ├─ instala/valida dados fornecidos pelo usuário, se necessário
      └─ inicia e supervisiona o runtime do jogo
```

## Pacote de jogo

Cada port deverá ter instruções próprias e declarar runtime, ABI, controles, arquivos necessários, CFWs testados e estado de evidência. A estrutura final ainda será ajustada conforme o primeiro port que virar release; caminhos ilustrativos não são contratos fixos.

Um pacote de release poderá conter launcher, runtime/loader redistribuível, perfis permitidos, documentação, metadados de catálogo e receitas de instalação BYO-data. Não deverá conter APK, OBB, IPA, dados do jogo, saves ou bibliotecas proprietárias.

## Perfil por sistema

Um perfil identifica pelo menos dispositivo/revisão, CFW/release, SoC/GPU, kernel, ABI, SDL/runtime e backend de vídeo. O nome do CFW isolado não seleciona driver. Sem correspondência exata, o launcher preserva o ambiente fornecido por PortMaster/CFW e registra `UNKNOWN`.

Perfis ficam ligados a resultados físicos específicos. O inventário de biblioteca disponível não basta para dizer qual driver foi carregado; o resultado precisa de log ou inspeção do processo ativo.

## Ferramentas compartilhadas

- `gatito-probe.sh`: inventário read-only para conhecer o alvo antes do port.
- `gatito-profile`: futuro resolvedor de perfis com fallback conservador.
- `gatito-extract`: futuro instalador transacional de dados do usuário por receita.
- `gatito-pack`: futuro validador/empacotador de releases.
- `catalog-builder`: futura geração de página/feed a partir do manifesto.

Cada ferramenta nasce com um caso real, fixtures sem dados de jogo e limite de compatibilidade documentado. Ferramentas planejadas não fazem parte da release atual.

## Evidências de pesquisa

As notas técnicas internas do proprietário ajudam a orientar as fichas públicas, mas não são copiadas automaticamente. Evidências devem ser revisadas e sanitizadas antes de publicação; caminhos pessoais, logs completos e hashes de conteúdo comercial não são publicados.
