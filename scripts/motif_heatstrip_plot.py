import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------
# Load matrix
# ----------------------------------

heatmap = pd.read_csv(
    "motif_heatstrip_matrix.tsv",
    sep="\t",
    index_col=0
)

# ----------------------------------
# Plot
# ----------------------------------

fig, ax = plt.subplots(
    figsize=(16,6),
    facecolor="white"
)

im = ax.imshow(
    heatmap,
    aspect="auto",
    cmap="Blues",
    interpolation="nearest"
)

# ----------------------------------
# Y labels
# ----------------------------------

ax.set_yticks(
    np.arange(len(heatmap.index))
)

ax.set_yticklabels(
    heatmap.index,
    fontsize=11,
    fontweight="bold"
)

# ----------------------------------
# X axis
# ----------------------------------

genome_length = 18246
n_bins = heatmap.shape[1]

tick_positions = [0,10,20,30,40,49]

tick_labels = [
    int(i*(genome_length/n_bins))
    for i in tick_positions
]

ax.set_xticks(tick_positions)
ax.set_xticklabels(tick_labels)

ax.set_xlabel(
    "Genome Position (bp)",
    fontsize=12,
    fontweight="bold"
)

ax.set_ylabel(
    "Dominant SSR Motifs",
    fontsize=12,
    fontweight="bold"
)

# ----------------------------------
# Gene boundaries
# ----------------------------------

boundaries = [
    2297,
    5004,
    6366,
    8706,
    11255
]

for b in boundaries:

    bin_pos = b/(genome_length/n_bins)

    ax.axvline(
        bin_pos,
        color="black",
        linestyle="--",
        linewidth=1,
        alpha=0.5
    )

# ----------------------------------
# Title
# ----------------------------------

ax.set_title(
    "Heatmap of Genomic Distribution of Dominant SSR Motifs",
    fontsize=15,
    fontweight="bold",
    pad=15
)

# ----------------------------------
# Colorbar
# ----------------------------------

cbar = plt.colorbar(im)

cbar.set_label(
    "Number of Unique Sites",
    fontsize=11
)

plt.tight_layout()

# ----------------------------------
# Save
# ----------------------------------

plt.savefig(
    "motif_heatstrip.png",
    dpi=1200,
    bbox_inches="tight"
)

plt.savefig(
    "motif_heatstrip.pdf",
    bbox_inches="tight"
)

plt.savefig(
    "motif_heatstrip.svg",
    bbox_inches="tight"
)

print("Saved motif_heatstrip.png/pdf/svg")
