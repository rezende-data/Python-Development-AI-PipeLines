**Idiomas / Languages:** 🇧🇷 [Português](README.pt-br.md) | 🇺🇸 [English](README.md)

# Analisador de Rendimento Imobiliário & Agregador de Oportunidades

Um framework programático de avaliação de imóveis que processa anúncios imobiliários, calcula as principais métricas de desempenho financeiro (Rendimento Bruto, Receita Operacional Líquida, Cap Rates) e compila memorandos de investimento institucional guiados por IA.

## 🚀 Valor de Negócio

* **Avaliação Automatizada (Underwriting):** Calcula a Receita Operacional Líquida (NOI) e Cap Rates em anúncios brutos.
* **Filtragem de Oportunidades:** Destaca propriedades alvo de alto rendimento, contabilizando despesas com impostos e manutenção.
* **Memorandos de Investimento:** Gera memorandos executivos de 3 tópicos via `openai/gpt-oss-120b` para as propriedades alvo.

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3.x
* **Cálculos Financeiros:** Aritmética Vetorizada do Pandas
* **Raciocínio com IA:** Groq API (`openai/gpt-oss-120b`)
* **Relatórios:** CSV, Excel (`.xlsx`), Memorando em Texto (`.txt`)

## 📐 Principais Fórmulas Financeiras Implementadas

* **Aluguel Bruto Anual** = Aluguel Mensal x 12
* **Receita Operacional Líquida (NOI)** = Aluguel Bruto Anual - Impostos - Manutenção (10%)
* **Cap Rate** = (NOI / Preço do Anúncio) x 100

## 📁 Entregáveis Gerados

* `real_estate_report.csv`: Métricas financeiras calculadas para todos os anúncios mapeados.
* `real_estate_report.xlsx`: Matriz de oportunidades formatada para investidores imobiliários.
* `real_estate_summary.txt`: Memorando de investimento institucional gerado por IA destacando os negócios com os melhores Cap Rates.

*Mantido por Rezende – Especialista em Engenharia de Dados & Automação.*

