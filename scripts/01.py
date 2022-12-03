#!/usr/bin/env python3
# Import packages
# Define functions
# Define global variables
input_file = "advent_of_code/input_01.txt"

# PART I
best_sum = 0
new_sum = 0
with open(input_file) as input_txt:
    for row in input_txt:
        if not row == "\n":
            new_sum += int(row)
        else:
            best_sum = max(best_sum, new_sum)
            new_sum = 0

    print(best_sum)
    input_txt.close()

# PART II
total = 0
cal_list = [0, 0, 0]
with open(input_file) as input_txt:
    for row in input_txt:
        if not row == "\n":
            total += int(row)
        else:
            if total > min(cal_list):
                cal_list.remove(min(cal_list))
                cal_list.append(total)
            total = 0
    input_txt.close()

final_total = sum(cal_list)
print(final_total)
