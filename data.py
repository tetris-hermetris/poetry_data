import json
from datetime import datetime


def getData(dataset):
    with open(f"data/{dataset}.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    for publication in data:
        date = publication["date"]
        publication["date"] = datetime.fromisoformat(publication["date"])
    return data
