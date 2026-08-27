# Python Web Scraping & AI Automation Pipelines

Production-ready Python infrastructure built for automated web extraction, ETL data transformation (Pandas), and high-speed LLM enrichment via Groq & OpenAI APIs (`openai/gpt-oss-120b`).

---

## 🚀 Executive Summary

This repository serves as a centralized portfolio hub for enterprise-grade, end-to-end data pipelines designed for commercial deployment. Every project features secure dynamic API key loading, anti-bot handling, and multi-format reporting (`.csv`, `.xlsx`, `.txt`).

---

## 📦 Featured Automation Projects

* **B2B Lead Enrichment & AI Scoring** (`/B2B_Lead_Enrichment`)  
  * **Strategy:** Turns raw prospect lists into high-converting sales pipelines. Parses firmographics, assigns ideal customer profile (ICP) scores (1–100), and auto-generates custom cold outreach hooks via Groq.

* **E-Commerce Competitor Intelligence** (`/Ecommerce_Competitor_Intelligence`)  
  * **Strategy:** Delivers automated pricing intelligence for brand managers. Tracks competitor SKUs in real time, flags margin gaps or inventory stockouts, and outputs LLM-driven repricing recommendations.

* **Real Estate Deal Aggregator** (`/Real_Estate_Deal_Aggregator`)  
  * **Strategy:** Accelerates investment underwriting. Extracts multi-market property listings, calculates key yield metrics (Net Operating Income and Cap Rates), and compiles automated acquisition memos.

* **Trustpilot SaaS Tracker** (`/Trustpilot_SaaS_Tracker`)  
  * **Strategy:** Exploits competitor churn. Scrapes SaaS product review feeds, isolates negative 1–2 star customer feedback with LLM sentiment analysis, and yields qualified replacement prospects.

* **YellowPages Lead Gen Engine** (`/YellowPages_Lead_Gen`)  
  * **Strategy:** High-speed regional B2B prospecting. Extracts commercial listings across target zip codes and niches, handles missing fields, deduplicates records, and exports client-ready CSV datasets.

* **Yelp Local Scorer & Pitch Generator** (`/Yelp_Local_Scorer`)  
  * **Strategy:** Identifies low-hanging agency targets. Scrapes local service providers, scores their profile completeness and rating gaps, and drafts tailored 2-sentence pitch hooks for instant cold outreach.

---

## 🛠️ Core Technical Stack

* **Languages & Core ETL:** Python 3.x, Pandas, OpenPyXL, BeautifulSoup4, Requests
* **AI Orchestration:** Groq REST API (`openai/gpt-oss-120b`), OpenAI API
* **Security Architecture:** Dynamic key ingestion via local `groq_key.txt` / Environment Variables (Zero Hardcoded Credentials)
* **Output Persistency:** CSV, XLSX, JSON, Formatted Text Briefings

---

*Engineered by Rezende — Data Engineering & Automation Specialist.*
