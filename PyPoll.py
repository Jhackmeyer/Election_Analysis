# Add dependencies
import csv
import os

# Assign variable to load path
file_to_load=os.path.join("Election_Analysis\Resources\election_results.csv")
# Assign variable to save path
file_to_save=os.path.join("Election_Analysis\Analysis\election_analysis.txt")

# Initialize counter
total_votes = 0
candidate_options =[]

# open and read file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #read header row
    headers = next(file_reader)
    
    #print each row
    for row in file_reader:
        #Tally/aggregate votes
        total_votes += 1
        #Print names from rows
        candidate_name= row[2]
        #if the name is unique, ie does not repeat
        if candidate_name not in candidate_options:
            #add to list
            candidate_options.append(candidate_name)


print(total_votes)
print(candidate_options)

# 1 Total number of votes cast
# 2 A complete list of candidates who received votes
# 3 Total number of votes each candidate received
# 4 Percentage of votes each candidate won
# 5 The winner of the election based on popular vote

