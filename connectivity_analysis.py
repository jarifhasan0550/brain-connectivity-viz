import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Representing 10 brain regions (e.g., Prefrontal Cortex, Amygdala, etc.)
regions = [f"Region_{i}" for i in range(1, 11)]
data = np.random.rand(10, 10)
connectivity_matrix = (data + data.T) / 2 # Making it symmetrical
np.fill_diagonal(connectivity_matrix, 1) # Self-correlation is always 1

df = pd.DataFrame(connectivity_matrix, index=regions, columns=regions)

# This addresses the 'data visualization' requirement
plt.figure(figsize=(10, 8))
sns.heatmap(df, annot=True, cmap='coolwarm', vmin=0, vmax=1)
plt.title("Functional Brain Connectivity Matrix")

# Save for 'Data Dissemination'
plt.savefig("connectivity_heatmap.png")
print("Visualization generated successfully.")
