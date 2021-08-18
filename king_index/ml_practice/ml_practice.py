import pandas as pd
# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

# Add label
train_df = pd.read_excel('./data/train.xls')
train_df['Good'] = 0

test_df = pd.read_excel('./data/test.xls')
test_df['Good'] = 0

# If price rise over 10%, mark it as positive whitch is represent by 1.
for i in range(train_df.shape[0]):
    if train_df.iloc[i,6]>=10:
        train_df.iloc[i,7] = 1
for i in range(test_df.shape[0]):
    if test_df.iloc[i,6]>=10:
        test_df.iloc[i,7] = 1

Y_train = train_df["Good"]
X_train = train_df.drop(["Good","id","name","return"], axis=1)

Y_test = test_df["Good"]
X_test = test_df.drop(["Good","id","name","return"], axis=1)


# Supervised Learning
# Classfication and Regression

# Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train,Y_train)
Y_pred = logreg.predict(X_test)
acc_log = round(logreg.score(X_train, Y_train)*100,2)
acc_log_pre = round(logreg.score(X_test, Y_test)*100,2)

# Support Vector Machines
svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
acc_svc_pre = round(svc.score(X_test, Y_test) * 100, 2)

# k-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
acc_knn = round(knn.score(X_train, Y_train) * 100, 2)
acc_knn_pre = round(knn.score(X_test, Y_test) * 100, 2)

# Gaussian Naive Bayes
gaussian = GaussianNB()
gaussian.fit(X_train, Y_train)
Y_pred = gaussian.predict(X_test)
acc_gaussian = round(gaussian.score(X_train, Y_train) * 100, 2)
acc_gaussian_pre = round(gaussian.score(X_test, Y_test) * 100, 2)

# Decision Tree
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, Y_train)
Y_pred = decision_tree.predict(X_test)
acc_decision_tree = round(decision_tree.score(X_train, Y_train) * 100, 2)
acc_decision_tree_pre = round(decision_tree.score(X_test, Y_test) * 100, 2)

# Random Forest
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, Y_train)
Y_pred = random_forest.predict(X_test)
random_forest.score(X_train, Y_train)
acc_random_forest = round(random_forest.score(X_train, Y_train) * 100, 2)
acc_random_forest_pre = round(random_forest.score(X_test, Y_test) * 100, 2)

acc = {
    "acc_log": [acc_log,acc_log_pre],
    "acc_svc": [acc_svc,acc_svc_pre],
    "acc_knn": [acc_knn,acc_knn_pre],
    "acc_gaussian": [acc_gaussian,acc_gaussian_pre],
    "acc_decision_tree": [acc_decision_tree,acc_decision_tree_pre],
    "acc_random_forest": [acc_random_forest,acc_random_forest_pre],
}

print(acc)