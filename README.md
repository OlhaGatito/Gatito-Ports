<div align="center">

# 🐈 Gatito Ports

### Ports e ferramentas de compatibilidade para handhelds Linux

Projetos Android, Marmalade S3E e Unity em pesquisa — com foco em ports reproduzíveis, perfis seguros e dados fornecidos pelo usuário.

[![Status](https://img.shields.io/badge/status-pesquisa%20e%20prot%C3%B3tipos-f59e0b?style=for-the-badge)](https://github.com/OlhaGatito/Gatito-Ports)
[![Catálogo](https://img.shields.io/badge/ports-5%20catalogados-2563eb?style=for-the-badge)](catalog/ports.json)
[![Dados](https://img.shields.io/badge/jogos-dados%20do%20usu%C3%A1rio-16a34a?style=for-the-badge)](#aviso-sobre-dados-e-licen%C3%A7a)
[![Releases](https://img.shields.io/badge/releases-ainda%20n%C3%A3o%20publicadas-64748b?style=for-the-badge)](https://github.com/OlhaGatito/Gatito-Ports/releases)

[📚 Catálogo](catalog/ports.json) · [🧭 Roadmap](docs/ROADMAP.md) · [🧩 Arquitetura](docs/ARCHITECTURE.md) · [🛠️ Ferramentas](tools/README.md)

</div>

---

**Estado do projeto:** fundação em andamento. As fichas abaixo representam pesquisa e protótipos; ainda não são ports prontos para instalar.

## O que queremos construir

- ports organizados por jogo e runtime, com suporte a vários CFWs quando houver teste real;
- instalação dos dados a partir da cópia do usuário, sem distribuir APKs, OBBs, assets, saves ou bibliotecas proprietárias;
- perfis de execução que identificam aparelho/CFW/stack com segurança e preservam o ambiente padrão quando não há perfil comprovado;
- ferramentas próprias para inventário do aparelho, instalação transacional de dados, empacotamento e geração de catálogo;
- registros de compatibilidade ligados ao aparelho, firmware, artefato e log testados.

## Projetos acompanhados

| Port | Origem/runtime | Situação registrada |
|---|---|---|
| Need for Speed Shift | Android / Marmalade S3E / ARM32 hard-float | Jogável em teste muOS; áudio ainda não funciona |
| The Sims 3 | Android / Marmalade S3E / ARM32 hard-float | Loader validado parcialmente; gameplay ainda sem confirmação no registro |
| Sonic 4 Episode I | Android / Marmalade S3E / ARM32 | Investigação; validar pacote e dados antes de avançar o loader |
| Minishoots Adventure | Android / Unity 6 IL2CPP / ARM64 | Investigação de binário, metadata e runtime |
| Dungeon Hunter 4 | Android / ARMv7 | Investigação de ABI, JNI/Bionic, OBB, gráficos e input |

O estado inicial fica em [catalog/ports.json](catalog/ports.json). O [modelo de arquitetura](docs/ARCHITECTURE.md), o [roadmap](docs/ROADMAP.md) e o [modelo de relatório de compatibilidade](docs/COMPATIBILITY-REPORT-TEMPLATE.md) registram como vamos transformar essas investigações em ports reproduzíveis.

## Princípios

1. Confirmar jogo, versão, pacote, ABI e dados antes de mexer no loader.
2. Separar loader/runtime, SDL, vídeo, áudio, input e launcher ao diagnosticar.
3. Começar pelo ambiente que PortMaster/CFW já prepara; aplicar overrides só com evidência para aquela combinação.
4. Distinguir documentado, provável e confirmado em hardware.
5. Não marcar compatibilidade com um CFW por ter iniciado em outro aparelho ou firmware.
6. Guardar artefatos e logs com identificador de versão, sem enviar conteúdo proprietário.

## Primeira ferramenta

[tools/gatito-probe.sh](tools/gatito-probe.sh) coleta informações do sistema e da stack gráfica em modo somente leitura. Ela não escolhe nem altera drivers; ajuda a construir a matriz de perfis com dados reais. Veja [como executar e interpretar](tools/README.md).

## Próximos passos

Veja [docs/ROADMAP.md](docs/ROADMAP.md) para as fases de catálogo, diagnóstico, instalação de dados, launcher por perfil e publicação.

## Base técnica

O projeto estuda fluxos públicos como o [NextOS Universal Ports](https://github.com/NextOs-Ports/nextos-universal-ports) para entender catálogo, pacotes BYO-data, instalação e publicação. O Gatito terá identidade, código, documentação e ferramentas próprias; não reutiliza código do NextOS sem verificar licença e atribuição.

## Aviso sobre dados e licença

Os ports exigem arquivos obtidos legitimamente pelo usuário. Nenhum dado de jogo é distribuído por este repositório. Nenhuma licença geral de código foi escolhida ainda; cada componente deverá declarar sua licença antes da primeira release.
