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


