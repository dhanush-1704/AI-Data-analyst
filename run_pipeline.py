import pandas as pd

# =========================
# Phase A: Deterministic pipeline
# =========================
from pipeline import (
    _01_data_loading_cleaning as clean_step,
    _02_data_quality_validation as quality_step,
    _03_exploratory_data_analysis as eda_step,
)

# =========================
# Phase B: Intelligence layer
# =========================
from pipeline.metadata_extractor import extract_metadata
from pipeline.rule_planner import generate_rule_plan
from pipeline.analyst_mind import AnalystMind

# =========================
# Phase C: Execution layer
# =========================
from pipeline.plan_executor import execute_plan


def main():
    # -------- Phase A --------
    print("▶ Running data loading & cleaning")
    clean_step.main()

    print("▶ Running data quality validation")
    quality_step.main()

    print("▶ Running EDA snapshot")
    eda_step.main()

    # Load cleaned data
    df = pd.read_csv("data/cleaned_dataset.csv")

    # -------- Phase B --------
    print("🧠 AI analyst is reasoning (LLM via Ollama)...")

    metadata = extract_metadata(df)
    baseline_plan = generate_rule_plan(metadata)

    mind = AnalystMind(metadata, baseline_plan)
    final_plan = mind.think_and_decide()

    # -------- Phase C --------
    print("▶ Executing AI-decided analysis plan")
    execute_plan(df, final_plan)

    # -------- AI Speaks --------
    mind.write_report()
    print("🧠 AI analyst report written to reports/ai_insights.md")


if __name__ == "__main__":
    main()
