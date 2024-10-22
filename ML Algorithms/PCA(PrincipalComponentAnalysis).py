#SupportVectorMachine(SVM)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Step 1: Load example data
data = load_iris()
X = data.data
y = data.target

# Step 2: Perform PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Step 3: Visualize the results
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, s=50, cmap='viridis')
plt.title('PCA of Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
