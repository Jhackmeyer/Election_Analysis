counties = ["Arapahoe", "Denver", "Jefferson"]

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for c in counties_dict:
    print(c)
    #same
for key in counties_dict.keys():
    print(key)

for val in counties_dict.values():
    print(val)
    #same
for name in counties_dict:
    print(counties_dict[name])
    #same
for county in counties_dict:
    print(counties_dict.get(county))
    #same
for county in counties_dict:
    print(counties_dict[county])


for county, val in counties_dict.items():
    print(county, "county has", val, "registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county in range(len(voting_data)):
    print(voting_data[county]["county"])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county, voters in counties_dict.items():
    print(f"{county} county has {val} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes=int(input("What is the total number of votes in the lection?"))
message_to_candidate=(
    f"you received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes/total_votes*100:.2f}% of the total votes")
print(message_to_candidate)


for county, val in counties_dict.items():
    print(f'{county} county has {val} registered voters.')

for x in range(len(voting_data)):
    print(voting_data[x]["county"], "county has", voting_data[x]["registered_voters"], "registered voters.")