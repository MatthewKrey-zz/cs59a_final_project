# Import Dependent Libraries & Iris Data Set

import sklearn
import numpy as np
import pandas as pd
import pydotplus
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

        print '''\nThis is my favorite part! First, you pick a random feature set from the Iris data set and you guess what species it is based on its features.
        Then I'll pick a random Iris from the data set and I'll guess that species it is. Then we can compare and see how we both did!\n'''

        # Select Random Iris features from Iris Data Set

        print "\nWhen you are ready, let's do this!\n\n 1. Choose Random Iris\n 2. Play another time.\n"

        user_selected_iris = raw_input("> ")

        if user_selected_iris == "2":
            print "Too bad... Perhaps another day then."

        elif user_selected_iris == "1":
            shape = np.shape(iris.data)
            shuffle = np.random.shuffle(iris.data)
            X_train = iris.data[:200, 1:5]
            random_user_selection = iris.data[np.random.randint(iris.data.shape[0], size=1)]
            print "Your randomly selected features are: %s" % (random_user_selection)

            # Capture and store user's guess

            print "\nBased on these features, what species of Iris do you think your flower is?\n"
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

            print "TEST TEST: user_guess = %s" % (user_guess)

            # Feed user example to Iris and see what her guess is

            print "\n\nNow it's my turn... I am one with the Force, the Force is with me!"

            print "\n\nYour features are: %s" % (random_user_selection)
            iris_guess = clf.predict(random_user_selection)
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
                print "\nWe agree!"
            elif user_guess != iris_final_answer:
                print "\nYou think %s, I think %s ... Who is the winner???" % (user_guess, iris_final_answer)

elif welcome_answer == "2":
    print "Right on! You are going to love this game."


    print '''\nOkay. We are going to explore my favorite data set, the Iris Data Set, by sampling Irises and guessing
    what species they are! \nIt has my favorite Iris species in it: %s.\n\nTo determine what species we would like to guess,
    we are going to look at each Iris's features: %s.\n\nLet's take a look at the data together now: \n''' % (iris.target_names,iris.feature_names, )

    for i in range(len(iris.target)):
        print "Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i])

    print '''\nThis is my favorite part! First, you pick a random feature set from the Iris data set and you guess what species it is based on its features.
Then I'll pick a random Iris from the data set and I'll guess that species it is. Then we can compare and see how we both did!\n'''


    # Select Random Iris features from Iris Data Set

    print "\nWhen you are ready, let's do this!\n\n 1. Choose Random Iris\n 2. Play another time.\n"

    user_selected_iris = raw_input("> ")

    if user_selected_iris == "2":
        print "Too bad... Perhaps another day then."

    elif user_selected_iris == "1":
        shape = np.shape(iris.data)
        shuffle = np.random.shuffle(iris.data)
        X_train = iris.data[:200, 1:5]
        random_user_selection = iris.data[np.random.randint(iris.data.shape[0], size=1)]
        print "Your randomly selected features are: %s" % (random_user_selection)

        # Capture and store user's guess

        print "\nBased on these features, what species of Iris do you think your flower is?\n"
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

        print "TEST TEST: user_guess = %s" % (user_guess)

        # Feed user example to Iris and see what her guess is

        print "\n\nNow it's my turn... I am one with the Force, the Force is with me!"

        print "\n\nYour features are: %s" % (random_user_selection)
        iris_guess = clf.predict(random_user_selection)
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
            print "\nWe agree!"
        elif user_guess != iris_final_answer:
            print "\nYou think %s, I think %s ... Who is the winner???" % (user_guess, iris_final_answer)