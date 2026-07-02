import pandas as pd
import numpy as np

# ==========================
# Load SSRs
# ==========================

df = pd.read_csv(
    "crossroad_unfair1000/job_1781073771422_537/output/main/mergedOut.tsv",
    sep="\t"
)

# ==========================
# Midpoint
# ==========================

df["mid"] = (
    df["start"] + df["stop"]
) / 2

# ==========================
# Genome bins
# ==========================

genome_length = 18246
bin_size = 200

bins = np.arange(
    0,
    genome_length + bin_size,
    bin_size
)

counts, edges = np.histogram(
    df["mid"],
    bins=bins
)

# ==========================
# Export Proksee BED
# ==========================

with open(
    "ssr_density_track.bed",
    "w"
) as out:

    for i, count in enumerate(counts):

        start = int(edges[i])
        end = int(edges[i+1])

        out.write(
            f"NC_002728.1\t{start}\t{end}\t{count}\n"
        )

print("Saved ssr_density_track.bed")
print("Bins:", len(counts))
