import numpy as np
import pandas as pd
import json
import csv


def flatten_data(data, category):
    result = []
    for obj in data:  
        intent = obj["intent"]
        for question in obj["patterns"]:
            resultObj = {"intent" : intent, "question" : question, "category" : category}
            result.append(resultObj)
    return result

output = []
with open('data/deepfake_dataset.json', 'r') as file:
    data = json.load(file)
    output.extend(flatten_data(data, "deepfake"))

with open('data/general_data.json', 'r') as file:
    data = json.load(file)
    output.extend(flatten_data(data, "general"))

with open('data/malware_dataset.json', 'r') as file:
    data = json.load(file)
    output.extend(flatten_data(data, "malware"))

with open('data/phishing_emails_dataset.json', 'r') as file:
    data = json.load(file)
    output.extend(flatten_data(data, "phishing"))


with open('data/processed/cyber_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['intent', 'question', 'category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(output)