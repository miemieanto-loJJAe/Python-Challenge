import os

import csv

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    Total_Months = len(list(csvreader))
    print(Total_Months)
    
    Total = sum(int(r['Value']) for r in csv.DictReader(csvfile))
    print(Total)