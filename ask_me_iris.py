# Import Iris Data Set
import sklearn
from sklearn.datasets import load_iris

iris = load_iris()
print iris.feature_names
print iris.target_names