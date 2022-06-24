import os
from get_data import read_params, get_data
import argparse
import logging

# setting logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
file_handler = logging.FileHandler('./logs/load_data.logs')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def load_save(config_path):
    try:
        config = read_params(config_path)
        df = get_data(config_path)
        raw_data_path = config["load_data"]["raw_dataset_csv"]
        # converting categorical data into numerical data
        df["sex"] = df["sex"].map({"female":0, "male":1})
        df["smoker"] = df["smoker"].map({"yes":1,"no":0})
        df["region"] = df["region"].map({"southeast":0, "southwest":1, "northwest":2, "northeast":3})
        df.to_csv(raw_data_path, index=False)
        logger.info("load_save function runs successfully")
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    try:
        args = argparse.ArgumentParser()
        args.add_argument("--config", default="params.yaml") 
        parsed_args = args.parse_args()
        load_save(config_path=parsed_args.config)
        logger.info("No error in load_data.py")
    except Exception as e:
        logger.error(e)

