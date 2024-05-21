# Email Classification System
This project is an email classification system that categorizes emails as "spam" or "valid" based on various features, such as word frequencies, presence of spam keywords, and sender information. The system utilizes Support Vector Machines (SVM) to handle high-dimensional data often present in text classification tasks.

## Table of Contents <br/>
1.  Preprocessing <br/>
2.  Training Data <br/>
3.  Models <br/>
4.  Deployment
<a name="preprocessing"></a>

## Preprocessing
1. **Explore the dataset:** Basic information about each column is gathered, and numerical columns are described using functions like head(), tail(), and describe(). <br/>
2. **Handle missing values:** Nulls are checked and manipulated by dropping cells containing nulls or replacing their value with the median (for numeric data) or mode (for categorical data). <br/>
3. **Drop duplicated rows:** Redundant data is removed by dropping duplicated rows. <br/>
4. **Select features: Columns** "label" and "label num" are compared, and the numerical column is kept. The final feature selection is the "Text" column. <br/>
<a name="training-data"></a>

## Training Data
1. **Convert text to numerical data:** The TfidfVectorizer technique is applied to convert the "Text" column to numerical data using a mathematical equation that calculates the frequency of strange words divided by the total words. <br/>
2. **Train the data:** The data is prepared for different models by applying the TfidfVectorizer technique.
<a name="models"></a>

## Models
1. **Primary models:** Logistic regression, Decision tree classifier, and SVM models are implemented. <br/>
2. **Additional models:** K-Nearest Neighbors (KNN) and Random Forest classifier models are added to test for different accuracies. <br/>
3. **Model evaluation:** Each model is applied to the features and target, and a classification report containing a confusion matrix is displayed to show precision and recall. <br/>
4. **Cross-validation:** K-fold cross-validation is used to evaluate the models, and overall accuracy for both train and test data is displayed for each model.
<a name="deployment"></a>

## Deployment
1. **GUI:** The graphical user interface is created using HTML, CSS, and JavaScript for the frontend and Python Flask for the backend. <br/>
2. **AI model integration:** The AI model is ready to classify new entered text as spam or not spam. <br/>
3. **User interaction:** Users can select existing AI models, enter text, and see whether the text is spam or not spam. Users can also view the selected models' test accuracy and train accuracy.
You can find the source code and documentation for this project in this repository. To get started, follow these steps:

## Prerequisites
* Python 3.x <br/>
* Required libraries: NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn, Flask
