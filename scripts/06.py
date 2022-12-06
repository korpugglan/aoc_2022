#!/usr/bin/env python3
# Import packages

# Define global variables
input_file = "input_files/input_06.txt"

# PART I
with open(input_file) as input_txt:
    for row in input_txt:
        row = row.strip()