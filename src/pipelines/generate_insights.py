import pandas as pd
import json
from pathlib import Path

# Absolute safe paths
DATA_PATH = Path("C:/Users/lenovo/AgenticFacebookPerformanceAnalyst/data/synthetic_fb_ads_undergarments.csv")
OUTPUT_PATH = Path("C:/Users/lenovo/AgenticFacebookPerformanceAnalyst/outputs/final/insights.json")

# -----------------------------
# MOCK LLM FUNCTION (Offline)
# -----------------------------
def fake_llm_generate_insights(summary_text: str):
    insights = []
    insights.append("Spend, impressions, clicks, purchases, and revenue were analyzed.")
    insights.append("Higher ROAS campaigns should be prioritized in scaling decisions.")
    insights.append("Campaigns with below-average CTR should be retested with new creatives.")
    insights.append("Audience segments with above-average purchases indicate strong intent.")
    insights.append("Creative messages with high CTR but low ROAS require funnel optimization.")
    return "\n".join(insights)

def load_data(path=DATA_PATH):
    return pd.read_csv(path)

def generate_insights():
    df = load_data()
    description = df.describe(include="all").to_string()

    insights_text = fake_llm_generate_insights(description)

    # Ensure parent folder exists (avoid FileNotFoundError)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_PATH, "w") as f:
        json.dump({"insights": insights_text}, f, indent=4)

    print(f"insights.json created successfully at: {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_insights()