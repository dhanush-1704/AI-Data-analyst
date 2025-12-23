import pandas as pd
from ydata_profiling import ProfileReport

def main():
    df = pd.read_csv("data/cleaned_dataset.csv")

    profile = ProfileReport(df, explorative=True)
    profile.to_file("reports/eda_profile.html")

    print("✅ EDA report generated")


if __name__ == "__main__":
    main()
