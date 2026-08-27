# Trustpilot SaaS Tracker & Competitor Intelligence Engine

A lightweight Python pipeline designed to monitor SaaS review health on Trustpilot, extract customer sentiment, identify negative review trends, and generate custom outreach leads based on competitor churn risks.

## Features

* **Review Scraping:** Extracts titles, star ratings, review text, timestamps, and reviewer locations.
* **Sentiment Analysis:** Integrates with Groq/OpenAI APIs to classify pain points (e.g., customer support issues, pricing changes, technical bugs).
* **Target Prospecting:** Highlights dissatisfied business users switching from competitors for targeted outreach.
* **Data Export:** Saves structured JSON and CSV reports automatically.

## Tech Stack

* **Language:** Python 3.10+
* **Libraries:** `requests`, `beautifulsoup4`, `pandas`, `openai`
* **API:** Groq API / OpenAI API

## Quickstart

```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/trustpilot-saas-tracker.git](https://github.com/YOUR_USERNAME/trustpilot-saas-tracker.git)
cd trustpilot-saas-tracker

# Install dependencies
pip install requests beautifulsoup4 pandas openai

# Run the tracker
python main.py --company "hubspot" --pages 5
