#Import Dependencies
import os
import csv

#Declare file location
budget_csv= os.path.join('..', 'Resources', 'budget_data.csv')

with open('budget_data.csv', 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ',')
    header= next(csvreader)

    #create empty lists to hold the csv values
    count_month= []
    profit= []
    profit_change= []

    #read through the value and add to the empty lists above
    for row in csvreader:
        count_month.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1]-profit[i])

#find the max profit increase and decrease from the data set
increase= max(profit_change)
decrease= min(profit_change)

#find the month of each max and min
month_increase= profit_change.index(max(profit_change))+1
month_decrease= profit_change.index(min(profit_change))+1

#Print the Financial Analysis
print("Financial Analysis")
print("------------------------------")
print(f"Total Months :{len(count_month)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {count_month[month_increase]} (${str(increase)})")
print(f"Greatest Decrease in Profits: {count_month[month_decrease]} (${str(decrease)})")

#Output File

output_file= '../Financial_Analysis.txt'
#Export to txt file
with open(output_file, "w") as outfile:
    outfile.write("Financial Analysis")
    outfile.write("\n")
    outfile.write("------------------------------")
    outfile.write("\n")
    outfile.write(f"Total Months :{len(count_month)}")
    outfile.write("\n")
    outfile.write(f"Total: ${sum(profit)}")
    outfile.write("\n")
    outfile.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
    outfile.write("\n")
    outfile.write(f"Greatest Increase in Profits: {count_month[month_increase]} (${str(increase)})")
    outfile.write("\n")
    outfile.write(f"Greatest Decrease in Profits: {count_month[month_decrease]} (${str(decrease)})")
