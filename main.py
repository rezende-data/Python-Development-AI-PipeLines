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

def generate_investment_memo(deals_json):
    prompt = (
        "You are an Institutional Real Estate Analyst. Review these property listings:\n"
        f"{deals_json}\n\n"
        "Identify the top deal with the highest Cap Rate and write a 3-bullet investment memo on why it stands out."
    )
    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    res = requests.post(GROQ_URL, headers=headers, json=payload)
    return res.json()['choices'][0]['message']['content'] if res.status_code == 200 else f"Error: {res.text}"

def run_pipeline():
    properties = [
        {"id": "PROP-101", "city": "Austin, TX", "list_price": 450000, "est_monthly_rent": 3200, "annual_taxes": 8000},
        {"id": "PROP-102", "city": "Tampa, FL", "list_price": 280000, "est_monthly_rent": 2400, "annual_taxes": 4200}
    ]
    df = pd.DataFrame(properties)
    df['gross_annual_rent'] = df['est_monthly_rent'] * 12
    df['est_net_operating_income'] = df['gross_annual_rent'] - df['annual_taxes'] - (df['gross_annual_rent'] * 0.10)
    df['cap_rate_pct'] = ((df['est_net_operating_income'] / df['list_price']) * 100).round(2)
    
    folder = "/storage/emulated/0/Documents/real_estate_deal_aggregator"
    df.to_csv(f"{folder}/real_estate_report.csv", index=False)
    df.to_excel(f"{folder}/real_estate_report.xlsx", index=False)
    
    memo = generate_investment_memo(df.to_json(orient="records"))
    with open(f"{folder}/real_estate_summary.txt", "w") as f:
        f.write(memo)
        
    print("=== REAL ESTATE PIPELINE EXECUTED SUCCESSFULLY ===")

if __name__ == "__main__":
    run_pipeline()
