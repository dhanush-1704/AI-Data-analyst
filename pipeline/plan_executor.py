from pipeline import visualization_engine as viz
from pipeline import statistical_analysis as stats

def execute_plan(df, plan):
    for v in plan.get("visualizations", []):
        if v["type"] == "distribution":
            viz.plot_distribution(df, v["column"])
        elif v["type"] == "violin":
            viz.plot_violin(df, v["x"], v["y"])
        elif v["type"] == "scatter":
            viz.plot_scatter(df, v["x"], v["y"])

    for s in plan.get("statistics", []):
        if s == "correlation":
            cols = df.select_dtypes(include=["int64", "float64"]).columns
            if len(cols) >= 2:
                stats.run_correlation(df, cols[0], cols[1])
