**Idiomas / Languages:** 🇧🇷 [Português](README.pt-br.md) | 🇺🇸 [English](README.md)

---

# Motor de Geração de Leads B2B no YellowPages

Um scraper B2B automatizado desenvolvido sob medida para pesquisa de mercado local e prospecção de leads frios. Ele extrai informações de contato direcionadas (nome da empresa, telefone, website, endereço, avaliação) por nicho e região geográfica.

## 🔗 Funcionalidades

* **Roteamento de Pesquisa Segmentado:** Consulte setores específicos em qualquer país, estado ou código postal (CEP).
* **Extração Inteligente de Dados:** Analisa os metadados das empresas de forma limpa, tratando campos ausentes de forma elegante.
* **Proteção Contra Duplicatas:** Elimina registros duplicados automaticamente ao longo das páginas de pesquisa.
* **Entregáveis Prontos para Clientes:** Gera arquivos estruturados em `.csv` e `.xlsx` organizados por cliente, localização ou nicho.

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3.10+
* **Bibliotecas:** `requests`, `beautifulsoup4`, `lxml`, `pandas`, `openpyxl`

## ⚙️ Instalação & Uso

```bash
# Clone o repositório
git clone [https://github.com/rezende-data/Python-Development-AI-PipeLines.git](https://github.com/rezende-data/Python-Development-AI-PipeLines.git)
cd Python-Development-AI-PipeLines/YellowPages_Lead_Gen

# Instale os requisitos
pip install requests beautifulsoup4 lxml pandas openpyxl

# Execute o pipeline de raspagem
python main.py

