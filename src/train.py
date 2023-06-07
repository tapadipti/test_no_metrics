import json, os

METRICS_FILE = os.path.join("metrics_train.json")
metrics_dict = {"loss": 0.3043525516986847, "accuracy": 0.8895000219345093}


with open(METRICS_FILE, "w") as f:
    f.write(json.dumps(metrics_dict))
