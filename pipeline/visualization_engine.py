import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid")

OUTPUT_DIR = "reports/visuals"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# =========================
# Low-level plot functions
# =========================

def plot_distribution(df, col):
    plt.figure()
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/distribution_{col}.png")
    plt.close()


def plot_violin(df, x, y):
    plt.figure()
    sns.violinplot(x=df[x], y=df[y])
    plt.title(f"{y} by {x}")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/violin_{y}_by_{x}.png")
    plt.close()


def plot_scatter(df, x, y):
    plt.figure()
    sns.scatterplot(x=df[x], y=df[y])
    plt.title(f"{x} vs {y}")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/scatter_{x}_vs_{y}.png")
    plt.close()


def plot_bar(df, col):
    plt.figure()
    df[col].value_counts().plot(kind="bar")
    plt.title(f"Counts of {col}")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/bar_{col}.png")
    plt.close()


# =========================
# AI-driven dispatcher
# =========================

def run_visualizations(df, viz_plan: list):
    """
    Executes visualization instructions decided by the LLM.
    """

    for viz in viz_plan:
        kind = viz.get("type")

        try:
            if kind == "distribution":
                plot_distribution(df, viz["column"])

            elif kind == "bar":
                plot_bar(df, viz["column"])

            elif kind == "violin":
                plot_violin(df, viz["x"], viz["y"])

            elif kind == "scatter":
                plot_scatter(df, viz["x"], viz["y"])

        except Exception as e:
            print(f"⚠️ Skipping visualization {viz}: {e}")
