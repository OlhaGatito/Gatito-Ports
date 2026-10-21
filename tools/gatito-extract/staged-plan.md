# Gatito Extractor — cadeia com fallback

Regra de execução: **OK → próxima etapa**; **ERRO → tentar outra rota**; **todas as rotas falharam → PARAR**.

Cada tentativa é apresentada na UI. Um fallback só é considerado bem-sucedido depois de passar pelo mesmo checkpoint da rota principal.

```text
ETAPA N → rota principal → OK → próxima etapa
             │
             ERRO
             ↓
          rota 2 → OK → próxima etapa
             │
             ERRO
             ↓
          rota 3 → OK → próxima etapa
             │
             ERRO
             ↓
          todas falharam → PARAR
```

O estado dos arquivos existentes no repositório não substitui a validação dos artefatos produzidos a partir do APK/OBB fornecido pelo usuário.
