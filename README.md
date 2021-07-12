# Election_Analysis
Analysis using Python and other tools

## Overview of Election Audit:
Here, we use Python and VS Code to automate the analysis and audit of a Colorado election.  The goal here includes reporting on the election results, but making sure the code itself is versatile enough to process any election data

## Election-Audit Results
- There were a total of 369,711 votes cast in this election
- A breakdown of the percentage and count of votes for each *county*:

  **Jefferson** made up 10.5% of votes (38,855)

  **Denver** made up 82.8% of votes (306,055)

  **Arapahoe** made up 6.7% of votes (24,801) 
- **Denver** had the largest voter turnout
- A breakdown of the percentage and count of votes for each *candidate*:

  **Charles Casper Stockham** took 23.0% of the votes (85,213)
  
  **Diana DeGette** took 73.8% of the votes (272,892)

  **Raymon Anthony Doane** took 3.1% of the votes (11,606)
- The winner of the election was **Diana DeGette** with 272,892 votes, or 73.8% of the total votes.

## Election-Audit Summary:
This script is general enough to apply to any election, as long as the script knows where to pull the data from and where to print its results to.  The file pathways in the following code will have to be updated to fit the new data file and analysis file.
```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Election_Analysis\Resources\election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("Election_Analysis\Analysis\election_analysis.txt")
```

If the data is formatted differently from the file provided, the script may also need to be edited accordingly to ensure that the candidate names and country names are being pulled from the correct columns.  The following code will scan through the 3rd column for candidate names and the 2nd column for county names.  Make sure either the data file is consistent with this, or the code itself is updated to direct the script to the correct columns.
```
  # Get the candidate name from each row.
  candidate_name = row[2]
  # 3: Extract the county name from each row.
  county_name = row[1]
```

