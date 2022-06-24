import os
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from get_data import read_params
import argparse
import joblib
import json
import logging

# setting logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
file_handler = logging.FileHandler('./logs/train_and_evaluate.logs')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def eva_metrics(actual, pred):
    r2 = r2_score(actual,pred)
    mse = mean_squared_error(actual, pred)
    mae = mean_absolute_error(actual, pred)
    return r2,mse,mae

def train_and_evaluate(config_path):
    try: 
        config = read_params(config_path)
        test_data_path = config["split_data"]["test_path"]
        train_data_path = config["split_data"]["train_path"]
        random_state = config["base"]["random_state"]
        model_dir = config["model_dir"]
        scores_file = config["reports"]["scores"]
        params_file = config["reports"]["params"]

        n_estimators = config["estimators"]["RandomForestRegressor"]["params"]["n_estimators"]
        criterion = config["estimators"]["RandomForestRegressor"]["params"]["criterion"]
        max_depth = config["estimators"]["RandomForestRegressor"]["params"]["max_depth"]
        min_samples_split = config["estimators"]["RandomForestRegressor"]["params"]["min_samples_split"]

        target = config["base"]["target_col"]

        train = pd.read_csv(train_data_path)
        test = pd.read_csv(test_data_path)

        y_train = train[target]
        y_test = test[target]

        X_train = train.drop(target, axis=1)
        X_test = test.drop(target,axis=1)

        model = RandomForestRegressor(n_estimators=n_estimators, criterion=criterion, max_depth=max_depth, min_samples_split=min_samples_split, random_state=random_state)
        model.fit(X_train, y_train)

        y_preds = model.predict(X_test)
        (r2, mse, mae) = eva_metrics(y_test, y_preds)

        with open(scores_file,"w") as f:
            scores = {
                "r2_score": r2,
                "mean_squared_error": mse,
                "mean_absolute_error": mae
            }
            json.dump(scores, f, indent=4)

        with open(params_file, "w") as f:
            params ={
                "n_estimators": n_estimators,
                "criterion": criterion,
                "max_depth": max_depth,
                "min_samples_split": min_samples_split
            }
            json.dump(params, f, indent=4)

        model_path = os.path.join(model_dir, "model.joblib")
        joblib.dump(model, model_path)
        logger.info("train_and_evaluate funtion runs successfully")
    
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    try:
        args = argparse.ArgumentParser()
        args.add_argument("--config", default="params.yaml")
        parsed_args = args.parse_args()
        train_and_evaluate(config_path=parsed_args.config)
    except Exception as e:
        logger.error(e)
    