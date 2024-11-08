import matplotlib.pyplot as plt
import mglearn
import mglearn.datasets
import numpy as np

X, y = mglearn.datasets.make_forge()
print(X, y)
mglearn.discrete_scatter(X[:,0], X[:, 1], y)

plt.legend(["Class 0", "Class 1"], loc=4)
plt.xlabel("First Feature")
plt.ylabel("Second Feature")
print(f"X.shape: {X.shape}")
print(type(X), X)
plt.show()
###

X, y = mglearn.datasets.make_wave()
plt.figure() # Creates a new figure 

plt.plot(X[:,0],y, 'o')
plt.xlabel('Feature')
plt.ylabel('Target')

plt.show()


