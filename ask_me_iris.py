# Import Dependent Libraries & Iris Data Set

import sklearn
import numpy as np
import pandas as pd
import pydotplus
import time
from sklearn.datasets import load_iris
from sklearn import tree
from numpy import random, arange
from random import randrange
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
Enter the number of your choice.\n
1. No
2. Yes
3. Maybe \n'''


welcome_answer = raw_input("> ")

if welcome_answer == "1":
    print "Okay. No worries. Perhaps another time."

elif welcome_answer == "3":
    print "Are you sure? It is SUPER fun! I love data. I think you will too. Want to join the fun? Enter the number of your choice.\n\n 1. No \n 2. Yes\n"
    maybe_answer = raw_input("> ")
    if maybe_answer == "1":
        print "Alright grumpy pants. I'm going to go find some data sets!"
    if maybe_answer == "2":
        shape = np.shape(iris.data)
        shuffle = np.random.shuffle(iris.data)
        X_train = iris.data[:200, 1:5]
        random_user_selection1 = iris.data[np.random.randint(iris.data.shape[0], size=1)]
        random_user_selection2 = iris.data[np.random.randint(iris.data.shape[0], size=1)]
        random_user_selection3 = iris.data[np.random.randint(iris.data.shape[0], size=1)]
        random_user_selection4 = iris.data[np.random.randint(iris.data.shape[0], size=1)]
        random_user_selection5 = iris.data[np.random.randint(iris.data.shape[0], size=1)]
        random_user_selection6 = iris.data[np.random.randint(iris.data.shape[0], size=1)]

        print "Now let's look at some examples.\n"
        print "Your features are: %s" % random_user_selection1
        time.sleep(1)
        print "Your features are: %s" % random_user_selection2
        time.sleep(1)
        print "Your features are: %s" % random_user_selection3
        time.sleep(1)
        print "Your features are: %s" % random_user_selection4
        time.sleep(1)
        print "Your features are: %s" % random_user_selection5
        time.sleep(1)
        print "Your features are: %s" % random_user_selection6
        time.sleep(1)

        print "\nDo you notice any patterns? If you do, you are using the same process our classifier will use.\n"

        print '''\nThis is my favorite part! Let's have you pick a random flower. Then I will pick a random flower.\n
                Based on the features of our flowers, we will both guess what species they are. Then we can compare and see how we both did!\n'''

        # Capture and store user's guess

        random_user_selection7 = iris.data[np.random.randint(iris.data.shape[0], size=1)]
        print "\n Our flower has the following features: %s" % (random_user_selection7)

        print "\nBased on these features, what species of Iris do you think your flower is? Enter the number of your choice. \n"
        print "\n0. setosa \n1. versicolor \n2. virginica"
        guess = raw_input("> ")

        if guess == "0":
            print "\nOkay. setosa. Your guess is as good as mine... OR IS IT?!\n"
            user_guess = "setosa"
        elif guess == "1":
            print "\nOkay. versicolor. Your guess is as good as mine... OR IS IT?!\n"
            user_guess = "versicolor"
        elif guess == "2":
            print "\nOkay. virginica. Your guess is as good as mine... OR IS IT?!\n"
            user_guess = "virginica"

        # Feed user example to Iris and see what her guess is

        print "\n\nNow it's my turn... I am one with the Force, the Force is with me!"

        print "\n\nYour features are: %s" % (random_user_selection7)
        iris_guess = clf.predict(random_user_selection7)
        iris_answer = str(iris_guess)
        print "\n\nHmmm... I think it is: %s" % (iris_guess)

        # Convert iris_guess & store iris_final_answer

        iris_final_answer = ""
        if "[0]" in iris_answer:
            iris_final_answer = "setosa"
        elif "[1]" in iris_answer:
            iris_final_answer = "versicolor"
        elif "[2]" in iris_answer:
            iris_final_answer = "virginica"

        # Compare user_guess vs. iris_guess
        print "You guessed: %s" % (user_guess)
        print "I guessed: %s, %s" % (iris_guess, iris_final_answer)

        # Print Final Result

        if user_guess == iris_final_answer:
            print "\nWe agree! We both classified our flower as the same species"
        elif user_guess != iris_final_answer:
            print "\nYou think %s, I think %s ... we both classified our flowers differently. Perhaps we can go back and figure out why. Thanks for playing! " % (
            user_guess, iris_final_answer)

        print "***THE END***"

elif welcome_answer == "2":
    print "Right on! You are going to love this game."

    print '''\nOkay. We are going to explore a data set of flowers, called Irises.\n
            To determine what species we would like to guess, or classify, we are going to look at each Iris's features.\n
            The features we are going to use to try and classify our flowers are: %s.\n
            These features will help us to determine what species a flower is - %s.\n
            If a label is 0, the flower is a setosa.\n
            If a label is 1, the flower is a versicolor.\n
            If a label is 2, the flower is a virginica.\n
            \nLet's look at a few examples \n''' % (iris.feature_names, iris.target_names)

    count = 0
    for i in range(len(iris.target)):
        print "Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i])
        count += 1
        if count == 3:
            break


    # Select Random Iris features from Iris Data Set

    print '''\nHmmm... this is interesting. It looks like Setosas have a bit of a pattern in petal width. This may be a good feature to help us classify our flowers.\n
          When you are ready, let's look at a few more examples to see if we can find other features to help us further classify.\n\n 1. Choose Random Iris\n 2. Play another time. Enter the number of your choice.\n'''

    user_selected_iris = raw_input("> ")

    if user_selected_iris == "2":
        print "Too bad... Perhaps another day then."

    elif user_selected_iris == "1":
        shape = np.shape(iris.data)
        shuffle = np.random.shuffle(iris.data)
        X_train = iris.data[:200, 1:5]
        random_user_selection1 = iris.data[np.random.randint(iris.data.shape[0], size=1)]
        random_user_selection2 = iris.data[np.random.randint(iris.data.shape[0], size=1)]
        random_user_selection3 = iris.data[np.random.randint(iris.data.shape[0], size=1)]
        random_user_selection4 = iris.data[np.random.randint(iris.data.shape[0], size=1)]
        random_user_selection5 = iris.data[np.random.randint(iris.data.shape[0], size=1)]
        random_user_selection6 = iris.data[np.random.randint(iris.data.shape[0], size=1)]


        print "Now let's look at some examples.\n"
        print "Your features are: %s" % random_user_selection1
        time.sleep(1)
        print "Your features are: %s" % random_user_selection2
        time.sleep(1)
        print "Your features are: %s" % random_user_selection3
        time.sleep(1)
        print "Your features are: %s" % random_user_selection4
        time.sleep(1)
        print "Your features are: %s" % random_user_selection5
        time.sleep(1)
        print "Your features are: %s" % random_user_selection6
        time.sleep(1)

        print "\nDo you notice any patterns? If you do, you using the same process our classifier will use.\n"

        print '''\nThis is my favorite part! Let's have you pick a random flower. Then I will pick a random flower.\n
        Based on the features of our flowers, we will both guess what species they are. Then we can compare and see how we both did!\n'''

        # Capture and store user's guess

        random_user_selection7 = iris.data[np.random.randint(iris.data.shape[0], size=1)]
        print "\n Our flower has the following features: %s" % (random_user_selection7)

        print "\nBased on these features, what species of Iris do you think your flower is? Enter the number of your choice. \n"
        print "\n0. setosa \n1. versicolor \n2. virginica"
        guess = raw_input("> ")

        if guess == "0":
            print "\nOkay. setosa. Your guess is as good as mine... OR IS IT?!\n"
            user_guess = "setosa"
        elif guess == "1":
            print "\nOkay. versicolor. Your guess is as good as mine... OR IS IT?!\n"
            user_guess = "versicolor"
        elif guess == "2":
            print "\nOkay. virginica. Your guess is as good as mine... OR IS IT?!\n"
            user_guess = "virginica"

        # Feed user example to Iris and see what her guess is

        print "\n\nNow it's my turn... I am one with the Force, the Force is with me!"

        print "\n\nYour features are: %s" % (random_user_selection7)
        iris_guess = clf.predict(random_user_selection7)
        iris_answer = str(iris_guess)
        print "\nLet me take a guess based on these features..."
        time.sleep(5)
        print "\n\nHmmm... I think it is: %s" % (iris_guess)

        # Convert iris_guess & store iris_final_answer

        iris_final_answer = ""
        if "[0]" in iris_answer:
            iris_final_answer = "setosa"
        elif "[1]" in iris_answer:
            iris_final_answer = "versicolor"
        elif "[2]" in iris_answer:
            iris_final_answer = "virginica"

        # Compare user_guess vs. iris_guess
        print "You guessed: %s" % (user_guess)
        print "I guessed: %s, %s" % (iris_guess, iris_final_answer)


        # Print Final Result

        if user_guess == iris_final_answer:
            print "\nWe agree! We both classified our flower as the same species"
        elif user_guess != iris_final_answer:
            print "\nYou think %s, I think %s ... we both classified our flowers differently. \nPerhaps we can go back and figure out why. \nThanks for playing! " % (user_guess, iris_final_answer)

        print "\n\n\n***THE END***"