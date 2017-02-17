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


welcome_answer = raw_input("> ")

if welcome_answer == "1":
    print "Okay. No worries. Perhaps another time."

elif welcome_answer == "3":
    print "Are you sure? It is SUPER fun! I love data. I think you will too. Want to join the fun? \n\n 1. No \n 2. Yes\n"
    maybe_answer = raw_input("> ")
    if maybe_answer == "1":
        print "Alright grumpy pants. I'm going to go find some data sets!"
    if maybe_answer == "2":
        print "Right on! Let's play! :)"

        print '''\nOkay. We are going to explore my favorite data set, the Iris Data Set, by sampling Irises and guessing
            what species they are! \nIt has my favorite Iris species in it: %s.\n\nTo determine what species we would like to guess,
            we are going to look at each Iris's features: %s.\n\nLet's take a look at the data together now: \n''' % (
        iris.target_names, iris.feature_names,)

        for i in range(len(iris.target)):
            print "Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i])

        print '''\nThis is my favorite part! First, you pick a random Iris from the data set and you guess what species it is.
Then I'll pick a random Iris from the data set and I'll guess that species it is. Then we can compare and see how we both did!'''

elif welcome_answer == "2":
    print "Right on! You are going to love this game."


    print '''\nOkay. We are going to explore my favorite data set, the Iris Data Set, by sampling Irises and guessing
    what species they are! \nIt has my favorite Iris species in it: %s.\n\nTo determine what species we would like to guess,
    we are going to look at each Iris's features: %s.\n\nLet's take a look at the data together now: \n''' % (iris.target_names,iris.feature_names, )

    for i in range(len(iris.target)):
        print "Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i])

    print '''\nThis is my favorite part! First, you pick a random Iris from the data set and you guess what species it is.
Then I'll pick a random Iris from the data set and I'll guess that species it is. Then we can compare and see how we both did!'''