def generate_rule_plan(metadata: dict) -> dict:
    plan = {
        "visualizations": [],
        "statistics": [],
        "notes": []
    }

    num = metadata["numeric_cols"]
    cat = metadata["categorical_cols"]

    if len(num) == 1:
        plan["visualizations"].append(
            {"type": "distribution", "column": num[0]}
        )
        plan["notes"].append("Single numeric column detected")

    if len(num) >= 1 and len(cat) >= 1:
        plan["visualizations"].append(
            {"type": "violin", "x": cat[0], "y": num[0]}
        )

    if len(num) >= 2:
        plan["visualizations"].append(
            {"type": "scatter", "x": num[0], "y": num[1]}
        )
        plan["statistics"].append("correlation")

    return plan
