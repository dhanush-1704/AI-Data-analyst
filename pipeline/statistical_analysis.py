from scipy import stats

def run_correlation(df, x, y):
    corr, p = stats.pearsonr(df[x], df[y])
    print(f"Correlation between {x} and {y}: {corr:.2f}, p={p:.4f}")
