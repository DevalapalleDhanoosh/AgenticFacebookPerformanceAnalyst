import json
from pathlib import Path

# Absolute path for inputs and outputs
INSIGHTS_PATH = Path("C:/Users/lenovo/AgenticFacebookPerformanceAnalyst/outputs/final/insights.json")
OUTPUT_PATH = Path("C:/Users/lenovo/AgenticFacebookPerformanceAnalyst/outputs/final/creatives.json")

# -----------------------------
# MOCK LLM CREATIVE GENERATOR
# -----------------------------
def fake_llm_generate_creatives(insights: str):
    """
    Offline creative generator — converts insights into
    creative recommendations without any API key.
    """
    return {
        "creative_strategy": "Based on dataset-level insights, generate ad copies, images, and video hooks.",
        "ad_copies": [
            "Experience all-day comfort. Premium undergarments built for daily wear.",
            "Soft. Breathable. Comfortable. The only undergarment you'll ever want.",
            "Feel the difference — moisture-wicking fabric with perfect stretch.",
        ],
        "image_ideas": [
            "Close-up fabric texture with soft lighting",
            "Lifestyle shot of model wearing the undergarment in morning routine",
            "Flat-lay of the product with pastel background for a clean premium feel",
        ],
        "video_hooks": [
            "3-second comfort test: Pull, stretch, and bounce demonstration.",
            "‘I switched to this and never looked back’ — UGC testimonial.",
            "Behind-the-scenes stitching and material selection preview.",
        ],
        "based_on_insights": insights[:500]  # limit length
    }

def main():
    # Load insights from file
    insights = ""
    if INSIGHTS_PATH.exists():
        with open(INSIGHTS_PATH, "r") as f:
            insights = json.load(f).get("insights", "")
    else:
        print("Insights file not found!")
        return

    # Generate creatives using offline model
    creatives = fake_llm_generate_creatives(insights)

    # Ensure folder exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Save creatives.json
    with open(OUTPUT_PATH, "w") as f:
        json.dump(creatives, f, indent=4)

    print(f"creatives.json generated at: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
