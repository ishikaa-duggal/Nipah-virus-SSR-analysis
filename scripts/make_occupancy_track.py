import pandas as pd

df = pd.read_csv(
    "crossroad_unfair1000/job_1781073771422_537/output/main/mergedOut.tsv",
    sep="\t"
)

# midpoint of SSR
df["mid"] = (
    df["start"] + df["stop"]
) / 2

# round nearby sites together
df["site"] = (
    df["mid"] / 50
).round() * 50

n_genomes = df["genomeID"].nunique()

occ = (
    df.groupby("site")["genomeID"]
      .nunique()
      .reset_index()
)

occ["occupancy"] = (
    occ["genomeID"] / n_genomes
) * 100

out = occ[["site","occupancy"]].copy()

out.columns = [
    "start",
    "score"
]

out["start"] = out["start"].astype(int)

out.to_csv(
    "proksee_occupancy.tsv",
    sep="\t",
    index=False
)

print(out.head())
print("\nGenomes =", n_genomes)
print("Sites =", len(out))
print("\nSaved proksee_occupancy.tsv")
