
### 2. YellowPages Lead Gen

```markdown
# YellowPages B2B Lead Generation Engine

An automated B2B scraper tailored for local market research and cold lead prospecting. It extracts targeted contact info (business name, phone, website, address, rating) by niche and geography.

## Features

* **Targeted Search Routing:** Query specific industries across any country, state, or city zip code.
* **Smart Data Extraction:** Cleanly parses business metadata while handling missing fields gracefully.
* **Duplication Guard:** Automatically deduplicates records across search pages.
* **Client-Ready Deliverables:** Generates structured `.csv` files organized by client, location, or niche.

## Tech Stack

* **Language:** Python 3.10+
* **Libraries:** `requests`, `beautifulsoup4`, `lxml`

## Installation & Usage

```bash
# Clone repository
git clone [https://github.com/YOUR_USERNAME/yellowpages-lead-gen.git](https://github.com/YOUR_USERNAME/yellowpages-lead-gen.git)
cd yellowpages-lead-gen

# Install requirements
pip install requests beautifulsoup4 lxml

# Execute scraping pipeline
python scraper.py --keyword "Roofing Contractors" --location "Austin, TX" --results 100
