# Marmalade S3E

<div align='center'>

**Jogos:** Need for Speed Shift · The Sims 3 · Sonic 4 Episode I  
**Origem:** Android · **ABI:** ARM32; hard-float registrado para Shift e Sims 3

</div>

> [!NOTE]
> O catálogo identifica estes jogos como Marmalade S3E. Esta ficha é um roteiro para investigar cada input específico, não prova que compartilhem loader, versão do SDK, extensões ou renderer.

## O que procurar

Marmalade/S3E é um runtime nativo com APIs do SDK e extensões que intermediam ciclo de vida, gráficos, input, áudio, arquivos e serviços do dispositivo. A build Android também pode depender de bootstrap Java/JNI e bibliotecas Bionic. Funções podem estar ligadas estaticamente; não encontrar um ELF chamado Marmalade não descarta a engine.

Use como pistas de triagem os ELFs ARM do APK, dependências/imports, símbolos e strings de inicialização, classes Java/JNI, dados da mesma build e chamadas de surface, loop, pausa, input e áudio. Confirme a hipótese cruzando pacote, dependências e comportamento; uma string isolada não basta.

## Roteiro de engenharia reversa

| Etapa | Inspecione | Resultado esperado |
|---|---|---|
| Identidade | APK/splits, package ID, versão, ABI, OBB e arquivos adicionais | Inventário da cópia do usuário |
| Bootstrap | Manifesto, Activity, JNI, ordem de carga e loop principal | Diagrama Activity → inicialização nativa → loop |
| Fronteira S3E | Imports/símbolos, lifecycle, device, arquivos e extensões | Contratos com assinatura, thread, argumentos e efeito |
| Renderização | API, contexto/surface, resolução, buffers e recursos | Caminho até um frame visível |
| Áudio e input | Formato, fila/callback, pressionar/soltar, pausa/retomada | Testes independentes de som e controles |
| ABI | ELF flags, ARM/Thumb, dependências e chamadas float/double | Fronteira Android ARM32 ↔ Linux ARM32 documentada |
| Validação | QEMU smoke test e execução física | Resultado ligado a hash, aparelho, CFW e log sanitizado |

### ARM32: confirme a convenção de float

Shift e Sims 3 aparecem como ARM32 hard-float no catálogo. Sonic 4 está apenas como ARM32, sem convenção confirmada. Android ARMv7 e Linux ARMHF não são automaticamente interoperáveis. Verifique ELF flags, compilador e interfaces; faça uma ponte explícita para chamadas float/double, structs e callbacks. Não conecte funções por coincidência de nome.

## Estado por jogo

| Jogo | Evidência atual | Próximo passo |
|---|---|---|
| **Need for Speed Shift** | Anbernic RG40XX-H/muOS: jogável a 640×480, áudio ausente | Isolar áudio sem quebrar o launcher/runtime jogável |
| **The Sims 3** | Log RG351MP/dArkOSRE valida parcialmente o loader; gameplay desconhecido | Reproduzir com log completo e separar inicialização, vídeo, som e input |
| **Sonic 4 Episode I** | S3E listado; build, pacote, OBB, ABI e dados precisam de validação | Fixar amostra e dependências antes de mexer em loader/gráficos |

Fonte dos estados: [catalog/ports.json](../../catalog/ports.json). Não generalize o teste de Shift aos outros jogos.

## Smoke tests e limites

1. Faça inventário estático antes de iniciar a build.
2. Valide loader host e erros esperados para imports/dependências ausentes.
3. Em QEMU ARM user mode, teste apenas userland com sysroot correto; não é emulação do hardware Marmalade do portátil.
4. No aparelho, registre separadamente processo, primeiro frame, menu, controles, gameplay, áudio, pausa/retomada, save e saída.
5. Teste instalação limpa com dados legítimos do usuário e prove que reinstalar não apaga saves.

O teste de Shift ainda registra áudio ausente; Sims 3 e Sonic 4 seguem sem confirmação de gameplay. Nenhum tem pacote de release disponível no catálogo. Antes de adaptar código de terceiros, confirme origem, pin e licença e preserve avisos legais. APK, OBB, assets, bibliotecas proprietárias e saves ficam fora deste repositório.
