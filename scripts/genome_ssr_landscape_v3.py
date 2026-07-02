import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Load data
# -------------------------

df = pd.read_csv(
    "top_motif_positions.tsv",
    sep="\t"
)

summary = (
    df.groupby("motif")["mid"]
      .agg(["min","max","count","nunique"])
      .reset_index()
)

summary.columns = [
    "motif",
    "min",
    "max",
    "SSRs",
    "Sites"
]

motif_order = [
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

summary["y"] = summary["motif"].map(
    {m:i for i,m in enumerate(reversed(motif_order))}
)

# -------------------------
# Gene coordinates
# -------------------------

genes = [
    ("N",55,2297),
    ("P",2300,5004),
    ("M",5007,6366),
    ("F",6369,8706),
    ("G",8709,11255),
    ("L",11258,18213)
]

# -------------------------
# Colors
# -------------------------

colors = {
    "ATT":"crimson",
    "TAA":"darkorange",
    "GAT":"steelblue",
    "TTTC":"steelblue",
    "CTA":"steelblue",
    "ATG":"steelblue",
    "AAG":"steelblue",
    "CAG":"steelblue",
    "TCA":"steelblue",
    "GTA":"steelblue"
}

# -------------------------
# Plot
# -------------------------

fig, ax = plt.subplots(figsize=(18,8))

for _, row in summary.iterrows():

    motif = row["motif"]

    ax.hlines(
        row["y"],
        row["min"],
        row["max"],
        color=colors[motif],
        linewidth=8
    )

    ax.plot(
        row["min"],
        row["y"],
        "o",
        color=colors[motif],
        markersize=8
    )

    ax.plot(
        row["max"],
        row["y"],
        "o",
        color=colors[motif],
        markersize=8
    )

    ax.text(
        row["max"] + 250,
        row["y"],
        f'{int(row["SSRs"])} SSRs | {int(row["Sites"])} sites',
        va="center",
        fontsize=10
    )

# -------------------------
# Gene boundaries
# -------------------------

boundaries = [
    2297,
    5004,
    6366,
    8706,
    11255
]

for b in boundaries:

    ax.axvline(
        b,
        linestyle="--",
        linewidth=1,
        alpha=0.5,
        color="grey"
    )

# -------------------------
# Gene track
# -------------------------

gene_y = -2

for gene,start,end in genes:

    ax.fill_between(
        [start,end],
        gene_y-0.3,
        gene_y+0.3,
        alpha=0.4
    )

    ax.text(
        (start+end)/2,
        gene_y-0.75,
        gene,
        ha="center",
        fontsize=12,
        fontweight="bold"
    )

# -------------------------
# Formatting
# -------------------------

ax.set_xlim(0,19000)

ax.set_yticks(summary["y"])
ax.set_yticklabels(summary["motif"])

ax.set_xlabel(
    "Genome Position (bp)",
    fontsize=13
)

ax.set_ylabel(
    "Dominant SSR Motifs",
    fontsize=13
)

ax.set_title(
    "Genomic Localization of Dominant SSR Motifs in Nipah Virus",
    fontsize=16,
    fontweight="bold"
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()

plt.savefig(
    "genome_ssr_landscape_v3.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    "genome_ssr_landscape_v3.pdf",
    bbox_inches="tight"
)

plt.savefig(
    "genome_ssr_landscape_v3.svg",
    bbox_inches="tight"
)

print("Saved:")
print("genome_ssr_landscape_v3.png")
print("genome_ssr_landscape_v3.pdf")
print("genome_ssr_landscape_v3.svg")
