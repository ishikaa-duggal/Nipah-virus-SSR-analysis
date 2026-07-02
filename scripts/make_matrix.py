import pandas as pd
import numpy as np
import os

ani_raw = pd.read_csv('ani_output.txt', sep='\t', header=None)
ani_raw.columns = ['ref', 'query', 'ani', 'frags', 'total']

def clean_name(path):
    return os.path.basename(path).replace('.fasta', '')

ani_raw['ref_name'] = ani_raw['ref'].apply(clean_name)
ani_raw['query_name'] = ani_raw['query'].apply(clean_name)

genomes = sorted(ani_raw['ref_name'].unique())
ani_matrix = pd.DataFrame(np.nan, index=genomes, columns=genomes)

for _, row in ani_raw.iterrows():
    ani_matrix.loc[row['ref_name'], row['query_name']] = row['ani']

for g in genomes:
    ani_matrix.loc[g, g] = 100.0

ani_matrix = ani_matrix.fillna(ani_matrix.T)
ani_matrix.to_csv('ani_matrix.csv')
print("✓ Matrix ready!")
