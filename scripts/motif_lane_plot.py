import pandas as pd

df = pd.read_csv(
    "crossroad_unfair1000/job_1781073771422_537/output/main/mergedOut.tsv",
    sep="\t"
)

top_motifs = [
    "ATT","GAT","CTA","ATG","TTTC",
    "TAA","AAG","CAG","TCA","GTA"
]

df = df[df["motif"].isin(top_motifs)].copy()

df["mid"] = (df["start"] + df["stop"]) / 2

df.to_csv("top_motif_positions.tsv", sep="\t", index=False)

print(df.shape)
print(df.head())
print("Saved top_motif_positions.tsv")
