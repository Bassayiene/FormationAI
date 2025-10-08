from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import numpy as np

# do not edit this
# create fake data
x, y = make_moons(
    n_samples=500,  # the number of observations
    random_state=42,
    noise=0.3
)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# Try different values of k (e.g. 1, 5, 15, 133)
for k in range(1,20):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)

    # Compute accuracies
    train_acc = knn.score(x_train, y_train)
    test_acc = knn.score(x_test, y_test)

    print(f"k = {k}")
    print("training accuracy: %f" % train_acc)
    print("testing accuracy: %f" % test_acc)
