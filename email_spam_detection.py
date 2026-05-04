# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import tree, svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

# ---------------------------
# Load Data
# ---------------------------
data = pd.read_csv("/content/spam_ham_dataset.csv")

# ---------------------------
# Basic Cleaning
# ---------------------------
data.drop_duplicates(inplace=True)
data.dropna(inplace=True)

# Drop unused column
if "label" in data.columns:
    data.drop("label", axis=1, inplace=True)

# Add a simple feature (text length)
data["text_length"] = data["text"].str.len()

# ---------------------------
# Train/Test Split
# ---------------------------
X = data["text"]
Y = data["label_num"]

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y
)

# ---------------------------
# Feature Extraction
# ---------------------------
vectorizer = TfidfVectorizer(min_df=2, stop_words='english', lowercase=True)

X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

# ---------------------------
# Models
# ---------------------------
models = [
    ('LogisticRegression', LogisticRegression(max_iter=200)),
    ('DecisionTree', tree.DecisionTreeClassifier()),
    ('SVC', svm.SVC(kernel='linear')),
    ('KNN', KNeighborsClassifier(n_neighbors=5)),
    ('RandomForest', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('NaiveBayes', MultinomialNB())
]

# ---------------------------
# Evaluation
# ---------------------------
for name, model in models:
    model.fit(X_train_features, y_train)
    y_pred = model.predict(X_test_features)

    print('-----------------------------------------------------')
    print(f"{name} Classification Report:\n")
    print(classification_report(y_test, y_pred))

    disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred))
    disp.plot()
    plt.title(f"Confusion Matrix - {name}")
    plt.show()

# ---------------------------
# Cross Validation
# ---------------------------
kf = KFold(n_splits=5, shuffle=True, random_state=42)

for name, model in models:
    pipe = Pipeline([
        ('tfidf', TfidfVectorizer(min_df=2, stop_words='english')),
        ('model', model)
    ])
    scores = cross_val_score(pipe, X, Y, cv=kf)
    print(f"{name} CV Accuracy: {np.mean(scores)*100:.2f}%")

# ---------------------------
# Prediction
# ---------------------------
user_input = input("Enter an email: ")

user_features = vectorizer.transform([user_input.lower()])

for name, model in models:
    prediction = model.predict(user_features)

    if prediction == 0:
        print(f"{name} Prediction: ham")
    else:
        print(f"{name} Prediction: spam")
