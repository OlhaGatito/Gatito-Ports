# Port — Sonic 4 Episode I ❌

> Fonte do catálogo: `catalog/ports.json` (`sonic-4-episode-i`)

| Campo | Valor |
|---|---|
| Plataforma | Android → handheld ARM |
| Runtime | Marmalade S3E · ARM32 |
| Status | ❌ investigação (formato DZ) |

## Descobertas registradas
- APK: `sonic-4-episode-i-v1-5-0.apk`; OBB: `main.6200011.com.sega.sonic4epi.obb`
- `mid.dz` / `high.dz`: **553 itens** catalogados; `attr_end = 0x43F5`
- Formato DZ/LZMA: ver Guia de Compilação `docs/marmalade/S3E-DZ-LZMA.md`

## Regra do projeto
Extração ≠ runtime: essas descobertas **não** concluem o port. Nenhum loader ou gráfico iniciou.

## Próximos passos
1. Confirmar ABI/imports do ELF no APK correto.
2. Verificar assets e OBB esperados antes de loader/graphics.
