# Import os
import os
# read csv
import csv
#import statistics
import statistics

#showing where the data is
budget_data = os.path.join('Resources','budget_data.csv')

Total_Months = 0
Total = 0


with open(budget_data) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    for row in csvreader:
        Total_Months += 1

    print(Total_Months)

    Total = Total + int(row[1])
    print(Total)
    




