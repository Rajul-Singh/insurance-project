# read params
# process
# return dataframe
from inspect import ArgSpec
import os
import yaml
import pandas as pd
import argparse
import logging

# setting logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
file_handler = logging.FileHandler('./logs/get_data.logs')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def read_params(config_path):
    try:
        with open(config_path) as f:
            config = yaml.safe_load(f)
            logger.info("read_params function runs successfully")
            return config
    except Exception as e:
        logger.error(e)


def get_data(config_path):
    try:
        config = read_params(config_path)
        data_path = config['data_source']['s3_source']
        df = pd.read_csv(data_path)
        logger.info("get_data function runs successfully")
        return df
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    try:
        args = argparse.ArgumentParser()
        args.add_argument("--config", default="params.yaml")
        parsed_args = args.parse_args()
        logger.info("No errors in get_data.py")
        data = get_data(config_path=parsed_args.config)
    except Exception as e:
        logger.error(e)