# Import Dependent Libraries & Iris Data Set

import sklearn
import numpy as np
import pydotplus
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO

# Test data set

iris = load_iris()
# print iris.feature_names
# print iris.target_names

# Split Training & Test Data

test_idx = [0,50,100]

# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# Train Decision Tree Classifier on training data

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

# print test_target
# print clf.predict(test_data)

# Begin Intro of Iris to User

print '''Hello, my name is Iris. I love data and I love to play games. \n
Would you like to play a game about my favorite data set with me? \n
1. No
2. Yes
3. Maybe \n'''

answer = raw_input("> ")

if answer == "1":
    print "Okay. No worries. Perhaps another time."

elif answer == "3":
    print "Are you sure? It is SUPER fun! I love data. I think you will too. Want to join the fun? \n\n 1. No \n 2. Yes\n"
    maybe_answer = raw_input("> ")
    if maybe_answer == "1":
        print "Alright grumpy pants. I'm going to go find some data sets!"
    if maybe_answer == "2":
        print "Right on! Let's play! :)"

elif answer == "2":
    print "Right on! You are going to love this game."


    # for i in range(len(iris.target)):
    #     print "Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i])