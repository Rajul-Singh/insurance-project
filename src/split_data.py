from inspect import ArgInfo
import os
import argparse
from posixpath import split
from random import random
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params
import logging

# setting logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
file_handler = logging.FileHandler('./logs/split_data.logs')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def split_and_save_data(config_path):
    try:
        config = read_params(config_path)
        test_data_path = config["split_data"]["test_path"]
        train_data_path = config["split_data"]["train_path"]
        raw_data_path = config["load_data"]["raw_dataset_csv"]
        test_ratio = config["split_data"]["test_size"]
        random_state = config["base"]["random_state"]

        df = pd.read_csv(raw_data_path)
        train, test = train_test_split(df, test_size=test_ratio, random_state=random_state)

        train.to_csv(train_data_path, index=False)
        test.to_csv(test_data_path, index=False)
        logger.info("split_and_save_data function runs successfully")
    
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    try:
        args = argparse.ArgumentParser()
        args.add_argument("--config", default="params.yaml")
        parsed_args = args.parse_args()
        split_and_save_data(config_path=parsed_args.config)
        logger.info("split_data.py file runs successfully")
    except Exception as e:
        logger.error(e)