# B2B Lead Enrichment & AI Lead Scoring Engine

An end-to-end B2B lead processing system designed to enrich raw prospect data, evaluate Ideal Customer Profile (ICP) alignment, and generate high-converting cold outreach hooks automatically using structured LLM reasoning.

## 🚀 Business Value
* **Automated Lead Scoring:** Assigns a 1–100 ICP fit score based on business sector and positioning.
* **Personalized Outreach:** Uses `openai/gpt-oss-120b` to produce tailored first-lines for email campaigns.
* **Structured Data:** Outputs strict JSON-validated schema directly into relational-ready CSV/XLSX formats.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Data Pipelines:** Pandas, JSON
* **LLM Orchestration:** Groq API with Structured JSON Response Formatting
* **Exports:** CSV, Excel, Plain Text Summary

## 📊 Pipeline Logic
1. **Raw Lead Parsing:** Imports firmographic signals and descriptions.
2. **LLM Enrichment:** Passes lead context to Groq API using JSON schema enforcement.
3. **Data Transformation:** Unpacks JSON attributes into Pandas DataFrames.
4. **Multi-Format Persistence:** Writes structured results to data stores.

## 📂 Deliverables Generated
* `b2b_leads_report.csv`: Complete enriched dataset featuring ICP scores and hooks.
* `b2b_leads_report.xlsx`: Structured lead sheet for sales teams.
* `b2b_leads_summary.txt`: Pitch hook breakdown for rapid review.

---
*Maintained by Rezende — Data Engineering & Automation Specialist.*
