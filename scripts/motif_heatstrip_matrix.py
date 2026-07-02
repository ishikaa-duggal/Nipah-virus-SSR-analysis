import pandas as pd
import numpy as np

df = pd.read_csv(
    "motif_unique_positions.tsv",
    sep="\t"
)

motifs = [
    "ATT",
    "TAA",
    "GAT",
    "TTTC",
    "CTA",
    "ATG",
    "AAG",
    "CAG",
    "TCA",
    "GTA"
]

genome_length = 18246

# 50 bins across genome
bins = np.linspace(
    0,
    genome_length,
    51
)

matrix = []

for motif in motifs:

    subset = df[df["motif"] == motif]

    counts, _ = np.histogram(
        subset["mid"],
        bins=bins
    )

    matrix.append(counts)

heatmap = pd.DataFrame(
    matrix,
    index=motifs
)

heatmap.to_csv(
    "motif_heatstrip_matrix.tsv",
    sep="\t"
)

print(heatmap.shape)
print(heatmap.head())
print("\nSaved motif_heatstrip_matrix.tsv")
