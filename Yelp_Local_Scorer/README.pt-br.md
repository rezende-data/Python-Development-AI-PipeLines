**Idiomas / Languages:** 🇧🇷 [Português](README.pt-br.md) | 🇺🇸 [English](README.md)

---

# Pontuador Local do Yelp & Gerador Automatizado de Pitches

Um framework automatizado de pontuação de leads que analisa cadastros de empresas locais no Yelp, detecta sinais fracos de otimização online (ex: perfis não reivindicados, baixo volume de avaliações, links de sites ausentes) e gera ganchos de abordagem personalizados por IA para prospecção fria de agências.

## 🔗 Funcionalidades

* **Pontuação de Oportunidades:** Calcula uma pontuação personalizada de lead com base no preenchimento do perfil, força das avaliações e status de reivindicação do perfil.
* **Geração de Pitches via LLM:** Integra-se com a Groq/LLMs para gerar ganchos de abordagem fria personalizados direcionados aos donos dos estabelecimentos.
* **Gestão Automatizada de Leads:** Exporta dados de avaliação de leads para arquivos estruturados e organiza subpastas de destino de forma automática.

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3.10+
* **Bibliotecas:** `requests`, `beautifulsoup4`, `lxml`, `pandas`, `openai`
* **API:** Groq API (`openai/gpt-oss-120b`)

## ⚙️ Instalação & Uso

```bash
# Clone o repositório
git clone [https://github.com/rezende-data/Python-Development-AI-PipeLines.git](https://github.com/rezende-data/Python-Development-AI-PipeLines.git)
cd Python-Development-AI-PipeLines/Yelp_Local_Scorer

# Instale os requisitos
pip install requests beautifulsoup4 pandas openai

# Execute o pipeline de pontuação
python main.py

