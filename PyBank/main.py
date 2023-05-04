import os

import csv

import statistics


budget_csv = os.path.join("Resources","budget_data.csv")

def Financial_Analysis(Budget_data):
     
    date = str(Budget_data[0])
    profit_losses = int(Budget_data[1])

    total_months = len(date)
    total = sum(profit_losses)
    average_change = (total / total_months)



    with open(budget_csv, 'r') as csvfile:

     csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

   
    Total_Months = len(list(csvreader))
    print(Total_Months)
   

 

        