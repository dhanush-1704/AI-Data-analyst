import pandas as pd
import csv

def load_csv_safely(path: str) -> pd.DataFrame:
    """
    Robust CSV loader that works with most real-world CSV files.
    """

    # Try automatic delimiter detection
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        sample = f.read(4096)
        dialect = csv.Sniffer().sniff(sample)
        delimiter = dialect.delimiter

    # Load CSV safely
    df = pd.read_csv(
        path,
        delimiter=delimiter,
        comment="#",
        engine="python"
    )

    # Basic structural validation
    if df.empty:
        raise ValueError("Loaded dataset is empty")

    if df.shape[1] < 2:
        raise ValueError("Dataset must have at least 2 columns")

    # Normalize column names
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df
