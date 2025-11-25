def detect_high_cpc(df, threshold=50):
    high_cpc = df[df["cpc"] > threshold]
    return high_cpc

def detect_low_roas(df, threshold=1):
    low_roas = df[df["roas"] < threshold]
    return low_roas

def summarize_metrics(df):
    summary = {
        "avg_cpc": df["cpc"].mean(),
        "avg_cpm": df["cpm"].mean(),
        "avg_ctr": df["ctr"].mean(),
        "avg_roas": df["roas"].mean()
    }
    return summary