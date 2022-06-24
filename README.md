## Insurance_internshipProject

### Problem Statement: <br>
The goal of this project is to give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind. This can assist a person in concentrating on the health side of an insurance policy rather han the ineffective part.

### Approach: <br>
The classical machine learning tasks like Data Exploration, Data Cleaning, Feature Engineering, Model Building and Model Testing. Try out different machine learning algorithms that’s best fit for the above case.
<b>Some Famous Algorithms</b>: - Multiple Linear Regression, Decision tree Regression and Gradient Boosting, Adaboost Regressor, RandomForestRegression and Elasticnet.

### Result: <br>
We have build a solution that should able to predict the amount of health insurance.

[Application Link](https://insurance7042.herokuapp.com/)

###### Follow the steps after making github repository and cloning in the working folder.

### STEPS ARE MENTIONED BELOW FOR MAKING THE ENTIRE PIPELINE

Step 1:- Create env
```bash
conda create -n insurance python=3.7 -y
```
Step 2:- Activate env
```bash
conda activate insurance
```
Step 6:- Download dataset :- [insurance](https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction)

Step 7:- Creat template for project
```bash
code present in template.py
```
Step 8:- Initialize dvc
```bash
dvc init
``` 

Step 9:- Add data into dvc for tracking
```bash
dvc add data_given/dataname.csv
```

Step 10:- Add all the file to github
```bash
git add -A
git commit -m "first commit"
git push -u origin main
```

Step 11:- Create ```params.yaml``` and ```dvc.yaml```
<b>params.yaml</b> and <b>dvc.yaml</b> both very important file for the project.

Step 12:- Start working in src directory and for load data and train model
```bash
get_data.py
load_data.py
split_data.py
train_and_evaluate.py
```

Step 13:- After finish model building now time to create webapp:- <br>
```bash
In webapp folder we have templates of the webpage and for styling we used bootstrap and css. CSS available in static folder.
```

Step 14:- 
```app.py``` on root dir for creating flask api
Now make routes like `\` for rendering home page and `/predict` for rendering predictions.

step 15:
For automation of the project create dir `.github\workflow\ci-cd.yaml` we used here github actions for automating our project.

<br>
Author: Abhishek Kumar
<br>
For any queries related to ml/dl contact me <a href="mailto:abhiprasad7042@gmail.com?subject = Feedback&body = Message">abhiprasad7042@gmail.com</a>
<br>

## Thank You

