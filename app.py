import numpy as np
from flask import Flask, request, render_template, jsonify
import json
import pickle

app = Flask(__name__)

featureExtractor = pickle.load(open('models/featureExtractionVectorizer.pkl', 'rb'))
valid = []
spam = []

@app.route('/')
def home():
    return render_template('index.html', valid=valid, spam=spam)

@app.route('/predict',methods=['POST'])
def predict():
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
        return render_template('index.html', prediction=result, usedModel=model, valid=valid, spam=spam)
    except:
        print()
        return render_template('index.html')

@app.route('/select',methods=['POST'])
def select():
    global model
    form_values = list(request.form.values())
    if form_values[0] == "DecisionTreeClassifier()":
        model = pickle.load(open('models/DecisionTreeClassifier.pkl', 'rb'))
    elif form_values[0] == "SVC(kernel='linear')":
        model = pickle.load(open('models/SVC.pkl', 'rb'))
    elif form_values[0] == "MultinomialNB()":
        model = pickle.load(open('models/MultinomialNB.pkl', 'rb'))
    elif form_values[0] == "RandomForestClassifier(random_state=42)":
        model = pickle.load(open('models/RandomForestClassifier.pkl', 'rb'))
    elif form_values[0] == "KNeighborsClassifier()":
        model = pickle.load(open('models/KNeighborsClassifier.pkl', 'rb'))
    else:
        model = pickle.load(open('models/LogisticRegression.pkl', 'rb'))

    return render_template('index.html', usedModel=form_values[0], vaild=valid, spam=spam)

if __name__ == "__main__":
    app.run(debug=True)