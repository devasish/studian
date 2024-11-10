from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print(score)

### find the best n_neighbours valus 

n_neighbors_list = list(range(1,30))
scores = []
score_map = []
best_score, best_n_neighbors=0,0
for n_neighbors in n_neighbors_list:
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    scores.append(score)
    if score > best_score: best_score,best_n_neighbors=score, n_neighbors
    print(score)

print(f"Best Score {best_score} with number of neighbors: {best_n_neighbors}")
# plt.figure()
# plt.plot(n_neighbors_list, scores)
# plt.show()


import mglearn
from matplotlib import pyplot as plt

# plot_knn_classification(n_neighbors=3)
mglearn.plots.plot_knn_classification(n_neighbors=3)
plt.show()



