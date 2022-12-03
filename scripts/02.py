#!/usr/bin/env python3
# Define global variables
input_file = "advent_of_code/input_02.txt"
win_list = ["A Y", "B Z", "C X"]
tie_list = ["A X", "B Y", "C Z"]
lose_list = ["A Z", "B X", "C Y"]
rpc_dict = {"X": 1, "Y": 2, "Z": 3}

# PART I
total_score = 0
with open(input_file) as input_txt:
    for row in input_txt:
        row = row.strip()
        shape = row[2]
        if row in lose_list:
            outcome_score = 0
        elif row in tie_list:
            outcome_score = 3
        elif row in win_list:
            outcome_score = 6
        else:
            print(f"IMPOSSIBRU: [{row}]")
        total_score += (rpc_dict[shape] + outcome_score)
    input_txt.close()
print(f"Total score: {total_score}")

# PART II
shape_dict = {"A": ["B", 1], "B": ["C", 2], "C": ["A", 3]}
total_score = 0
with open(input_file) as input_txt:
    for row in input_txt:
        row = row.strip()
        enemy_move = row[0]
        outcome = row[2]
        if outcome == "X":
            outcome_score = 0
            losing_move = [k for k, v in shape_dict.items() if v[0] == enemy_move][0]
            shape_score = shape_dict[losing_move][1]
        elif outcome == "Y":
            outcome_score = 3
            shape_score = shape_dict[enemy_move][1]
        elif outcome == "Z":
            outcome_score = 6
            winning_move = shape_dict[enemy_move][0]
            shape_score = shape_dict[winning_move][1]
        else:
            print(f"IMPOSSIBRU: [{row}]")
        total_score += (shape_score + outcome_score)
    input_txt.close()
print(f"Total score: {total_score}")
