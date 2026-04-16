import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def read_data(file_name='data/7817_1.csv'):
    logging.info("Reading data from file...")
    data = pd.read_csv(file_name)
    logging.info("Completed reading data....")
    return data

def clean_data(data):
    logging.info("Cleaning data...")
    reviews = data['reviews.text'].dropna().tolist()
    logging.info("Completed cleaning data....")
    return reviews
