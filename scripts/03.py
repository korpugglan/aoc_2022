#!/usr/bin/env python3
# Import packages
import string

# Define global variables
input_file = "input_files/input_03.txt"

letter_keys = [x for x in string.ascii_letters]
number_values = [x for x in range(1, 53)]
prio_dict = dict(zip(letter_keys, number_values))

# PART I
prio_sum = 0
with open(input_file) as input_txt:
    for row in input_txt:
        row = row.strip()
        section_1 = row[:int(len(row)/2)]
        section_2 = row[int(len(row)/2):]
        for item in section_1:
            if item in section_2:
                prio_sum += prio_dict[item]
                break
    print(f"SUM OF PRIORITY SCORE: {prio_sum}")


