import matplotlib.pyplot as plt
import mglearn
import mglearn.datasets
import numpy as np
import sys
import pandas as pd

###3
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
cancer = load_breast_cancer()
print(cancer.keys())
print(f"Shape of cancer data {cancer.data.shape}")
print(f"Feature names of cancer data: {cancer.feature_names}")
#print(cancer.DESCR)


X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=47)
cancer_df = pd.DataFrame(X_train[:, :5], columns=cancer.feature_names[:5])

pd.plotting.scatter_matrix(cancer_df, c=y_train, figsize=(50, 50), marker='o', hist_kwds={'bins': 20}, s=60, alpha=0.8, cmap=mglearn.cm3)
plt.show()

sys.exit(0)
###2
X, y = mglearn.datasets.make_forge()
print(X, y)
mglearn.discrete_scatter(X[:,0], X[:, 1], y)

plt.legend(["Class 0", "Class 1"], loc=4)
plt.xlabel("First Feature")
plt.ylabel("Second Feature")
print(f"X.shape: {X.shape}")
print(type(X), X)
plt.show()
###1

X, y = mglearn.datasets.make_wave()
plt.figure() # Creates a new figure 

plt.plot(X[:,0],y, 'o')
plt.xlabel('Feature')
plt.ylabel('Target')

plt.show()


