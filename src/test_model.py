"""
Script to test the trained model on test data

usage: python test_model.py path/test_data.csv

Author: Satish Jasthi
"""
import sys
from pathlib import Path
import pandas as pd
from random import choice
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_trained_model():
  """
  Function to load trained model
  """
  ## Fill up code here to load your model ##
  return lambda x: choice([0,1])


def test_model(test_data_fname:str):
  """
  function to test the model on the test data
  
  test_data_fname(str): path to test data csv file
  """
  trained_model = load_trained_model()
  test_df = pd.read_csv(test_data_fname)
  predictions = []
  for _, row in test_df.iterrows():
    predictions.append(trained_model(row['feature']))
  test_df['prediction'] = predictions
  test_df.to_csv(PROJECT_ROOT/'Predictions.csv', index=False)


if __name__=="__main__":
  import argparse
  parser = argparse.ArgumentParser(description='Test model on test data')
  parser.add_argument('test_data_fname', type=str,
                    help='Path to the test data csv file')
  args = parser.parse_args()

  # test model
  test_model(args.test_data_fname)