# Port — Need for Speed Shift 🟨

> Fonte do catálogo: `catalog/ports.json` (`nfs-shift`) · repos do port: [need-for-speed-shift-Android-Port](https://github.com/OlhaGatito/need-for-speed-shift-Android-Port)

| Campo | Valor |
|---|---|
| Plataforma | Android → handheld ARM |
| Runtime | Marmalade S3E · ARM32 hard-float |
| Status | 🟨 Jogável em muOS 640×480; **áudio ausente** |
| Evidência | Teste físico RG40XX-H/muOS (`Playable at 640x480; audio is missing`) |
| Engine ficha | [Engine/Marmalade-S3E](../../Engine/Marmalade-S3E/README.md) |

## Requisitos
- APK/OBB da sua cópia própria (não distribuído)
- muOS/PortMaster no aparelho; espaço para extração transacional

## Passo a passo (resumo)
1. Extração do `.s3e`, divisão das arenas LZMA e conversão `.dz` → ver Guia de Compilação `docs/marmalade/S3E-DZ-LZMA.md`.
2. Loader ARMv7 hard-float (compila; ELF validado).
3. `parsing`, `veneers` e `mapping` comprovados. QEMU → SIGSEGV; hardware → jogável.

## Problemas e correções
- **Áudio**: `SDL2_mixer unavailable` em ambiente de teste; em físico nunca validado. → próxima etapa: provar áudio isoladamente preservando o caminho jogável.
- **SIGSEGV em QEMU** (user-space) diferente de aparelho → testar físico antes de depurar QEMU.

## Comandos/logs usados
- Guia completo: [docs/porting/NEED-FOR-SPEED-SHIFT.md no Guia de Compilação](https://github.com/OlhaGatito/Guia-compilacao-By-NextOS-lembrancas/blob/main/docs/porting/NEED-FOR-SPEED-SHIFT.md)

## Próximo passo
Investigar áudio de forma independente preservando o launcher/runtime já testável.
