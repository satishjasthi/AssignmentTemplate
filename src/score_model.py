"""
Script to score the model performance
based on 
- Accuracy 
- f1 score

Author: Satish Jasthi
"""
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

accuracy_score_map = {(0, 30): 5, (30, 60): 10, (60, 90): 12, (90, 100): 20}
f1_score_map = {(0.0, 0.30): 5, (0.30, 0.60): 10, (0.60, 0.90): 12, (0.90, 0.100): 20}


def get_score(metric_value: float, metric_name: str):
    """
    get score based on metric value and name
    """
    if metric_name == "accuracy":
        metric_map = accuracy_score_map
    elif metric_name == "f1_score":
        metric_map = f1_score_map
    else:
        raise NotImplementedError
    for value_range, score in metric_map.items():
        min_value, max_value = value_range
        if metric_value >= min_value and metric_value < max_value:
            return score
    return 0


def evaluate_model(predictions_fname: str):
    """
    Function to score the model
    """
    pred_data = pd.read_csv(predictions_fname)
    y_true = pred_data["label"]
    y_pred = pred_data["prediction"]

    # calculate accuracy
    acc = accuracy_score(y_true, y_pred)
    f1_scr = f1_score(y_true, y_pred)

    # get score based on metric value
    acc_score = get_score(metric_value=acc, metric_name="accuracy")
    f1_m_score = get_score(metric_value=f1_scr, metric_name="f1_score")
    return acc_score + f1_m_score


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Score model based on test data performance"
    )
    parser.add_argument(
        "predictions_fname", type=str, help="Path to the predictions data csv file"
    )
    args = parser.parse_args()

    # test model
    final_score = evaluate_model(args.predictions_fname)
    print(f"Final score: {final_score}")
