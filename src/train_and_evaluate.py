import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,precision_score,recall_score
from sklearn.linear_model import LogisticRegression
from get_data import read_params
import argparse
import joblib
import json


def eval_metrics(actual, pred):
    accuracy = accuracy_score(actual, pred)
    precision = precision_score(actual, pred)
    recall = recall_score(actual, pred)
    return accuracy,precision,recall

def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]

    penalty = config["estimators"]["LogisticRegression"]["params"]["penalty"]
    solver = config["estimators"]["LogisticRegression"]["params"]["solver"]
    l1_ratio = config["estimators"]["LogisticRegression"]["params"]["l1_ratio"]

    target = [config["base"]["target_col"]]

    train = pd.read_csv(train_data_path)
    test = pd.read_csv(test_data_path)

    train_y = train[target]
    test_y = test[target]

    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

    lr = LogisticRegression(
        penalty=penalty,
        solver=solver, 
        l1_ratio=l1_ratio, 
        random_state=random_state)
    lr.fit(train_x, train_y)

    predicted_qualities = lr.predict(test_x)
    
    (accuracy,precision,recall) = eval_metrics(test_y, predicted_qualities)

    #print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (solver, l1_ratio))
    print("  ACCURACY: %s" % accuracy)
    print("  PRECISION: %s" % precision)
    print("  RECALL: %s" % recall)

#####################################################
    scores_file = config["reports"]["evaluation"]
    params_file = config["reports"]["params"]

    with open(scores_file, "w") as f:
        scores = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall
        }
        json.dump(scores, f, indent=4)

    with open(params_file, "w") as f:
        params = {
            "penalty": penalty,
            "solver": solver,
            "l1_ratio": l1_ratio,
        }
        json.dump(params, f, indent=4)
#####################################################


    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(lr, model_path)



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)


