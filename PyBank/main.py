import os

import csv

import statistics


budget_csv = os.path.join("Resources","budget_data.csv")

Total_Months = 0
Total = 0




with open(budget_csv, 'r') as csvfile:

     csvreader = csv.reader(csvfile, delimiter=',')


     csv_header = next(csvreader)

for row in csvreader:
       Total_Months = len(list(csvreader))
       Total += int(row[1])
print()

   
  
   

 

        