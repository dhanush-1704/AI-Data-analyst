import pandas as pd

def main():
    df = pd.read_csv("data/cleaned_dataset.csv")

    assert not df.empty, "Dataset is empty"
    assert df.isna().sum().sum() == 0, "Missing values detected"

    print("✅ Data quality checks passed")


if __name__ == "__main__":
    main()
