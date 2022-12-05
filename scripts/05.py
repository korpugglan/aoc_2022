#!/usr/bin/env python3
# Import packages
import numpy as np
import pandas as pd
import re


# Define functions
def get_container_names(input_string, container_size):
    value_list = [input_string[i] for i in range(1, len(input_string), container_size + 1)]
    value_series = pd.Series(value_list)
    return value_series


def move_containers(df_in, amount, origin, destination, crane_type):
    df_out = df_in.copy()
    if crane_type == "CrateMover 9000":
        for counter in range(0, amount):
            # Define the index to pick up the container at
            # If there is no container to move, stop the process
            if all(df_out[origin].isna()):
                break
            # Otherwise, pick the highest container with the lowest index
            else:
                orig_cont_index = df_out[df_out[origin].notna()].index.min()

            # Define the index to move the container to
            # If the stack is full, add an empty row and set it as the destination
            if all(df_out[destination].notna()):
                df_out.loc[df_out.index.min() - 1, :] = np.nan
                dest_cont_index = df_out.index.min()
                df_out.sort_index(inplace=True)
            # Otherwise, move it to the lowest possible spot
            else:
                dest_cont_index = df_out[df_out[destination].isna()].index.max()

            # Move the container to the new space and remove it from the old
            df_out.loc[dest_cont_index, destination] = df_out.loc[orig_cont_index, origin]
            df_out.loc[orig_cont_index, origin] = np.nan
    elif crane_type == "CrateMover 9001":
        # If there is no container to move, stop the process
        if all(df_out[origin].isna()):
            return df_out
        # The amount order is larger than the stack, take the maximum amount
        elif df_out[origin].notna().sum() < amount:
            amount = df_out[origin].notna().sum()
        # Define the range of crate to pick up
        orig_range_top = df_out[df_out[origin].notna()].index.min()
        orig_range_bottom = orig_range_top + amount - 1

        # Define the indices to move the containers to
        # If there isn't enough room to fill, create it
        if df_out[destination].isna().sum() < amount:
            missing_amount = amount - df_out[destination].isna().sum()
            missing_df = pd.DataFrame(np.nan,
                                      index=pd.Index(range(df_out.index.min() - missing_amount, df_out.index.min()),
                                                     dtype="Int64"),
                                      columns=list(df_out))
            df_out = pd.concat([missing_df, df_out])
            df_out.sort_index(inplace=True)
        # Define the range of crate drop off
        dest_range_bottom = df_out[df_out[destination].isna()].index.max()
        dest_range_top = dest_range_bottom - amount + 1

        # Move the containers to the new space and remove them from the old
        df_out.loc[dest_range_top:dest_range_bottom, destination] = \
            df_out.loc[orig_range_top:orig_range_bottom, origin].to_list()
        df_out.loc[orig_range_top:orig_range_bottom, origin] = np.nan
    else:
        print("ERROR: Unknown crane type")

    return df_out


# Define global variables
input_file = "input_files/input_05.txt"
input_df = pd.read_csv(input_file, header=None)
# crane_model = "CrateMover 9000"
crane_model = "CrateMover 9001"

# CREATE STACK DATAFRAME
stack_df = input_df[~input_df[0].str.startswith("move")].copy()
# Create a list of stack names based on lowest row
stack_list = re.split(r"\s+", stack_df.loc[stack_df.index.max(), 0].strip())
# Add the container values to the correct stack columns
stack_df[stack_list] = stack_df[0].apply(lambda x: get_container_names(x, 3))
# Clean the dataframe
stack_df = stack_df.loc[:stack_df.index.max() - 1, stack_list]
stack_df[stack_df == " "] = np.nan
# CREATE MOVES DATAFRAME
moves_df = input_df[input_df[0].str.startswith("move")].copy()
# Split moves into columns for readability
moves_df[["amount", "origin", "destination"]] = moves_df[0].apply(lambda x: pd.Series(re.findall(r"\s(\d+)\s?", x)))
moves_df["amount"] = moves_df["amount"].astype("Int64")

# PART I & II
for index, row in moves_df.iterrows():
    stack_df = move_containers(stack_df, row["amount"], row["origin"], row["destination"], crane_model)
stack_df.dropna(how="all", inplace=True)

result = "".join([stack_df.loc[stack_df[stack_df[col].notna()].index.min(), col] for col in list(stack_df)])
print(f"Result with {crane_model}: {result}")
