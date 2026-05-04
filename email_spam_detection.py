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
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

def load_data(file_path):
    """Load the dataset from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """Preprocess the data by dropping duplicates and handling missing values."""
    data.drop_duplicates(inplace=True)
    data.dropna(inplace=True)
    return data

def split_data(data):
    """Split the data into training and testing sets."""
    X = data["text"]
    Y = data["label_num"]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
    return X_train, X_test, y_train, y_test

def extract_features(X_train, X_test):
    """Extract features from the text data using TF-IDF vectorization."""
    vectorizer = TfidfVectorizer(min_df=2, stop_words='english', lowercase=True)
    X_train_features = vectorizer.fit_transform(X_train)
    X_test_features = vectorizer.transform(X_test)
    return X_train_features, X_test_features

def train_model(X_train_features, y_train):
    """Train a machine learning model on the training data."""
    models = [
        ('LogisticRegression', LogisticRegression(max_iter=200)),
        ('DecisionTree', tree.DecisionTreeClassifier()),
        ('SVC', svm.SVC(kernel='linear')),
        ('KNN', KNeighborsClassifier(n_neighbors=5)),
        ('RandomForest', RandomForestClassifier(n_estimators=100, random_state=42)),
        ('NaiveBayes', MultinomialNB())
    ]
    for name, model in models:
        model.fit(X_train_features, y_train)
        yield name, model

def evaluate_model(model, X_test_features, y_test):
    """Evaluate the performance of a machine learning model."""
    y_pred = model.predict(X_test_features)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model: {model.__class__.__name__}")
    print(f"Accuracy: {accuracy:.2f}")
    print(classification_report(y_test, y_pred))
    disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred))
    disp.plot()
    plt.show()

def main():
    file_path = "/content/spam_ham_dataset.csv"
    data = load_data(file_path)
    data = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(data)
    X_train_features, X_test_features = extract_features(X_train, X_test)
    for name, model in train_model(X_train_features, y_train):
        evaluate_model(model, X_test_features, y_test)

if __name__ == "__main__":
    main()