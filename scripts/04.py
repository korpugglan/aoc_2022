#!/usr/bin/env python3
# Import packages

# Define global variables
input_file = "input_files/input_04.txt"

# PART I
full_overlap_count = 0
with open(input_file) as input_txt:
    for row in input_txt:
        row = row.strip()
        range_pair = [int(x) for x in row.replace("-", ",").split(",")]
        # If the starting or ending numbers of the ranges are the same, there is full overlap
        if range_pair[0] == range_pair[2] or range_pair[1] == range_pair[3]:
            full_overlap_count += 1
        # If the left range is larger than the right range or vice versa, there is full overlap
        elif (range_pair[0] < range_pair[2] and range_pair[1] > range_pair[3]) or \
                (range_pair[0] > range_pair[2] and range_pair[1] < range_pair[3]):
            full_overlap_count += 1
        else:
            continue
    print(f"NUMBER OF FULL OVERLAP RANGES: {full_overlap_count}")

# PART II
partial_overlap_count = 0
with open(input_file) as input_txt:
    for row in input_txt:
        row = row.strip()
        range_pair = [int(x) for x in row.replace("-", ",").split(",")]
        # If numbers match between the ranges, there is overlap
        if any(x in range_pair[2:] for x in range_pair[:2]):
            partial_overlap_count += 1
        # If either starting number falls within the other range, there is overlap
        elif range_pair[2] < range_pair[0] < range_pair[3] or range_pair[0] < range_pair[2] < range_pair[1]:
            partial_overlap_count += 1
        else:
            continue
    print(f"NUMBER OF PARTIAL OVERLAP RANGES: {partial_overlap_count}")
