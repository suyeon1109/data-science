import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage

# features, true_labels = make_blobs(
#     n_samples=200,
#     centers=3,
#     cluster_std=2.75,
#     random_state=42
# )

## Real Data Set

df = pd.read_csv('/Users/mac/Documents/GitHub/data-science/lecture/real-dataset.csv')
print(df.head(13))

df_protein = df[['RedMeat',  'WhiteMeat',  'Eggs',  'Milk',  'Fish',  'Cereals',  'Starch',  'Nuts',  'Fr.Veg']]
labelList = list(df['Country'])

Z1 = linkage(df_protein, method='single', metric='euclidean')
Z2 = linkage(df_protein, method='complete', metric='euclidean')
Z3 = linkage(df_protein, method='average', metric='euclidean')

plt.plot(), dendrogram(Z1,labels=labelList), plt.title('Single')
plt.show()

plt.plot(), dendrogram(Z2,labels=labelList), plt.title('Complete')
plt.show()

plt.plot(), dendrogram(Z3,labels=labelList), plt.title('Average')
plt.show()
