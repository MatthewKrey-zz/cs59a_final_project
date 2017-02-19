'''Visualize Decision Tree to see how tree.DecisionTreeClassifier() works on lines 34-35 of ask_me_iris.py

This is the section of the script that generates the iris.pdf file

This is not necessary to run ask_me_iris.py, but if you are curious, copy & paste this to the bottom of
ask_me_iris.py or to a new cell in Jupyter notebooks at the bottom of ask_me_iris.ipynb to visualize
DecisionTreeClassifier() and generate iris.pdf

'''

import pydotplus
from sklearn.externals.six import StringIO

dot_data = StringIO()
tree.export_graphviz(clf,
                        out_file = dot_data,
                        feature_names = iris.feature_names,
                        class_names = iris.target_names,
                        filled = True,
                        rounded = True,
                        impurity = False)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")

print test_data[0], test_target[0]
print test_data[1], test_target[1]

print iris.feature_names
print iris.target_names