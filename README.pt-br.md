**Idiomas / Languages:** 🇧🇷 [Português](README.pt-br.md) | 🇺🇸 [English](README.md)

---

# Pipelines de Web Scraping & Automação com IA em Python

Infraestrutura em Python pronta para produção desenvolvida para extração web automatizada, transformação de dados ETL (Pandas) e enriquecimento de alta velocidade com LLMs via APIs do Groq e OpenAI.

---

## 🚀 Resumo Executivo

Este repositório serve como um hub centralizado de portfólio para pipelines de dados end-to-end de nível empresarial, projetados para implantação comercial. Cada projeto conta com carregamento dinâmico e seguro de chaves de API, tratamento de rotinas anti-bot e relatórios multiformato (.csv, .xlsx, .txt).

---

## 📦 Projetos de Automação em Destaque

* **Enriquecimento de Leads B2B & Scoring com IA** (`/B2B_Lead_Enrichment`)
  * **Estratégia:** Transforma listas brutas de prospects em pipelines de vendas de alta conversão. Analisa dados firmográficos, atribui pontuação de ICP (Perfil de Cliente Ideal, 1–100) e gera automaticamente ganchos personalizados para abordagem comercial (cold outreach) via Groq.

* **Inteligência de Concorrência para E-Commerce** (`/ECommerce_Competitor_Intelligence`)
  * **Estratégia:** Entrega inteligência automatizada de preços para gestores de marcas. Monitora SKUs de concorrentes em tempo real, identifica gargalos de margem ou rupturas de estoque e gera recomendações de reajuste de preço guiadas por LLM.

* **Agregador de Oportunidades Imobiliárias** (`/Real_Estate_Deal_Aggregator`)
  * **Estratégia:** Acelera a análise de viabilidade de investimentos (underwriting). Extrai anúncios imobiliários de múltiplos mercados, calcula métricas-chave de rentabilidade (NOI e Cap Rates) e compila memorandos de aquisição automatizados.

* **Rastreador SaaS no Trustpilot** (`/Trustpilot_SaaS_Tracker`)
  * **Estratégia:** Explora o churn de concorrentes. Coleta avaliações de produtos SaaS, isola feedbacks negativos (1 a 2 estrelas) utilizando análise de sentimento por LLM e gera prospects qualificados para substituição de software.

* **Motor Gerador de Leads B2B (YellowPages)** (`/YellowPages_Lead_Gen`)
  * **Estratégia:** Prospecção B2B regional em alta velocidade. Extrai cadastros comerciais por região e nicho, trata campos ausentes, remove registros duplicados e exporta conjuntos de dados em CSV prontos para uso do cliente.

* **Pontuação Local & Gerador de Pitches (Yelp)** (`/Yelp_Local_Scorer`)
  * **Estratégia:** Identifica alvos estratégicos para agências. Realiza scraping de prestadores de serviços locais, pontua perfis incompletos e gaps de avaliação, e rascunha ganchos de abordagem direta de 2 frases para prospecção imediata.

---

## 🛠️ Stack Técnica Principal

* **Linguagens & ETL Core:** Python 3.x, Pandas, OpenPyXL, BeautifulSoup4, Requests
* **Orquestração de IA:** Groq REST API, OpenAI API
* **Arquitetura de Segurança:** Ingestão dinâmica de chaves via `groq_key.txt` / Variáveis de Ambiente (Zero credenciais expostas no código)
* **Persistência de Dados:** CSV, XLSX, JSON, Relatórios Executivos em Texto Formatado

---

*Desenvolvido por Rezende – Especialista em Engenharia de Dados & Automação.*
