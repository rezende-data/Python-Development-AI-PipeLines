**Idiomas / Languages:** 🇧🇷 [Português](README.pt-br.md) | 🇺🇸 [English](README.md)

# Motor de Enriquecimento de Leads B2B & Scoring com IA

Um sistema de ponta a ponta para processamento de leads B2B, projetado para enriquecer dados brutos de prospecção, avaliar o alinhamento com o Perfil de Cliente Ideal (ICP) e gerar automaticamente ganchos de abordagem fria (cold outreach) de alta conversão utilizando raciocínio estruturado de LLMs.

## 🚀 Valor de Negócio

* **Scoring Automatizado de Leads:** Atribui uma pontuação de adequação ao ICP de 1 a 100 com base no setor e posicionamento da empresa.
* **Prospecção Personalizada:** Utiliza `openai/gpt-oss-120b` para produzir primeiras linhas totalmente adaptadas para campanhas de e-mail.
* **Dados Estruturados:** Exporta dados validados em schemas estritos de JSON diretamente para formatos CSV/XLSX, prontos para bancos de dados relacionais.

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3.x
* **Pipelines de Dados:** Pandas, JSON
* **Orquestração de LLM:** Groq API com Formatação de Resposta Estruturada em JSON
* **Exportações:** CSV, Excel, Resumo em Texto Puro

## 📊 Lógica do Pipeline

1. **Processamento Bruto de Leads:** Importa sinais firmográficos e descrições das empresas.
2. **Enriquecimento via LLM:** Envia o contexto do lead para a API da Groq aplicando validação forçada de schema JSON.
3. **Transformação de Dados:** Desempacota os atributos do JSON em DataFrames do Pandas.
4. **Persistência Multiformato:** Grava os resultados estruturados nos respectivos formatos de armazenamento.

## 📁 Entregáveis Gerados

* `b2b_leads_report.csv`: Conjunto de dados enriquecido completo, contendo as pontuações de ICP e os ganchos gerados.
* `b2b_leads_report.xlsx`: Planilha estruturada de leads pronta para a equipe de vendas.
* `b2b_leads_summary.txt`: Detalhamento dos ganchos de pitch para revisão rápida.

*Mantido por Rezende – Especialista em Engenharia de Dados & Automação.*

