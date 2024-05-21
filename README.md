Email Classification System
This project is an email classification system that categorizes emails as "spam" or "valid" based on various features, such as word frequencies, presence of spam keywords, and sender information. The system utilizes Support Vector Machines (SVM) to handle high-dimensional data often present in text classification tasks.

Table of Contents
Preprocessing
Training Data
Models
Deployment
<a name="preprocessing"></a>

Preprocessing
Explore the dataset: Basic information about each column is gathered, and numerical columns are described using functions like head(), tail(), and describe().
Handle missing values: Nulls are checked and manipulated by dropping cells containing nulls or replacing their value with the median (for numeric data) or mode (for categorical data).
Drop duplicated rows: Redundant data is removed by dropping duplicated rows.
Select features: Columns "label" and "label num" are compared, and the numerical column is kept. The final feature selection is the "Text" column.
<a name="training-data"></a>

Training Data
Convert text to numerical data: The TfidfVectorizer technique is applied to convert the "Text" column to numerical data using a mathematical equation that calculates the frequency of strange words divided by the total words.
Train the data: The data is prepared for different models by applying the TfidfVectorizer technique.
<a name="models"></a>

Models
Primary models: Logistic regression, Decision tree classifier, and SVM models are implemented.
Additional models: K-Nearest Neighbors (KNN) and Random Forest classifier models are added to test for different accuracies.
Model evaluation: Each model is applied to the features and target, and a classification report containing a confusion matrix is displayed to show precision and recall.
Cross-validation: K-fold cross-validation is used to evaluate the models, and overall accuracy for both train and test data is displayed for each model.
<a name="deployment"></a>

Deployment
GUI: The graphical user interface is created using HTML, CSS, and JavaScript for the frontend and Python Flask for the backend.
AI model integration: The AI model is ready to classify new entered text as spam or not spam.
User interaction: Users can select existing AI models, enter text, and see whether the text is spam or not spam. Users can also view the selected models' test accuracy and train accuracy.
