import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    "gene_motif_matrix.tsv",
    sep="\t",
    index_col=0
)

# Row-normalize
df_norm = df.div(df.sum(axis=1), axis=0) * 100

# Remove very rare motifs
df_norm = df_norm.loc[:, df_norm.max(axis=0) > 1]

sns.set_theme(style="white")

g = sns.clustermap(
    df_norm,
    cmap="viridis",
    figsize=(14,8),
    linewidths=0.5,
    row_cluster=False,
    col_cluster=True
)

g.fig.suptitle(
    "Gene-Specific SSR Motif Landscape in Nipah Virus",
    fontsize=16,
    fontweight="bold"
)

g.savefig(
    "gene_motif_heatmap.png",
    dpi=600,
    bbox_inches="tight"
)

print("Heatmap saved!")
