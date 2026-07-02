import pandas as pd
from upsetplot import from_contents, UpSet
import matplotlib.pyplot as plt

# Read SSR data

df = pd.read_csv(
"/home/jnlab5/ishika/crossroads_data_nipah/crossroad_out_final/job_1780482811529_809/output/main/ssr_genecombo.tsv",
sep="\t"
)

print("Total SSR records:", len(df))
print("Total unique motifs:", df["motif"].nunique())

# Keep top 100 motifs

top100 = df["motif"].value_counts().head(100).index
df = df[df["motif"].isin(top100)]

print("SSR records retained:", len(df))
print("Motifs retained:", df["motif"].nunique())

# Create gene -> motif sets

gene_sets = {
gene: set(group["motif"])
for gene, group in df.groupby("gene")
}

# Convert to UpSet format

upset_data = from_contents(gene_sets)

# Plot

upset = UpSet(
upset_data,
subset_size="count",
sort_by="cardinality",
show_counts=True    # <-- Counts automatically shown on bars
)

upset.plot()

plt.savefig(
"gene_motif_upset_top100_labeled.png",
dpi=300,
bbox_inches="tight"
)

plt.close()

print("Done! Saved as gene_motif_upset_top100_labeled.png")
