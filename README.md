# scikit-with-custom-dataset-as-csv
Using this Python Script, You can use your own CSV Dataset Easily for Machine Learning in Scikit Learn. Illustration is done using Decision Tree Classifier. Cleaveland Heart Disease Dataset has been used.

How this Works?

In this script, we first split the dataset into two. Features and Label. 
The example dataset has 13 features and one Label (The Predicted Value).
We load the datasets separately and convert it into a list. Then we pass this list to be predicted by the Classifier, here we have used the Decision tree Classifier from Scikit Learn.

How to use?

Split your dataset into features and labels.
Pass the input from the script and run the file.

CLEAVELAND HEART DISEASE DATASET

This dataset takes in 13 features and predicts the presence or absence of heart disease.

FEATURES:

features.csv

1. age: age in years 
2. sex: sex (1 = male; 0 = female) 
3. cp: chest pain type 

-- Value 1: typical angina 

-- Value 2: atypical angina 

-- Value 3: non-anginal pain 

-- Value 4: asymptomatic 

4. trestbps: resting blood pressure (in mm Hg on admission to the hospital) 

5. chol: serum cholestoral in mg/dl 
6. fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false) 
7. restecg: resting electrocardiographic results 

-- Value 0: normal 

-- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) 

-- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria 

8. thalach: maximum heart rate achieved 
9. exang: exercise induced angina (1 = yes; 0 = no) 
10. oldpeak = ST depression induced by exercise relative to rest 
11. slope: the slope of the peak exercise ST segment 

-- Value 1: upsloping 

-- Value 2: flat 

-- Value 3: downsloping 

12. ca: number of major vessels (0-3) colored by flourosopy
13. thal: 3 = normal; 6 = fixed defect; 7 = reversable defect 

LABEL:

label.csv

The Predicted Attribute
1. num: diagnosis of heart disease (angiographic disease status)

-- Value 0: < 50% diameter narrowing 

-- Value 1: > 50% diameter narrowing 

-- Value >1 : Severity of narrowing.

Dataset Archive : https://archive.ics.uci.edu/ml/datasets/Heart+Disease

Also Visit : https://www.neilspaul.com



