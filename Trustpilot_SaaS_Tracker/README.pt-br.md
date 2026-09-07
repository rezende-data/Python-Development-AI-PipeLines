**Idiomas / Languages:** 🇧🇷 [Português](README.pt-br.md) | 🇺🇸 [English](README.md)

---

# Rastreador de SaaS no Trustpilot & Motor de Inteligência de Concorrência

Um pipeline leve em Python projetado para monitorar a saúde das avaliações de plataformas SaaS no Trustpilot, extrair o sentimento do cliente, identificar tendências de avaliações negativas e gerar leads para prospecção personalizada com base nos riscos de churn (cancelamento) dos concorrentes.

## 🔗 Funcionalidades

* **Raspagem de Avaliações:** Extrai títulos, classificações por estrelas, texto da avaliação, datas/horas e localização dos avaliadores.
* **Análise de Sentimento:** Integra-se com as APIs da Groq/OpenAI para classificar pontos de dor (ex: problemas de suporte ao cliente, mudanças de preços, bugs técnicos).
* **Prospecção de Alvos:** Destaca usuários corporativos insatisfeitos que estão abandonando concorrentes, permitindo uma prospecção direcionada.
* **Exportação de Dados:** Salva relatórios estruturados em formatos JSON e CSV de forma automática.

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3.10+
* **Bibliotecas:** `requests`, `beautifulsoup4`, `pandas`, `openai`
* **API:** Groq API / OpenAI API

## 🚀 Início Rápido

```bash
# Clone o repositório
git clone [https://github.com/SEU_USUARIO/trustpilot-saas-tracker.git](https://github.com/SEU_USUARIO/trustpilot-saas-tracker.git)
cd trustpilot-saas-tracker

# Instale as dependências
pip install requests beautifulsoup4 pandas openai

# Execute o rastreador
python main.py --company "hubspot" --pages 5

