# Gatito Extractor

Extrator BYO-data para ports Linux do Gatito, inspirado no fluxo público do NXExtract do NextOS, mas com implementação e regras próprias.

## Fluxo

```text
dados do usuário → descoberta → receita → ABI → staging → validação → publicação
```

A primeira versão implementa descoberta em `gamedata/` ou por `--input`, receitas JSON, seleção de ABI, extração ZIP/APK/arquivo solto, staging, validação por tamanho/SHA-256 e publicação com recuperação em caso de falha.

### Regras

- APK/OBB/assets/bibliotecas proprietárias nunca entram no Git.
- O input do usuário nunca é apagado.
- A receita não executa shell arbitrário nem downloads.
- O ambiente/driver do jogo não é alterado pelo extrator.
- O payload ativo só é substituído depois da validação do staging.
- Marmalade/S3E, Unity/IL2CPP e outros runtimes podem ter receitas próprias.

## Receita mínima

```json
{
  "id": "example-port",
  "version": "1",
  "abi_order": ["arm64-v8a", "armeabi-v7a"],
  "extract": [
    {
      "source": {"patterns": ["lib/{abi}/libexample.so"]},
      "destination": "game/libexample.so"
    }
  ],
  "validate": [{"path": "game/libexample.so", "min_size": 1024}],
  "commit": {"root": "game"}
}
```

## Próximas etapas

`recipe-check`, `scan`, `verify`, APK splits, journal/retomada/rollback completo, UI gráfica adaptativa e integração com o primeiro port real.

O objetivo é reaproveitar a arquitetura de extração entre ports sem presumir que todos usam a mesma engine ou formato.
