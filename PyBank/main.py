import os
import csv

budget_data = os.path.join('Resources','budget_data.csv')

#listing variables
Total_Months = 0
Total = 0

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    print(csvreader)
#going to create a loop

    Total_Months += 1
