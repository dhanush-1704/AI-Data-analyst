import pandas as pd

def extract_metadata(df: pd.DataFrame) -> dict:
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "numeric_cols": df.select_dtypes(include=["int64", "float64"]).columns.tolist(),
        "categorical_cols": df.select_dtypes(include=["object"]).columns.tolist(),
        "missing_pct": (df.isna().mean() * 100).round(2).to_dict(),
        "unique_counts": df.nunique().to_dict()
    }
