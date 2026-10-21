# Port — Dungeon Hunter 4 ❌

> Fonte do catálogo: `catalog/ports.json` (`dungeon-hunter-4`)

| Campo | Valor |
|---|---|
| Plataforma | Android → handheld ARM |
| Runtime | Android nativo; contrato de runtime NÃO confirmado |
| ABI | ARMv7; float ABI a confirmar |
| Status | ❌ mapeamento inicial |

## Plano do catálogo
1. Inspecionar dependências ELF/`NEEDED`, exigências Bionic/JNI.
2. Acesso ao OBB, eventos de input e inicialização gráfica.
3. Confirmar engine e ABI (hard/soft float) antes de qualquer loader.

## Referência
- Métodos gerais: ficha [Engine/Android-Nativo-ARMv7](../../Engine/Android-Nativo-ARMv7/README.md)
