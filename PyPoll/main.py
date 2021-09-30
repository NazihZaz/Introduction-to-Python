# import modules
import csv
from os import name

# path of the input file
PyPoll_input_file=r"PyPoll\Resources\election_data.csv"

# create an empty list of the voter IDs
votes_cast_list=[]

# create an empty list for the list of candidates
candidate_list=[]

# create an empty list for the total votes cast for each candidate
all_votes=[]

# create an empty list for the percentages votes cast for each candidate
all_percentages=[]

# set intial value of total votes cast per candidate
Khan_votes=0
Correy_votes=0
Li_votes=0
OTooley_votes=0

# open the input file in a read mode
with open(PyPoll_input_file, 'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    # skip the header
    next(csvreader)

        # loop through the file
    for row in csvreader:

        # determine the total number of votes cast
        votes_cast_list.append(row[0])
        total_votes_cast=int(len(votes_cast_list))
        
        # detect the candidates receiving votes and append the list
        if row[2] not in candidate_list:
                candidate_list.append(row[2])
        
        # determine the total of votes cast for each candidate

        if row[2]=="Khan":
                Khan_votes+=1      
        elif row[2]=="Correy":
                Correy_votes+=1
        elif row[2]=="Li":
                Li_votes+=1
        elif row[2]=="O'Tooley":
                OTooley_votes+=1   

# calculate the percentage of votes each candidate won and insert it into all_percentages list
Khan_votes_percentage=round(Khan_votes/total_votes_cast*100,3)
Correy_votes_percentage=round(Correy_votes/total_votes_cast*100,3)
Li_votes_percentage=round(Li_votes/total_votes_cast*100,3)
OTooley_votes_percentage=round(OTooley_votes/total_votes_cast*100,3)

all_percentages.insert(0, Khan_votes_percentage)
all_percentages.insert(1, Correy_votes_percentage)
all_percentages.insert(2, Li_votes_percentage)
all_percentages.insert(3, OTooley_votes_percentage)

# insert all the total votes cast for each candidate into all_votes list        
all_votes.insert(0, Khan_votes)
all_votes.insert(1, Correy_votes)
all_votes.insert(2, Li_votes)
all_votes.insert(3, OTooley_votes)

# create a dictionary using candidate names as keys
final_list={candidate_list[i]: all_votes[i] for i in range(len(candidate_list))}

# find the election winner
winner=max(final_list, key=final_list.get)

# path of the output file
PyPoll_output_file=r"PyPoll\Analysis\PyPoll Analysis.txt"

# open the output file in write mode
with open(PyPoll_output_file,'w') as analysis:

        # write the results on the output file
        analysis.write("Election Results")
        analysis.write("\n----------------------------")
        analysis.write(f"\nTotal Votes: {total_votes_cast}")
        analysis.write("\n----------------------------")
        for x in range(len(candidate_list)):
                analysis.write(f"\n{candidate_list[x]}: {all_percentages[x]}% ({all_votes[x]})")
        analysis.write("\n----------------------------")
        analysis.write(f"\nWinner: {winner}")
        analysis.write("\n----------------------------")

