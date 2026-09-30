# Engines em estudo

<div align="center">

### Do pacote Android ao port Linux ARM
**Inventário → runtime → mapa de interfaces → adapter → provas no aparelho**

</div>

> [!IMPORTANT]
> Esta área cataloga o que o Gatito Ports acompanha e oferece um roteiro de investigação. Engine identificada não significa port pronto nem compatibilidade confirmada.

## Mapa rápido

| Engine / escopo | Jogos catalogados | ABI de origem | Situação |
|---|---|---|---|
| [Marmalade S3E](Marmalade-S3E/README.md) | Need for Speed Shift, The Sims 3, Sonic 4 Episode I | ARM32; hard-float anotado para Shift e Sims 3 | Um teste jogável com áudio ausente; dois em investigação |
| [Unity IL2CPP](Unity-IL2CPP/README.md) | Minishoots Adventure | AArch64 | Binário, metadata e contrato em investigação |
| [Android nativo ARMv7](Android-Nativo-ARMv7/README.md) | Dungeon Hunter 4 | ARMv7; float ABI desconhecido | Runtime ainda não confirmado |

Os estados refletem o catálogo em [catalog/ports.json](../catalog/ports.json).

## Fluxo de investigação

<div align='center'>

**Cópia Android do dono** → **identidade, versão, ABI** → **ELF, JNI, assets e imports** → **ciclo de vida** → **gráficos, áudio e input** → **adapter Linux ARM** → **QEMU smoke test + handheld real**

</div>

QEMU ajuda a encontrar problemas de execução/ABI, mas não reproduz GPU, controles, áudio nem firmware do handheld. Só declare compatibilidade de aparelho após testar o artefato exato nele.

## Método comum

<details>
<summary><strong>01 · Fixe a amostra</strong></summary>

Use somente APK, splits, OBB e dados fornecidos legitimamente pelo dono. Registre pacote, versão, origem, ABI, arquivos e hashes locais. Mantenha os dados fora do Git e dos artefatos CI; não publique bibliotecas proprietárias, assets, saves ou logs privados.

</details>

<details>
<summary><strong>02 · Identifique runtime e ABI</strong></summary>

Liste arquivos do pacote e bibliotecas por ABI; inspecione ELF, dependências, símbolos, strings e manifesto. Nomes de biblioteca são pistas, não prova suficiente. Em ARMv7, determine também a convenção de ponto flutuante.

</details>

<details>
<summary><strong>03 · Mapeie inicialização e ciclo de vida</strong></summary>

Registre ordem de bibliotecas, inicializadores, JNI, surface/contexto, thread principal, callbacks de pausa/retomada e encerramento. Compare com referências da mesma família e versão. Não pule etapas para forçar uma cena ou chamar uma função interna.

</details>

<details>
<summary><strong>04 · Catalogue cada fronteira</strong></summary>

Separe loader/runtime, arquivos, gráficos, áudio, input, rede e persistência. Para cada chamada necessária, registre assinatura, argumentos, ownership, thread, efeito observável e teste negativo. Import obrigatório desconhecido deve produzir diagnóstico, nunca sucesso fictício.

</details>

<details>
<summary><strong>05 · Implemente e valide em camadas</strong></summary>

Mantenha alterações específicas do jogo num adapter próprio. Valide primeiro inventário e lógica host; depois carregamento, primeiro frame, input, áudio e persistência. Use QEMU para smoke tests com o sysroot correto e o handheld real para compatibilidade física.

</details>

<details>
<summary><strong>06 · Registre evidências e limites</strong></summary>

Anote hash do artefato, aparelho/revisão, SoC/GPU, CFW/versão, ABI, resolução, testes e itens desconhecidos. Diferencie inicia, chega ao menu, jogável, jogável com problemas e não confirmado. Um jogo não certifica toda a engine.

</details>

## Referências

O material NextOS disponível no ambiente contém guias de inventário Android, ABI, JNI, lifecycle, gráficos, input/áudio, extração e testes por runtime. Use como método, junto ao [NextOS Universal Ports](https://github.com/NextOs-Ports/nextos-universal-ports). Esses guias não são especificação universal de engines e não provam que outro jogo use a mesma versão/configuração.

Veja também [a arquitetura Gatito](../docs/ARCHITECTURE.md); atualize os estados em [catalog/ports.json](../catalog/ports.json).
