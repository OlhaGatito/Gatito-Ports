# Gatito-Extrator

Área de teste separada do tools/gatito-extract.

Objetivos desta primeira etapa:

- testar a interface visual sem envolver The Sims 3;
- manter a UI aberta durante todo o processo;
- coletar dados do sistema, ferramentas e dispositivos disponíveis;
- registrar a saída em logs/gatito-extrator.log;
- chamar o motor existente do Gatito Extractor, sem duplicá-lo;
- permitir teste visual puro com --demo.

Teste visual:
  ./gatito-extrator.sh --demo

A interface permanece aberta até ENTER.

Teste real:
  ./gatito-extrator.sh --game-dir /caminho/do/teste --recipe /caminho/da/receita.json --input /caminho/app.apk

O diretório é separado para que esta experiência não altere o fluxo do The Sims 3.
