import os
import json
import requests
import pandas as pd

def get_groq_api_key():
    """Reads API key securely from Android Documents directory."""
    key_path = "/storage/emulated/0/Documents/groq_key.txt"
    if os.path.exists(key_path):
        with open(key_path, "r") as f:
            return f.read().strip()
    return os.environ.get("GROQ_API_KEY", "")

GROQ_API_KEY = get_groq_api_key()
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_ai_briefing(df_json):
    system_prompt = (
        "You are a Senior E-Commerce Pricing Strategist. Analyze the provided competitor product data "
        "and generate a concise executive summary covering: 1. Price disparity highlights, "
        "2. Strategic positioning risks, 3. Specific pricing adjustment recommendations."
    )
    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Competitor Product Catalog Data:\n{df_json}"}
        ],
        "temperature": 0.2
    }
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    res = requests.post(GROQ_URL, headers=headers, json=payload)
    return res.json()['choices'][0]['message']['content'] if res.status_code == 200 else f"Error: {res.text}"

def run_pipeline():
    products = [
        {"sku": "NK-01", "name": "Pro Running Shoes", "competitor_a_price": 120.00, "our_price": 135.00, "stock_status": "In Stock"},
        {"sku": "NK-02", "name": "Ultra Lightweight Hoodie", "competitor_a_price": 65.00, "our_price": 60.00, "stock_status": "Low Stock"},
        {"sku": "NK-03", "name": "Compression Shorts", "competitor_a_price": 35.00, "our_price": 42.00, "stock_status": "Out of Stock"}
    ]
    df = pd.DataFrame(products)
    df['price_difference'] = df['our_price'] - df['competitor_a_price']
    
    folder = "/storage/emulated/0/Documents/ecommerce_competitor_intelligence"
    df.to_csv(f"{folder}/ecommerce_report.csv", index=False)
    df.to_excel(f"{folder}/ecommerce_report.xlsx", index=False)
    
    summary = generate_ai_briefing(df.to_json(orient="records"))
    with open(f"{folder}/ecommerce_summary.txt", "w") as f:
        f.write(summary)
    
    print("=== E-COMMERCE PIPELINE EXECUTED SUCCESSFULLY ===")

if __name__ == "__main__":
    run_pipeline()
