# YellowPages B2B Lead Generation Engine

An automated B2B scraper tailored for local market research and cold lead prospecting. It extracts targeted contact info (business name, phone, website, address, rating) by niche and geography.

## Features

* **Targeted Search Routing:** Query specific industries across any country, state, or city zip code.
* **Smart Data Extraction:** Cleanly parses business metadata while handling missing fields gracefully.
* **Duplication Guard:** Automatically deduplicates records across search pages.
* **Client-Ready Deliverables:** Generates structured `.csv` and `.xlsx` files organized by client, location, or niche.

## Tech Stack

* **Language:** Python 3.10+
* **Libraries:** `requests`, `beautifulsoup4`, `lxml`, `pandas`, `openpyxl`

## Installation & Usage

```bash
# Clone repository
git clone [https://github.com/rezende-data/Python-Development-AI-PipeLines.git](https://github.com/rezende-data/Python-Development-AI-PipeLines.git)
cd Python-Development-AI-PipeLines/YellowPages_Lead_Gen

# Install requirements
pip install requests beautifulsoup4 lxml pandas openpyxl

# Execute scraping pipeline
python main.py
