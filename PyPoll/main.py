#import os module
import os
#read csv file
import csv

election_data = os.path.join('Resources','election_data.csv')

txt_path = "Election_Analysis.txt"

#declaring variables
Total_Votes = 0
Election_candidates = []
Candidate_votes = {}
Vote_Count = 0
Election_winner = ""

#Open csv
with open(election_data) as csvfile:
    csvreader = csv.DictReader(csvfile)


    #start loop to find answers
    for row in csvreader:
        Total_Votes += 1
        Candidate = row["Candidate"]
        
        #finding unique candidates
        if Candidate not in Election_candidates:
            Election_candidates.append(Candidate)
            Candidate_votes[Candidate] = 1
        Candidate_votes[Candidate] = Candidate_votes[Candidate] + 1

    for Candidate in Candidate_votes:
        vote = Candidate_votes[Candidate]
        percent_vote = float(vote)/float(Total_Votes)*100
        if (vote > Vote_Count):
            Vote_Count = vote
            Election_winner= Candidate
        Output = (f"{Candidate}: {percent_vote: .3f}% ({vote})/n")
        print(Output)
        
    Winner = (f"Winner: {Election_winner}")
    print(Winner)

with open (txt_path, 'w') as f:
    f.write("Election Results")
    f.write("__________________")
    f.write(Output)
    f.write(Winner)



