import json
from pathlib import Path

# Absolute paths for inputs/outputs
INSIGHTS_PATH = Path("C:/Users/lenovo/AgenticFacebookPerformanceAnalyst/outputs/final/insights.json")
CREATIVES_PATH = Path("C:/Users/lenovo/AgenticFacebookPerformanceAnalyst/outputs/final/creatives.json")
OUTPUT_PATH = Path("C:/Users/lenovo/AgenticFacebookPerformanceAnalyst/outputs/final/report.md")

def generate_report(insights: str, creatives: dict):
    """Offline report generator — combines insights + creatives."""
    report = []

    report.append("# 📊 Facebook Ads Performance Report\n")
    report.append("## 📌 Executive Summary\n")
    report.append("This report summarizes key insights, performance trends, and creative recommendations extracted from the synthetic Facebook ads dataset.\n")

    report.append("## 📈 Insights Summary\n")
    report.append(insights + "\n\n")

    report.append("## 🎨 Creative Recommendations\n")
    report.append("Here are the recommended creative strategies and assets:\n\n")

    report.append("### Ad Copies\n")
    for copy in creatives.get("ad_copies", []):
        report.append(f"- {copy}\n")

    report.append("\n### Image Ideas\n")
    for img in creatives.get("image_ideas", []):
        report.append(f"- {img}\n")

    report.append("\n### Video Hooks\n")
    for hook in creatives.get("video_hooks", []):
        report.append(f"- {hook}\n")

    report.append("\n## 🧩 Conclusion\n")
    report.append(
        "This report provides a high-level view of campaign performance and strategic creative suggestions. "
        "Use these insights to optimize budgets, refine audiences, and build higher-performing ad variations.\n"
    )

    return "".join(report)

def main():
    # Load insights
    if not INSIGHTS_PATH.exists():
        print("❌ insights.json not found!")
        return
    with open(INSIGHTS_PATH, "r") as f:
        insights_data = json.load(f)
        insights = insights_data.get("insights", "")

    # Load creatives
    if not CREATIVES_PATH.exists():
        print("❌ creatives.json not found!")
        return
    with open(CREATIVES_PATH, "r") as f:
        creatives = json.load(f)

    # Generate markdown report
    md_report = generate_report(insights, creatives)

    # Ensure folder exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Save report
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(md_report)

    print(f"✅ report.md generated at: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()