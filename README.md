# 🧩 Gatito Ports

> **Catálogo colaborativo** de ports, ferramentas e scripts para handhelds Linux (Rockchip / RK3326, etc.).

<div align="center">

[![Status – pesquisa](https://img.shields.io/badge/status-pesquisa%20e%20prot%C3%B3tipos-f59e0b?style=for-the-badge)]
[![Catálogo – 5 ports](https://img.shields.io/badge/ports-5%20catalogados-2563eb?style=for-the-badge)]
[![Releases – nenhum](https://img.shields.io/badge/releases-ainda%20n%C3%A3o%20publicadas-64748b?style=for-the-badge)]

</div>

---

## 📦 O que você encontra aqui

| 🎲 Port | Runtime / ABI | Estado |
|---------|----------------|--------|
| **Need for Speed Shift** | Android / Marmalade S3E / ARM32 hard‑float | Jogável em muOS (áudio ainda não funciona) |
| **The Sims 3** | Android / Marmalade S3E / ARM32 hard‑float | Loader validado parcialmente; gameplay em teste |
| **Sonic 4 Episode I** | Android / Marmalade S3E / ARM32 | Investigação inicial |
| **Minishoots Adventure** | Android / Unity IL2CPP / ARM64 | Investigação de binário e dependências |
| **Dungeon Hunter 4** | Android / ARMv7 | Análise de ABI, JNI/Bionic, gráficos, áudio |

> ⚠️ **Aviso de dados:** este repositório **não** inclui APKs, OBBs, assets, bibliotecas proprietárias ou saves. Você deve prover esses arquivos legalmente a partir do seu próprio backup.

---

## 🛠️ Ferramentas incluídas

| 🧰 Ferramenta | Função |
|---------------|--------|
| `gatito‑probe.sh` | Coleta informações do sistema (CPU, GPU, CFW, versão). |
| `gatito‑extract/` | Implementação do **NXExtract** (stage → hooks → validation → commit) usado pelos ports. |
| `scripts/` | Scripts de setup e execução (`setup.sh`, `run.sh`). |

> 📖 **Documentação completa** das ferramentas está na pasta `tools/` do repositório **`Main`**.

---

## 📚 Documentação (centralizada)

| Documento | Localização |
|-----------|--------------|
| 📖 Catálogo de ports (JSON) | `Main/catalog/ports.json` |
| 🧭 Roadmap do projeto | `Main/docs/ROADMAP.md` |
| 🏗️ Arquitetura geral | `Main/docs/ARCHITECTURE.md` |
| ✅ Checklist de diagnóstico | `Main/docs/CHECKLIST.md` |
| 🗂️ Modelo de relatório de compatibilidade | `Main/docs/COMPATIBILITY-REPORT-TEMPLATE.md` |
| 📖 Guia de contribuição | `Main/CONTRIBUTING.md` |
| 🔐 Política de segurança | `Main/SECURITY.md` |

---

## 🚀 Como usar (passo‑a‑passo rápido)

1. **Clone** este repositório.
2. **Coloque** o APK/OBB do jogo na pasta `data/` do port desejado.
3. Execute o script de *setup*:
   ```bash
   ./setup.sh   # prepara o stage, extrai o .s3e, gera .dz, etc.
   ```
4. Rode o port:
   ```bash
   ./run.sh
   ```

> Os scripts exibem logs no terminal e criam arquivos de diagnóstico em `logs/`.

---

## 🧑‍💻 Contribuindo

1. **Fork** o repositório **`Main`** (código‑fonte, scripts e documentação). 
2. Adicione ou melhore um port, atualize `catalog/ports.json` e envie um *pull‑request* para `Main`. 
3. Quando o CI (GitHub Actions) validar o build, uma nova *release* será criada automaticamente neste repositório (`Gatito‑Ports`) contendo apenas os binários e scripts prontos para o usuário final.

---

## ⚖️ Licença

Todo o código está sob **GPL‑2.0‑or‑later**. Para detalhes, veja `Main/LICENSE`.

---
