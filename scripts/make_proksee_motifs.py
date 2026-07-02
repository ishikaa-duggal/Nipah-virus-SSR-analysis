import pandas as pd

df = pd.read_csv(
    "crossroad_unfair1000/job_1781073771422_537/output/main/mergedOut.tsv",
    sep="\t"
)

top_motifs = [
    "ATT","GAT","CTA","ATG","TTTC",
    "TAA","AAG","CAG","TCA","GTA"
]

df = df[df["motif"].isin(top_motifs)]

df["mid"] = (
    df["start"] + df["stop"]
) / 2

df = df.drop_duplicates(
    subset=["motif","mid"]
)

out = df[["mid","motif"]].copy()

out.columns = [
    "start",
    "name"
]

out["start"] = out["start"].astype(int)

out.to_csv(
    "proksee_top_motifs.tsv",
    sep="\t",
    index=False
)

print(out.head())
print("\nSaved proksee_top_motifs.tsv")
