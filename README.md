# 🐱 Gatito Ports

<div align="center">
  <img src="assets/sarue.svg" alt="Mascote Sarué da Gatito" width="120"><br>

**Ports, ferramentas e catálogo da família Gatito** — de jogos Android para handhelds ARM Linux
e para PC (recomp/native). Foco em Mali-450/GLES2 (muOS, ROCKNIX, ArkOS, Knulli).

[![Status](https://img.shields.io/badge/status-prot%C3%B3tipos%20e%20pesquisa-f59e0b?style=for-the-badge)](catalog/ports.json)
[![Ports](https://img.shields.io/badge/ports-5%20ARM%20%2B%203%20PC-2563eb?style=for-the-badge)](#-catálogo-de-ports)
[![Plataformas](https://img.shields.io/badge/alvo-RG40XX%E2%80%91H%20%7C%20R36S%20%7C%20RG351%20%7C%20PC-16a34a?style=for-the-badge)](#-catálogo-de-ports)
[![Regra](https://img.shields.io/badge/regra-BYO%20data%20(sem%20jogos)-dc2626?style=for-the-badge)](#-aviso-legal)

</div>

---

## 📑 Índice

- [O que você encontra aqui](#-o-que-você-encontra-aqui)
- [Catálogo de ports](#-catálogo-de-ports)
- [Como usar](#-como-usar)
- [Como compilar](#-como-compilar)
- [Ferramentas incluídas](#%EF%B8%8F-ferramentas-incluídas)
- [Documentação](#-documentação)
- [FAQ e troubleshooting](#-faq-e-troubleshooting)
- [Roadmap](#-roadmap)
- [Como contribuir](#-como-contribuir)
- [Créditos](#-créditos)
- [Aviso legal](#-aviso-legal)

---

## 📦 O que você encontra aqui

- **Catálogo por status** de ports ARM (Android → handheld) e PC (PS4 → recomp/native), com página de documentação por port;
- **Ferramentas próprias**: probe de sistema, extrator BYO-data com UI de progresso;
- **Fichas por engine** (Marmalade S3E, Unity IL2CPP, Android nativo) com roteiros de RE;
- **Política sem dados de jogo**: nenhum APK/OBB/BIOS/asset/save é distribuído — você fornece do seu próprio backup.

## 🎮 Catálogo de ports

Status: ✅ jogável · 🟨 quase · 🚧 em andamento · ❌ com falha / investigação

### Ports ARM (Android → handheld)

| Port | Runtime / método | Status | Doc |
|---|---|:---:|---|
| Need for Speed Shift | Marmalade S3E · ARM32 hf · loader próprio + DZ/LZMA | 🟨 jogável em muOS 640×480, sem áudio | [docs/ports/NFS-SHIFT.md](docs/ports/NFS-SHIFT.md) |
| The Sims 3 | Marmalade S3E · ARM32 hf · NXExtract (stage/commit validado) | 🚧 loader validado, gameplay pendente (GLES) | [docs/ports/THE-SIMS-3.md](docs/ports/THE-SIMS-3.md) |
| Sonic 4 Episode I | Marmalade S3E · ARM32 · RE do formato DZ | ❌ investigação (553 itens, `attr_end=0x43F5`) | [docs/ports/SONIC-4-EP1.md](docs/ports/SONIC-4-EP1.md) |
| Minishoots Adventure | Unity 6 IL2CPP · AArch64 | ❌ validando binário/metadata | [docs/ports/MINISHOOTS.md](docs/ports/MINISHOOTS.md) |
| Dungeon Hunter 4 | Android nativo · ARMv7 (ABI a definir) | ❌ mapeando ELF/JNI/GLES/áudio | [docs/ports/DUNGEON-HUNTER-4.md](docs/ports/DUNGEON-HUNTER-4.md) |

### Ports PC (console → Windows/Linux)

| Port | Jogo / método | Status | Obs |
|---|---|:---:|---|
| SpartanPort (God of War III Remastered) | PS4 → Windows/Linux · native + Vulkan | ✅ comunidade ativa (uso local) | dump próprio: CUSA01623 01.00/01.02 |
| Bloodborne (bbport) | PS4 → Windows · native + Vulkan | ✅ comunidade ativa (uso local) | dump próprio: CUSA03173, v1.09 p/ patches |
| Monster Hunter Tri | Wii → a investigar | ❌ decisão de abordagem pendente | sem dump registrado |

<details>
<summary>📖 Por que ports de console no catálogo Gatito?</summary>

Os ports de PC seguem a mesma disciplina do projeto: **executar o código do jogo legítimo
do usuário**, sem redistribuir arquivos. Eles servem como referência cruzada de técnicas
(barreiras gráficas, patching, drivers) compartilhadas com os ports ARM.
</details>

## 🚀 Como usar

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/OlhaGatito/Gatito-Ports.git
   ```
2. **Coloque os dados do jogo** que você possui (APK/OBB/arquivos) na pasta de dados do port — veja a página de documentação do port.
3. **Siga a página do port** (staging/extração com as ferramentas abaixo, depois o launcher `run`).

> O catálogo de status exige evidência física; nada é anunciado sem teste (filosofia do projeto).

## 🔨 Como compilar

Depende do método do port — a página de cada port tem os comandos exatos. O fluxo geral:

```sh
# probe do aparelho (somente-leitura) antes de qualquer tentativa
sh tools/gatito-probe.sh > gatito-system-report.txt 2>&1

# extrator BYO-data (staging + validação por etapa, UI de progresso)
python3 tools/gatito-extract/gatito-extract-v2.py --recipe receita.json
```

Toolchain/WSL2, paths e env: consulte o repo irmão
[Guia de Compilação By NextOS](https://github.com/OlhaGatito/Guia-compilacao-By-NextOS-lembrancas).

## 🛠️ Ferramentas incluídas

| 🧰 | Função |
|---|---|
| [`gatito-probe.sh`](tools/gatito-probe.sh) | Coleta info de CPU/GPU/CFW/SDL do aparelho (read-only). |
| [`tools/gatito-extract/`](tools/gatito-extract/README.md) | Extrator BYO-data geracional: descoberta → extração → validação → publicação; v2 atual + UI em `BUILD.ui/`. |
| [`tools/Gatito-Extrator/`](tools/Gatito-Extrator/README.md) | Geração anterior (UI antiga), mantida por histórico — **prefira `gatito-extract`.** |
| [`catalog/ports.json`](catalog/ports.json) | Fonte de verdade do catálogo (status + observações por aparelho). |

## 📚 Documentação

| Área | Onde |
|---|---|
| Arquitetura do projeto | [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) |
| Roadmap | [`docs/ROADMAP.md`](docs/ROADMAP.md) |
| Template de relatório de compatibilidade | [`docs/COMPATIBILITY-REPORT-TEMPLATE.md`](docs/COMPATIBILITY-REPORT-TEMPLATE.md) |
| Páginas por port | [`docs/ports/`](docs/ports/) |
| Fichas por engine | [`Engine/`](Engine/) (Marmalade S3E, Unity IL2CPP, Android Native) |
| Ferramentas | [`tools/README.md`](tools/README.md) |

## ❓ FAQ e troubleshooting

Veja [`docs/FAQ.md`](docs/FAQ.md) e [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md).

## 🗺️ Roadmap

Consulte [`docs/ROADMAP.md`](docs/ROADMAP.md) (fases 0–2 e matriz de evidência aparelho × CFW).

## 🤝 Como contribuir

- Abra uma issue com `gatito-system-report.txt` (confira que não contém caminhos pessoais).
- Mudanças por pull request e atualização de `catalog/ports.json` na mesma PR.
- Siga a política de evidência: **nada é anunciado sem teste físico**.

## 🧾 Créditos

- **NextOS framework** — referência metodológica (ver [AI-Port-Arm](https://github.com/OlhaGatito/AI-Port-Arm)).
- **PortMaster / harbourmaster** — infraestrutura de ports para handhelds.
- Ferramentas Gatito: autorais do projeto.

## ⚖️ Aviso legal

Este repositório **não distribui** jogos, APK, OBB, BIOS, saves, assets ou bibliotecas
proprietárias. O usuário fornece os arquivos a partir de sua própria cópia obtida legalmente.
Jogos citados são marcas de seus respectivos donos. Projeto sem afiliação com a Sega, Rockstar,
EA, Ubisoft, Sony ou autores dos ports de PC usados como base de estudo.

Licença do código: **GPL-2.0-or-later** (veja `LICENSE`). Ferramentas de terceiros mantêm as próprias licenças.
