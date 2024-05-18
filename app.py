# imports
import numpy as np
from flask import Flask, request, render_template, jsonify
import json
import pickle

app = Flask(__name__)

# Load the feature extractor and models
featureExtractor = pickle.load(open('models/featureExtractionVectorizer.pkl', 'rb'))
model = pickle.load(open('models/LogisticRegression.pkl', 'rb'))

# Load valid and spam arrays
try:
    valid = pickle.load(open('valid.pkl', 'rb'))
    spam = pickle.load(open('spam.pkl', 'rb'))
    accuracies = pickle.load(open('accuracies.pkl', 'rb'))
except:
    valid = []
    spam = []
    accuracies = []


# home menu
@app.route('/')
def home():
    model
    pickle.dump(valid, open('valid.pkl', 'wb'))
    pickle.dump(spam, open('spam.pkl', 'wb'))
    return render_template('index.html', valid=valid, spam=spam, usedModel=model)


# predict results
@app.route('/predict',methods=['POST'])
def predict():
    global model
    global accuracyTrain
    global accuracyTest
    try:
        form_values = list(request.form.values())
        str_features = [str(x) for x in form_values]
        concatenated_string = "\n".join([s for s in str_features])
        str_features.clear()
        str_features.append(concatenated_string)
        features = featureExtractor.transform(str_features)
        prediction = model.predict(features)
        result = prediction[0]
        if result == 0:
            valid.append(concatenated_string)
        else:
            spam.append(concatenated_string)
        print(model)

        pickle.dump(valid, open('valid.pkl', 'wb'))
        pickle.dump(spam, open('spam.pkl', 'wb'))
        print(str(accuracyTest) + " " + str(accuracyTrain))
        return render_template('index.html', prediction=result, usedModel=model, valid=valid, spam=spam, accuracyTest=accuracyTest, accuracyTrain=accuracyTrain)
    except:
        print()
        return render_template('index.html')

# model selection
@app.route('/select',methods=['POST'])
def select():
    global model
    global accuracyTrain
    global accuracyTest
    form_values = list(request.form.values())
    if form_values[0] == "DecisionTreeClassifier()":
        model = pickle.load(open('models/DecisionTreeClassifier.pkl', 'rb'))
        accuracyTest, accuracyTrain = accuracies["DecisionTreeClassifier"][0], accuracies["DecisionTreeClassifier"][1]
    elif form_values[0] == "SVC(kernel='linear')":
        model = pickle.load(open('models/SVC.pkl', 'rb'))
        accuracyTest, accuracyTrain = accuracies["SVC"][0], accuracies["SVC"][1]
    elif form_values[0] == "RandomForestClassifier(random_state=42)":
        model = pickle.load(open('models/RandomForestClassifier.pkl', 'rb'))
        accuracyTest, accuracyTrain = accuracies["RandomForestClassifier"][0], accuracies["RandomForestClassifier"][1]
    elif form_values[0] == "KNeighborsClassifier()":
        model = pickle.load(open('models/KNeighborsClassifier.pkl', 'rb'))
        accuracyTest, accuracyTrain = accuracies["KNeighborsClassifier"][0], accuracies["KNeighborsClassifier"][1]
    else:
        model = pickle.load(open('models/LogisticRegression.pkl', 'rb'))        
        accuracyTest, accuracyTrain = accuracies["LogisticRegression"][0], accuracies["LogisticRegression"][1]

    accuracyTest = "Test Accuracy :  " + str(round(accuracyTest, 4)*100) + "%"
    accuracyTrain = "Train Accuracy :  " + str(round(accuracyTrain, 4)*100) + "%"
    print(str(accuracyTest) + " " + str(accuracyTrain))


    pickle.dump(valid, open('valid.pkl', 'wb'))
    pickle.dump(spam, open('spam.pkl', 'wb'))
    return render_template('index.html', usedModel=form_values[0], vaild=valid, spam=spam)

if __name__ == "__main__":
    app.run(debug=True)