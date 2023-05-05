# Import os
import os
# read csv
import csv
#import statistics
import statistics

#showing where the data is
budget_data = os.path.join('Resources','budget_data.csv')

# setting change as veriable so i can use it later
change = []

with open(budget_data) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    
    Total_Months = 0
    Total = 0

    Total_Months = len(list(csvreader))

 
    for row in csvreader:
        Total += int(row[1])
    print(Total)

  
