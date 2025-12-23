import numpy as np
from utils.data_loader import load_csv_safely

def main():
    df = load_csv_safely("data/dataset.csv")

    print(df.info())

    df = df.drop_duplicates()

    for col in df.columns:
        if df[col].dtype.kind in "if":
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna("unknown")

    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    if len(num_cols) > 0:
        df[f"log_{num_cols[0]}"] = np.log1p(df[num_cols[0]])

    df.to_csv("data/cleaned_dataset.csv", index=False)

    print("✅ Cleaned dataset saved")


if __name__ == "__main__":
    main()
