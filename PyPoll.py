# import modules
import csv
import os

# turn data path into filename variable
file_to_load=os.path.join("Election_Analysis\Resources\election_results.csv")

# turn destination into filenam evariable
file_to_save=os.path.join("Election_Analysis\Analysis\election_analysis.txt")
# open as text file
outfile = open(file_to_save, "w")
# write in file
outfile.write("Hello world 1")
# close file
outfile.close()

with open(file_to_save, "w") as outfile:
    outfile.write("Counties in the election\n")
    outfile.write("------------------\n")
    outfile.write("Arapahoe\nDenver\nJefferson")
#    outfile.write("Denver, ")
 #   outfile.write("Jefferson")


# 1 Total number of votes cast
# 2 A complete list of candidates who received votes
# 3 Total number of votes each candidate received
# 4 Percentage of votes each candidate won
# 5 The winner of the election based on popular vote

