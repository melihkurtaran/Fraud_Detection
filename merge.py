import os
import pandas as pd

# Set the path to the directory containing the CSV files
dir_path = "dataset/"

# Get a list of all the CSV files in the directory
csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]

# Create an empty list to hold the dataframes
dfs = []

# Loop through the CSV files, read each one into a dataframe, and append it to the list
for csv_file in csv_files:
    file_path = os.path.join(dir_path, csv_file)
    df = pd.read_csv(file_path,delimiter=';')
    dfs.append(df)

# Concatenate all the dataframes in the list into a single dataframe
merged_df = pd.concat(dfs)

# Save the merged dataframe as a CSV file
merged_df.to_csv(os.path.join(dir_path, 'merged.csv'), index=False)
