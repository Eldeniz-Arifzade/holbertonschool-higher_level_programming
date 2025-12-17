#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(filename):
    try:
        with open(filename, 'r') as file:
            with open('data.json', 'w') as data:
                data.write(list(csv.DictReader(file)))
                return True
    except Exception:
        return False
