import pandas as pd

df = pd.read_csv(
    "ssr_density_track.bed",
    sep="\t",
    header=None
)

df.columns = [
    "contig",
    "start",
    "end",
    "score"
]

df[["start","score"]].to_csv(
    "proksee_density.tsv",
    sep="\t",
    index=False
)

print("Saved proksee_density.tsv")
