import json

class FacebookPerformanceAgent:
    def __init__(self, system_prompt_path):
        with open(system_prompt_path, "r") as f:
            self.prompt = json.load(f)

    def identify_issues(self, analysis_results):
        issues = []

        if analysis_results.get("avg_roas", 0) < 1:
            issues.append("Overall ROAS is low → campaigns may be unprofitable.")

        if analysis_results.get("avg_cpc", 0) > 50:
            issues.append("Average CPC is too high → targeting inefficiency.")

        return issues

    def generate_insights(self, df):
        insights = []
        if df["ctr"].mean() < 0.5:
            insights.append("CTR is low → creatives may need improvement.")
        if df["cpm"].mean() > 200:
            insights.append("CPM is high → competition or poor audience match.")
        return insights

    def structured_output(self, issues, insights):
        return {
            "issues": issues,
            "insights": insights,
            "recommendations": [
                "Improve targeting refinement",
                "A/B test creative",
                "Allocate budget to best-performing ad sets"
            ]
        }