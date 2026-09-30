# Gatito Extractor — contrato de execução por etapas

A UI do Gatito Extractor não deve perguntar apenas se o payload final já existe. Ela deve acompanhar a preparação dos dados desde a entrada fornecida pelo usuário.

## Contrato

Para cada item da receita:
1. Procurar entrada: APK/APKM/APKS/XAPK/OBB ou arquivo suportado existe?
2. Verificar saída: o resultado esperado já existe? Se existe, validar antes de avançar. Se não existe, iniciar a extração correspondente.
3. Extrair: mostrar na UI o arquivo/etapa em execução.
4. Validar: existência, diretório não vazio quando aplicável, tamanho, SHA-256 e magic/header quando a receita fornecer.
5. Checkpoint: somente depois da validação o estágio seguinte é liberado.
6. Hook: quando a receita definir um estágio confiável, executá-lo e validar seu checkpoint.
7. Publicação: somente o staging completamente validado vira game/.

## Exemplo Sims 3

APK encontrado → extrair assets/The Sims 3.s3e → validar S3E → extrair assets/* → validar assets → executar hook de unpack S3E/LZMA → validar game.s3e.unpacked + XE3U → publicar → iniciar runtime.

A UI deve mostrar cada uma dessas etapas e nunca avançar para a próxima somente porque o tempo passou.

## Regra

A existência de um arquivo no repositório do port não significa que a etapa de extração foi cumprida. O que importa é o estado dos dados fornecidos pelo usuário e os artefatos produzidos durante a execução.