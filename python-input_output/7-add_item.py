#!/usr/bin/python3
"""This module will load, add, and save args to file"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    load_from_json_file('add_item.json')
    save_to_json_file(argv[1:], 'add_item.json')
except Exception:
    save_to_json_file(argv[1:], 'add_item.json')
