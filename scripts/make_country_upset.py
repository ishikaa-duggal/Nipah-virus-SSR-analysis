import pandas as pd
import matplotlib.pyplot as plt

from upsetplot import UpSet
from upsetplot import from_indicators

# -----------------------
# Load data
# -----------------------

df = pd.read_csv(
    "crossroad_unfair1000/job_1781073771422_537/output/main/mergedOut.tsv",
    sep="\t"
)

# SSR midpoint
df["mid"] = (
    (df["start"] + df["stop"]) / 2
).astype(int)

# Countries to compare
countries = [
    "Bangladesh",
    "India",
    "Malaysia"
]

df = df[
    df["category"].isin(countries)
]

# -----------------------
# Build loci table
# -----------------------

loci = sorted(
    df["mid"].unique()
)

table = pd.DataFrame(
    index=loci
)

for country in countries:

    sites = set(
        df[
            df["category"] == country
        ]["mid"]
    )

    table[country] = [
        locus in sites
        for locus in loci
    ]

# -----------------------
# UpSet
# -----------------------

upset_data = from_indicators(
    countries,
    table
)

plt.figure(figsize=(10,6))

up = UpSet(
    upset_data,
    subset_size='count',
    show_counts=True,
    sort_by='cardinality'
)

up.plot()

plt.suptitle(
    "Shared SSR Loci Across Nipah Virus Populations",
    fontsize=14,
    fontweight='bold'
)

plt.savefig(
    "country_upset_plot.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    "country_upset_plot.svg",
    bbox_inches="tight"
)

plt.close()

print("Saved:")
print("country_upset_plot.png")
print("country_upset_plot.svg")
