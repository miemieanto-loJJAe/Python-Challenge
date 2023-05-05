import os
import csv
import statistics

budget_data = os.path.join('Resources','budget_data.csv')

#listing variables
Total_Months = 0
Total = 0

with open(budget_data) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

#going to create a loop
    for row in csvreader:
        Total_Months += 1
        Total += int(row[1])

