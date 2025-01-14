# Heart Stroke Prediction App

## Description
This project is an end-to-end machine learning application for predicting the likelihood of a heart stroke based on user-provided inputs. The application uses a trained Decision Tree model to make predictions and is built using Python, Streamlit, and other libraries.

## Features
- User-friendly interface for inputting data.
- Predicts the likelihood of a heart stroke.
- Displays the result in real time.
- Built using a Decision Tree model trained on a balanced dataset.

## Tech Stack
- **Programming Language:** Python
- **Framework:** Streamlit
- **Machine Learning Libraries:** scikit-learn
- **Python Libraries:** pandas, numpy, matplotlib 

## Dataset
- Dataset Source: [Kaggle - Heart Stroke Prediction Dataset](https://www.kaggle.com/datasets/godfatherfigure/healthcare-dataset-stroke-data)
- Features: Age, Gender, BMI, Smoking Status, Hypertension, etc.
- Target: Stroke (1 = Yes, 0 = No)
- Preprocessing: Applied SMOTE to handle class imbalance.

## Model Details
- Models Trained: Logistic Regression, Decision Tree, Random Forest, SVM
- Best Model: Decision Tree
- Performance Metrics: Accuracy, Precision, Recall
- Additional Processing: Applied SMOTE for balancing the dataset.

## Steps I followed:
- Data Loadimg and cleaning
- Exploratory Data Analysis(EDA) on the dataset
- Feature Engineering: Encoded categorical features using OHE
- Feature Selection: Removed unwanted features such as ID
- Decision Tree was trained on the dataset
- Applied SMOTE technique to address class imbalance
- Performed Hyperparameter Tuning to optimize the model
- The final model was loaded into a file using pickle
- An user interface is created using streamlit framework where user gives input for various features and get prediction as output

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Neelakanta3144/Heart-Stroke-Prediction.git
```

2. Navigate to the project directory:
```bash
cd heart-stroke-prediction
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```


## Usage
1. Open the app in your browser (http://localhost:8501).
2. Enter the required details, such as age, BMI, etc.
3. Click the "Predict" button to get the result.

## Screenshots
![Home Page](https://github.com/Neelakanta3144/Heart-Stroke-Prediction/blob/main/Outputs/Screenshot1.png)
![Prediction Page](https://github.com/Neelakanta3144/Heart-Stroke-Prediction/blob/main/Outputs/Screenshot2.png)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Dataset from Kaggle
- Streamlit documentation
- scikit-learn library
