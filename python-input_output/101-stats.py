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
        last_part = line.split()
        status = last_part[-2]
        size = last_part[-1]
        total_size += int(size)
        if status in status_codes:
            status_counts[status] = status_counts.get(status, 0) + 1
        if line_count % 10 == 0:
            print("File size:", total_size)
            for key in sorted(status_counts.keys()):
                if status_counts[key] > 0:
                    print(f'{key}: {status_counts[key]}')
except KeyboardInterrupt:
    print("File size:", total_size)
    for key in sorted(status_counts.keys()):
        if status_counts[key] > 0:
            print(f'{key}: {status_counts[key]}')
