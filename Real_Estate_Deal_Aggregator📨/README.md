# Real Estate Yield Analyzer & Deal Aggregator

A programmatic property evaluation framework that processes real estate listings, calculates key financial performance metrics (Gross Yield, Net Operating Income, Cap Rates), and compiles AI-driven institutional investment memos.

## 🚀 Business Value
* **Automated Underwriting:** Computes Net Operating Income (NOI) and Cap Rates across raw listings.
* **Deal Filtering:** Surface high-yield property targets while accounting for tax and maintenance overhead.
* **Investment Memos:** Generates 3-bullet executive memos via `openai/gpt-oss-120b` for target properties.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Financial Calculations:** Pandas Vectorized Arithmetic
* **AI Reasoning:** Groq API (`openai/gpt-oss-120b`)
* **Reporting:** CSV, Excel (`.xlsx`), Text Memo (`.txt`)

## 📐 Key Financial Formulas Implemented
$$\text{Gross Annual Rent} = \text{Monthly Rent} \times 12$$

$$\text{Net Operating Income (NOI)} = \text{Gross Annual Rent} - \text{Taxes} - \text{Maintenance (10\%)}$$

$$\text{Cap Rate (\%)} = \left( \frac{\text{NOI}}{\text{List Price}} \right) \times 100$$

## 📂 Deliverables Generated
* `real_estate_report.csv`: Calculated financial metrics for all target listings.
* `real_estate_report.xlsx`: Formatted deal matrix for real estate investors.
* `real_estate_summary.txt`: AI-generated institutional investment memo highlighting top Cap Rate deals.

---
*Maintained by Rezende — Data Engineering & Automation Specialist.*
