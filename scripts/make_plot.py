import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

ani_matrix = pd.read_csv('ani_matrix.csv', index_col=0)

# NaN values ko handle karo
ani_matrix = ani_matrix.fillna(ani_matrix.mean().mean())

# Check karo
print(f"Matrix shape: {ani_matrix.shape}")
print(f"Any NaN left: {ani_matrix.isna().sum().sum()}")

g = sns.clustermap(
    ani_matrix,
    cmap='RdYlGn',
    vmin=75, vmax=100,
    figsize=(16, 14),
    linewidths=0.5,
    xticklabels=True,
    yticklabels=True,
    method='average',
    metric='euclidean',
)

g.ax_heatmap.set_xticklabels(g.ax_heatmap.get_xticklabels(), rotation=90, fontsize=8)
g.ax_heatmap.set_yticklabels(g.ax_heatmap.get_yticklabels(), rotation=0, fontsize=8)
g.fig.suptitle('NiV ANI Clustermap', fontsize=16, y=0.995)

plt.tight_layout()
plt.savefig('ani_clustermap.png', dpi=300, bbox_inches='tight')
plt.savefig('ani_clustermap.pdf', bbox_inches='tight')
print("✓ Done! Check ani_clustermap.png")
