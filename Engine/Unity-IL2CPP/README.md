# Unity com IL2CPP

<div align='center'>

**Jogo:** Minishoots Adventure · **Origem:** Android · **ABI:** AArch64 · **Estado:** investigação

</div>

> [!WARNING]
> Unity 6 IL2CPP é a classificação registrada para este jogo, não um runtime portátil genérico. A versão/build e os binários ainda precisam ser validados. Nenhum port ou suporte gráfico está confirmado.

## Composição da build

Uma build Android Unity IL2CPP combina player Unity, código gerado IL2CPP e metadata, bootstrap Android/JNI, plugins nativos e dados do jogo. A composição muda por versão/configuração. Encontrar libunity ou libil2cpp não fornece por si só um runtime Linux ARM compatível.

A investigação deve descobrir o contrato da build e estimar o adapter necessário. Não presuma que o Unity Editor exportará Linux ARM a partir do APK, nem misture metadata e bibliotecas de versões diferentes.

## Procedimento

### 1. Fixe a build

Registre package ID, versão, splits, ABI, versão Unity, dados e ELFs do pacote. Localize player, IL2CPP, metadata e plugins quando existirem; confirme seus caminhos no input em vez de presumir layout. Mantenha arquivos do jogo em armazenamento privado.

### 2. Mapeie bootstrap e ciclo de vida

Documente Activity → JNI → configuração do player → surface/contexto → loop → pausa/retomada/encerramento. Catalogue classes e métodos Java realmente chamados, bibliotecas carregadas e dependências Android/Bionic. Separe chamadas obrigatórias de plugins opcionais.

### 3. Mapeie IL2CPP e dados

Relacione biblioteca gerada, metadata da mesma build, arquitetura, imports e arquivos de dados. Registre versões e hashes localmente para não misturar peças incompatíveis. Se algo estiver ausente, deixe a incerteza explícita. Não pule o bootstrap chamando uma função interna.

### 4. Meça gráficos

Determine se a build inicia GLES ou Vulkan, como cria surface/resolução, quais shaders/extensões usa e como apresenta frames. Separe falha de contexto, shader, textura/formato, framebuffer e apresentação. Áudio ativo ou processo vivo não comprova imagem.

### 5. Prove áudio, input e persistência

Catalogue plugins/APIs de áudio, controles/toque, suspensão, arquivos e saves. Valide caminhos isoladamente e prove save/reload após encerrar o processo. Registre diferenças entre host e handheld.

### 6. Escolha estratégia Linux

Após mapear o contrato, avalie recompilar com código disponível, adaptar uma camada suportada ou implementar compatibilidade para a build Android. São estratégias distintas e dependem de fontes, licenças e APIs reais. Mantenha protótipos no escopo do jogo.

## Relação com estudos NextOS

O material NextOS disponível no ambiente tem estudos Unity separados por build e guias de inventário Android, ABI, gráficos/texturas, input/áudio e diagnóstico. Use-os para formular medições, não como prova de que Minishoots usa a mesma configuração nem como autorização para reutilizar código/dados. Confira origem e licença antes de qualquer reutilização.

## Estado registrado

O próximo passo em [catalog/ports.json](../../catalog/ports.json) é validar binário e metadata correspondentes e identificar o contrato de runtime antes de selecionar uma stack gráfica. Minishoots ainda não tem observações de aparelho. Registre cada nova evidência com build/ABI, aparelho/CFW, artefato, resultado e limitações. Um título não certifica Unity 6 em geral.
