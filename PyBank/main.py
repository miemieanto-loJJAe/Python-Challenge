import os
import csv
import statistics

#csv path
budget_data = os.path.join('Resources','budget_data.csv')

txt_path = "Financial_Analysis.txt"

#listing variables
Total_Months = 0
Total = 0
Biggest_Increase = 0
Biggest_Decrease = 0
Highest_Month = ''
Lowest_Month = ''

Difference = []
Monthly_Difference = []



#open csv file
with open(budget_data) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

#going to create a loop for biggest increase and decrease
    for row in csvreader:
        Total_Months += 1
        Total += int(row[1])
        if int(row[1]) < Biggest_Decrease:
            Biggest_Decrease = int(row[1])
            Lowest_Month = (row[0])
        elif int(row[1]) > Biggest_Increase:
            Biggest_Increase = int(row[1])
            Highest_Month = (row[0])
        Difference.append(int(row[1]))

    for i in range(len(Difference)-1): 
        DifferenceForMonth= (Difference[i+1] - Difference[i])
        Monthly_Difference.append(DifferenceForMonth)

    Average_Difference = statistics.mean(Monthly_Difference)

  
    print("Financial Analysis")
    print('____________________')
    print(f"Total Months: {Total_Months}")
    print(f"Total: ${Total}")
    print(f"Average Change: ${Average_Difference}")
    print(f"Greatest Increase in Profits: {Lowest_Month}, {Biggest_Increase}")
    print(f"Greatest Decrease in Profits: {Highest_Month}, {Biggest_Decrease}")

with open(txt_path, 'w') as f:
    f.write("Financial Analysis")
    f.write("__________________")
    f.write(f"Total Months: {Total_Months}")
    f.write(f"Total: ${Total}")
    f.write(f"Average Change: ${Average_Difference}")
    f.write(f"Greatest Increase in Profits: {Lowest_Month}, {Biggest_Increase}")
    f.write(f"Greatest Decrease in Profits: {Highest_Month}, {Biggest_Decrease}")