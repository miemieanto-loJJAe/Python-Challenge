import os

import csv

csvpath = os.path.join("Resources","budget_data.csv")

def Financial_Analysis(Budget_data):
    Date = str(Budget_data[0])
    Profit_Losses = int(Budget_data[1])
    
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    Total_Months = len(list(csvreader))

    def sum(numbers):
        length = len(numbers)
        Total = 0
    
        Total = Total + (row["Profit/Losses"])