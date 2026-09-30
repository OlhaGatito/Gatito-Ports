# Gatito-Extrator

Área de teste separada do `tools/gatito-extract`.

Esta versão testa uma **UI gráfica real no handheld**, sem depender de
`printf`, ANSI, `dialog`, X11 ou Wayland.

## Arquitetura de teste

```
gatito-extrator.sh
      |
      v
    run.sh
      |
      v
 gatito-ui.py
      |
      +--> SDL2 / vídeo disponível
      |
      +--> fallback /dev/fb0
      |
      +--> eventos de controle SDL2
      |       ou /dev/input/event*
      |
      v
gatito-extract.py
```

O motor de extração continua separado da interface.

### Teste visual

```sh
./gatito-extrator.sh --demo
```

A interface deve ocupar a tela do handheld e permanecer aberta ao terminar.
Para este teste, **qualquer botão físico detectado encerra a UI**.

Não é necessário pressionar ENTER e o teste não depende de stdin.

### Teste real

```sh
./gatito-extrator.sh --game-dir /caminho/do/teste --recipe /caminho/da/receita.json --input /caminho/app.apk
```

### Backends

A UI tenta, nesta ordem, vídeo SDL2 com os backends disponíveis no sistema e,
se SDL2 não conseguir criar a janela, usa `/dev/fb0` diretamente.

A leitura de botões também não depende de teclado: quando SDL2 está ativo,
eventos SDL são usados; no fallback, os dispositivos Linux
`/dev/input/event*` são monitorados.

Se nenhum backend gráfico estiver disponível, o programa termina com erro em
vez de apresentar uma falsa UI no terminal.

## Observação

Esta é uma implementação de teste. O objetivo imediato é confirmar no R36S e
no muOS que a interface realmente aparece na tela e que um botão físico fecha
a tela. A integração definitiva com o The Sims 3 será feita depois que esse
teste for validado.

O diretório é separado para que esta experiência não altere o fluxo do
The Sims 3.
