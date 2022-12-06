#!/usr/bin/env python3
# Define global variables
input_file = "input_files/input_06.txt"

# PART I
with open(input_file) as input_txt:
    signal = input_txt.read()
    input_length = len(signal)
    while True:
        # Test if the first 4 characters contain a duplicate. Remove a character and try again if that is the case
        if len(signal[:4]) == len(set(signal[:4])):
            break
        else:
            signal = signal[1:]
    marker_found_at = input_length - len(signal) + 4
    print(f"First marker found after position {marker_found_at}")
