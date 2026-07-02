import pandas as pd

# Load SSR table
df = pd.read_csv(
    "crossroad_unfair1000/job_1781073771422_537/output/main/mergedOut.tsv",
    sep="\t"
)

# Nipah reference gene coordinates
genes = [
    ("N", 55, 2297),
    ("P", 2300, 5004),
    ("M", 5007, 6366),
    ("F", 6369, 8706),
    ("G", 8709, 11255),
    ("L", 11258, 18213)
]

# Assign each SSR to a gene
assigned_genes = []

for _, row in df.iterrows():

    start = row["start"]
    end = row["stop"]

    midpoint = (start + end) / 2

    assigned_gene = "INTERGENIC"

    for gene, gene_start, gene_end in genes:

        if gene_start <= midpoint <= gene_end:
            assigned_gene = gene
            break

    assigned_genes.append(assigned_gene)

# Add gene column
df["gene"] = assigned_genes

# Create Gene × Motif matrix
heatmap = pd.crosstab(df["gene"], df["motif"])

# Save matrix
heatmap.to_csv(
    "gene_motif_matrix.tsv",
    sep="\t"
)

print("\nMatrix shape:")
print(heatmap.shape)

print("\nFirst rows:")
print(heatmap.head())

print("\nSaved:")
print("gene_motif_matrix.tsv")
