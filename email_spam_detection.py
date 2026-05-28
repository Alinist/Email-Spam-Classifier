import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV

def load_data(file_path):
    """Load the dataset from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """Preprocess the data by handling missing values and duplicates."""
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
        ('DecisionTree', LogisticRegression(max_iter=200)),
        ('SVC', LogisticRegression(max_iter=200))
    ]
    best_model = None
    best_score = 0
    for name, model in models:
        model.fit(X_train_features, y_train)
        y_pred = model.predict(X_train_features)
        score = accuracy_score(y_train, y_pred)
        if score > best_score:
            best_score = score
            best_model = model
    return best_model

def evaluate_model(model, X_test_features, y_test):
    """Evaluate the performance of the model on the test data."""
    y_pred = model.predict(X_test_features)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model: {model.__class__.__name__}")
    print(f"Accuracy: {accuracy:.2f}")
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

def main():
    file_path = "/content/spam_ham_dataset.csv"
    data = load_data(file_path)
    data = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(data)
    X_train_features, X_test_features = extract_features(X_train, X_test)
    model = train_model(X_train_features, y_train)
    evaluate_model(model, X_test_features, y_test)

if __name__ == "__main__":
    main()