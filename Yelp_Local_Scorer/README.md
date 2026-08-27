# Yelp Local Scorer & Automated Pitch Generator

An automated lead-scoring framework that analyzes local business listings on Yelp, detects weak online optimization signals (e.g., unclaimed profiles, low review counts, missing website links), and generates personalized AI outreach hooks for agency cold outreach.

## Features

* **Opportunity Scoring:** Calculates a custom lead score based on profile completeness, rating strength, and claim status.
* **LLM Pitch Generation:** Integrates with Groq/LLMs to generate customized cold outreach hooks targeting business owners.
* **Automated Lead Management:** Exports lead evaluation data to structured files and organizes target subfolders automatically.

## Tech Stack

* **Language:** Python 3.10+
* **Libraries:** `requests`, `beautifulsoup4`, `lxml`, `pandas`, `openai`
* **API:** Groq API (`openai/gpt-oss-120b`)

## Installation & Usage

```bash
# Clone repository
git clone [https://github.com/rezende-data/Python-Development-AI-PipeLines.git](https://github.com/rezende-data/Python-Development-AI-PipeLines.git)
cd Python-Development-AI-PipeLines/Yelp_Local_Scorer

# Install requirements
pip install requests beautifulsoup4 pandas openai

# Execute scoring pipeline
python main.py

