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
with open('election_data') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #start loop to find answers
    for row in csvreader:
        Total_Votes += 1
    print(Total_Votes)
    


