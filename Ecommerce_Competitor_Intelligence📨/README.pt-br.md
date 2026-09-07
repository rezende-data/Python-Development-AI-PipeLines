**Idiomas / Languages:** 🇧🇷 [Português](README.pt-br.md) | 🇺🇸 [English](README.md)

# Inteligência de Concorrência para E-Commerce & Motor de Precificação com IA

Um pipeline automatizado de ETL e análise de mercado construído em Python. Esta ferramenta ingere dados de catálogos de e-commerces alvo, calcula disparidades de preços relativas contra SKUs internos e utiliza o endpoint de LLM de alta velocidade da Groq (`openai/gpt-oss-120b`) para gerar relatórios executivos acionáveis.

## 🚀 Valor de Negócio

* **Otimização de Margem:** Identifica automaticamente inventário com preço abaixo ou acima do mercado.
* **Inteligência de Concorrência:** Monitora o status de estoque e os pontos de preço dos concorrentes em escala.
* **Suporte à Decisão Executiva:** Substitui a análise manual em planilhas por resumos de mercado instantâneos gerados por IA.

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3.x
* **Processamento de Dados:** Pandas, OpenPyXL
* **Análise com IA:** Groq REST API (`openai/gpt-oss-120b`)
* **Formatos de Exportação:** CSV, Excel (`.xlsx`), Texto (`.txt`)

## ⚙️ Arquitetura e Segurança

**Nota de Segurança:** As chaves de API são carregadas dinamicamente a partir de variáveis de ambiente locais ou do arquivo `groq_key.txt`. Nenhuma credencial é inserida diretamente no código (hardcoded) ou comitada no repositório.

## 📁 Entregáveis Gerados

* `ecommerce_report.csv`: Catálogo de SKUs normalizado com variações de preço.
* `ecommerce_report.xlsx`: Planilha formatada e pronta para apresentação ao cliente.
* `ecommerce_summary.txt`: Recomendações de precificação em nível executivo geradas por IA.

*Mantido por Rezende – Especialista em Engenharia de Dados & Automação.*

