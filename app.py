# from pca import X_train, X_test pca loses the label but it might be needed
# from scaling import X_train
from splitting import X_train, X_test, y_train, y_test
# from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix

# model building
dt_clf = DecisionTreeClassifier()

model = dt_clf.fit(X_train, y_train)
prediction = model.predict([[3, 2, 3, 1, 4, 0, 2, 2, 3, 4, 1, 2, 4, 5, 1, 3, 4, 3, 3, 2]])
print("Age predicted as ", prediction)  # single age predicted

y_pred = dt_clf.predict(X_test)  # making prediction

# visualization

text_representation = export_text(dt_clf)

with open("decistion_tree.log", "w") as fout:
    fout.write(text_representation)

fig = plt.figure(figsize=(25, 20))
_ = plot_tree(dt_clf, filled=True)
fig.savefig("decistion_tree.png")

# model elimination

cm = confusion_matrix(y_pred, y_test)
print("Confusion Matrix ", cm)

if __name__ == "__main__":
    pass
