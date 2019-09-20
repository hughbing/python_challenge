import os
import csv

csv_path = os.path.join("..","Resources","budget_data.csv")

mcount = 0
total = 0
PreValue = 0 
Diff = 0
DiffMax = 0 
DiffMin = 0

with open(csv_path, newline='') as csvfile:
     csv_reader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csv_reader)
     print('Financial Analysis')
 for i in csv_reader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue

         #Placeholder to track greatest increase in profits (financial analysis)
         if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month

         #Placeholder to track greatest decrease in profits (financial analysis)
         if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month

         PreValue = iAmount   
         # Get total months (financial analysis)
         mcount = mcount + 1
         total += int(Amount) 

## Display Results ##      
#The total number of months included in the dataset
print('Total Months : {mcount}')
#The total net amount of "Profit/Losses" over the entire period
print('Total: $ {total}')
# Greatest increase in profit
print('Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
# Greatest increase in profit
print('Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')
