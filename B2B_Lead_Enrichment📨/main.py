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

def enrich_lead(company, raw_info):
    prompt = f"""
    Analyze this B2B Lead:
    Company Name: {company}
    Raw Description: {raw_info}
    
    Return JSON ONLY with exact keys:
    1. "industry": (Short string)
    2. "icp_score": (Integer 1-100 based on SaaS fit)
    3. "personalized_pitch_hook": (One high-converting cold email opening line)
    """
    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "response_format": {"type": "json_object"}
    }
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    try:
        res = requests.post(GROQ_URL, headers=headers, json=payload)
        return json.loads(res.json()['choices'][0]['message']['content'])
    except Exception as e:
        return {"industry": "Unknown", "icp_score": 0, "personalized_pitch_hook": str(e)}

def run_pipeline():
    leads = [
        {"company": "Apex Logistics", "raw_info": "Mid-market 3PL provider specializing in cold chain storage across Western Europe."},
        {"company": "FinTech Flow", "raw_info": "Early stage startup offering API integrations for instant bank payments."}
    ]
    results = [{**lead, **enrich_lead(lead['company'], lead['raw_info'])} for lead in leads]
    df = pd.DataFrame(results)
    
    folder = "/storage/emulated/0/Documents/b2b_lead_enrichment"
    df.to_csv(f"{folder}/b2b_leads_report.csv", index=False)
    df.to_excel(f"{folder}/b2b_leads_report.xlsx", index=False)
    
    summary_txt = "\n".join([f"Company: {r['company']}\nScore: {r['icp_score']}\nHook: {r['personalized_pitch_hook']}\n" for r in results])
    with open(f"{folder}/b2b_leads_summary.txt", "w") as f:
        f.write(summary_txt)
        
    print("=== B2B LEAD PIPELINE EXECUTED SUCCESSFULLY ===")

if __name__ == "__main__":
    run_pipeline()
