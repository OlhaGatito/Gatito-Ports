# Android nativo ARMv7

<div align='center'>

**Jogo:** Dungeon Hunter 4 · **Runtime:** ainda não confirmado  
**ABI registrada:** ARMv7; float ABI desconhecido · **Estado:** investigação

</div>

> [!CAUTION]
> Este é um escopo de pesquisa, não uma engine confirmada. Não classifique Dungeon Hunter 4 como Unity, Unreal, Marmalade, Cocos ou SDL sem evidência do pacote e do fluxo de inicialização.

## O que significa “nativo Android”

Um APK pode misturar Java/Kotlin e bibliotecas C/C++ chamadas por JNI, NativeActivity ou um runtime conhecido. A presença de ELF nativo não revela quem controla loop, gráficos ou lifecycle. Identifique primeiro o bootstrap; classifique a engine somente depois.

## Roteiro

| Fronteira | Evidência | Pergunta |
|---|---|---|
| Pacote/ABI | APK, splits, manifesto, package/version, ABI dirs e OBB | Qual amostra completa foi analisada? |
| ELF | readelf headers/dynamic/symbols, dependências e ELF flags | ARMv7? ARM/Thumb? EABI? softfp/hard-float? Bibliotecas Android exigidas? |
| Bootstrap | Activity, NativeActivity, System.loadLibrary, exports JNI e JNI_OnLoad | Quem carrega cada ELF, em qual ordem e thread? |
| Render | EGL/GLES/Vulkan, lifecycle da surface, shaders e resolução | Qual backend inicia e qual o primeiro frame? |
| Dados | OBB/assets, caminhos e arquivos obrigatórios | Quais dados vêm da cópia do usuário e como são localizados? |
| Input/lifecycle | Touch/joystick, eventos de janela, pause/resume e foco | Quais eventos Android o jogo consome? |
| Áudio/saves | Backend, formatos, callbacks, paths e gravações | Som retoma? Saves sobrevivem a reinstalação? |

Símbolos ausentes ou renomeados não provam ausência de runtime. Combine imports, strings, layout, metadados e comportamento. Trate APK/binários como inputs não confiáveis; inspecione scripts antes de executá-los e use fixtures sem dados comerciais.

## Fronteira ARMv7

Determine ABI/ELF e dependências antes de carregar bibliotecas. Android ARMv7 e Linux ARMHF não são automaticamente compatíveis. Chamadas float/double, structs, callbacks, exceções C++ e ownership exigem contrato e ponte demonstrados. Não passe objetos C++ entre runtimes por coincidência binária.

Se JNI/Bionic for obrigatório, implemente apenas os serviços realmente chamados e registre ausências. Imports obrigatórios desconhecidos devem falhar com diagnóstico, nunca com stubs de sucesso.

## Quando reclassificar

Só renomeie esta pasta após registrar build/ABI confirmadas, evidência positiva do runtime, versão e contrato de plugins, mapa JNI/lifecycle, dependências de dados/gráficos/áudio/input/persistência e proveniência/licença de qualquer fonte considerada.

Até lá, preserve “runtime não confirmado” no [catálogo](../../catalog/ports.json).
