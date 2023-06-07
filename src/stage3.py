import json

# Data to be written
dictionary = {"loss": 0.4, "accuracy": 0.8}

# Serializing json
json_object = json.dumps(dictionary)

# Writing to sample.json
with open("stage3_metrics.json", "w") as outfile:
	outfile.write(json_object)

