import os
import csv
import statistics

budget_data = os.path.join('Resources','budget_data.csv')

#listing variables
Total_Months = 0
Total = 0
Biggest_Increase = 0
Biggest_Decrease = 0
Highest_Month = ''
Lowest_Month = ''

with open(budget_data) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

#going to create a loop
    for row in csvreader:
        Total_Months += 1
        Total += int(row[1])
        if int(row[1]) < Biggest_Decrease
            Biggest_Decrease = int(row[1])
            Lowest_Month = (row[0])
        elif int(row[1]) > Biggest_Increase
            Biggest_Increase = int(row[1])
            Highest_Month = (row[0])
    print(Biggest_Decrease)

