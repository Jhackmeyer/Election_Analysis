# import modules
import csv
import os

# turn data path into filename variable
file_to_load=os.path.join("Election_Analysis\Resources\election_results.csv")
# turn destination into filename variable
file_to_save=os.path.join("Election_Analysis\Analysis\election_analysis.txt")

# open and read file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #read and print header row
    headers = next(file_reader)
    print(headers)


# 1 Total number of votes cast
# 2 A complete list of candidates who received votes
# 3 Total number of votes each candidate received
# 4 Percentage of votes each candidate won
# 5 The winner of the election based on popular vote

