# import modules
import csv
from os import name

# path of the input file
PyPoll_input_file=r"PyPoll\Resources\election_data.csv"

# create an empty list for the list of candidates
candidates_list=[]

# create an empty list for all votes cast
votes_list=[]

# create an empty list for total votes cast for each candidate
candidates_votes=[]

# create an empty list for percentages of votes for each candidate
percentages_list=[]

# open the input file in a read mode
with open(PyPoll_input_file, 'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    # skip the header
    next(csvreader)

        # loop through the file
    for row in csvreader:

        # determine the total number of votes cast
        votes_list.append(row[2])
        total_votes_cast=int(len(votes_list))

        # detect the candidates receiving votes and append the list
        if row[2] not in candidates_list:
            candidates_list.append(row[2])

    # find the number of votes and their percentages for each candidate
    for x in candidates_list:
        candidates_votes.append(votes_list.count(x))
        percentages_list.append(votes_list.count(x)/total_votes_cast*100)
      
     # create a dictionary using candidate names as keys
final_list={candidates_list[i]: candidates_votes[i] for i in range(len(candidates_list))}

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
    for candidate, percentage, vote in zip(candidates_list, percentages_list, candidates_votes):
        analysis.write(f"\n{candidate}: {percentage:.3f}% ({vote})")
    analysis.write("\n----------------------------")
    analysis.write(f"\nWinner: {winner}")
    analysis.write("\n----------------------------")