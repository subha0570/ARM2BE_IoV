# Analysis/performance.py

import json
import os

FILE_NAME = "performance.json"

def save_time(operation, elapsed_time):

    data = {}

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as f:
            data = json.load(f)

    if operation not in data:
        data[operation] = []

    data[operation].append(elapsed_time)

    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)
