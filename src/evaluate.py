import json

# Data to be written
dictionary = {"loss": 0.3043525516986847, "accuracy": 0.8895000219345093}

# Serializing json
json_object = json.dumps(dictionary)

# Writing to sample.json
with open("metrics.json", "w") as outfile:
	outfile.write(json_object)

