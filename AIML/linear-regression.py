from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

cancer = load_breast_cancer()
X_train, X_test, y_train,y_test = train_test_split(cancer.data, cancer.target, random_state=1)

model = LinearRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))


