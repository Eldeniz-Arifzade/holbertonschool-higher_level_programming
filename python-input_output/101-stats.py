#!/usr/bin/python3
"""This module will parse the input entered to stdin line by line"""
import sys


total_size = 0
status_counts = {}
line_count = 0
status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
try:
    for line in sys.stdin:
        line_count += 1
        status, size = line.split()[-2, -1]
        total_size += size
        if status in status_codes:
            status_counts[status] += 1
        if line_count % 10 == 0:
            print("File size:", total_size)
            for key, value in status_counts.items():
                print(f'{key}: {value}')
except KeyboardInterrupt:
    print("File size:", total_size)
    for key, value in status_counts.items():
    print(f'{key}: {value}')
