# Add dependencies
import csv
import os

# Assign variable to load path
file_to_load=os.path.join("Election_Analysis\Resources\election_results.csv")
# Assign variable to save path
file_to_save=os.path.join("Election_Analysis\Analysis\election_analysis.txt")

# Initialize vote counter, candidates, and vote dictionary
total_votes = 0
candidate_options =[]
candidate_votes= {}
# Declare winning variables
winning_candidate=""
winning_count = 0
winning_percentage = 0

# Open and read file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    # Read header row
    headers = next(file_reader)
    
    # Print each row
    for row in file_reader:
        # Tally/aggregate votes
        total_votes += 1
        # Print names from rows
        candidate_name= row[2]
        # If the name is unique, ie does not repeat
        if candidate_name not in candidate_options:
            # Add to list
            candidate_options.append(candidate_name)

            # Track vote counts
            candidate_votes[candidate_name] = 0

        # Tally/aggregate votes
        candidate_votes[candidate_name] += 1
        
    print('\n')       
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percent = float(votes)/float(total_votes)*100
        print(f'{candidate_name}: {vote_percent:.1f}% ({votes})\n')

        # If variables are the max
        if(votes > winning_count) and (vote_percent > winning_percentage):
            # Keep variables as winning variables
            winning_count=votes
            winning_percentage=vote_percent
            winning_candidate=candidate_name
    winning_candidate_summary=(
        f'========================\n'
        f'Winner: {winning_candidate}\n'
        f'Winning vote percent: {winning_percentage:.1f}%\n'
        f'Winning vote count: {winning_count}\n'
        f'========================\n')



# 1 Total number of votes cast
print(f'========================\n')
print(total_votes)
# 2 A complete list of candidates who received votes
print(f'========================\n')
print(candidate_options)
# 3 Total number of votes each candidate received
print(f'========================\n')
print(candidate_votes)
# 4 Percentage of votes each candidate won
print(f'========================\n')
for candidate_name in candidate_votes:
    print(f'{candidate_name}: {vote_percent:.1f}% \n')
# 5 The winner of the election based on popular vote
print(winning_candidate_summary)