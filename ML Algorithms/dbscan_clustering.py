#DBSCAN Clustering Code


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN

# Step 1: Create some example data
# We’ll create two interleaving half circles to simulate a clustering scenario.
X, _ = make_moons(n_samples=300, noise=0.05)

# Step 2: Set up the DBSCAN algorithm
# Here, we define how DBSCAN will group our data.
# - `eps`: This is the maximum distance between two points to be considered in the same cluster.
# - `min_samples`: This is the minimum number of points needed to form a dense region (or cluster).
dbscan = DBSCAN(eps=0.2, min_samples=5)

# Step 3: Fit the model to our data
# This will run the DBSCAN algorithm on our data and assign cluster labels.
labels = dbscan.fit_predict(X)

# Step 4: Visualize the results
plt.figure(figsize=(10, 6))

# Get the unique labels (clusters) and create a color for each
unique_labels = set(labels)
colors = [plt.cm.Spectral(i / len(unique_labels)) for i in range(len(unique_labels))]

# Plot each cluster
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Use black color for noise points
        col = 'k'  
    
    # Get the points that belong to this cluster
    class_member_mask = (labels == k)
    xy = X[class_member_mask]
    
    # Scatter plot of the points
    plt.scatter(xy[:, 0], xy[:, 1], s=50, c=[col], label=f'Cluster {k}' if k != -1 else 'Noise')

# Final touches to the plot
plt.title('DBSCAN Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
