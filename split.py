# Author: Melih Kurtaran
# Splits datasets into smaller csvs to upload GitHub

import csv

# Input CSV file name
filename = 'input.csv'

# Output CSV file names
output_filename_1 = 'realTransactions_2013Sep_sp_1.csv'
output_filename_2 = 'realTransactions_2013Sep_sp_2.csv'

# Number of rows to include in each split
split_size = 150000

# Open the input file for reading
with open(filename, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)

    # Read the headers
    headers = next(reader)

    # Open the output files for writing
    with open(output_filename_1, 'w', newline='') as outfile1, \
         open(output_filename_2, 'w', newline='') as outfile2:

        # Write the headers to both output files
        writer1 = csv.writer(outfile1)
        writer1.writerow(headers)
        writer2 = csv.writer(outfile2)
        writer2.writerow(headers)

        # Write rows to each output file in turn
        for i, row in enumerate(reader):
            if i < split_size:
                writer1.writerow(row)
            else:
                writer2.writerow(row)

