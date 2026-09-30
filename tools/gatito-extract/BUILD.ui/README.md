# BUILD.ui

Camada visual do Gatito Extractor.

O motor não depende da interface. A UI recebe eventos GATITO_STAGE e mostra uma barra central de 0 a 100%.

Cada etapa segue o contrato:

1. iniciar etapa;
2. executar;
3. validar presença/tamanho/formato;
4. aguardar a validação;
5. somente então liberar a próxima etapa.

A barra representa progresso real, não um temporizador fictício.
