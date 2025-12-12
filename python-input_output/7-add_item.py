#!/usr/bin/python3
"""This module will load, add, and save args to file"""
from sys import argv
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
save_to_json_file(argv, 'add_item.json')
load_from_json_file('add_item.json')
