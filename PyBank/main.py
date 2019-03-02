import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

print()
print("Financial Analysis")
print("------------------------")

months = []
profits = []
change = []

def getMonths():
    for row in csvreader:
        months.append(row[0])

def getProfits():
    for row in csvreader:
        profits.append(int(row[1]))
        
def getChange():
    for i in range(len(profits) - 1):
        change.append(profits[i+1] - profits[i])
    return (sum(change)/len(change))

def getInc():
    inc = 0
    index = 0
    for i in range(len(change)):
        if change[i] > inc:
            inc = change[i]
            index = i
    return index
    
def getDec():
    dec = 0
    index = 0
    for i in range(len(change)):
        if change[i] < dec:
            dec = change[i]
            index = i
    return index

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    getMonths()
    
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    getProfits()
    
monthsTotal = len(months)
print(f"Total Months: {monthsTotal}")

nettotal = 0
for i in range(len(profits)):
    nettotal += profits[i]
print(f"Total: ${nettotal}")

avgChange = round(getChange(),2)
print(f"Average Change: ${avgChange}")

indexInc = getInc()
print(f"Greatest Increase in Profits: {months[indexInc+1]} (${change[indexInc]})")

indexDec = getDec()
print(f"Greatest Increase in Profits: {months[indexDec+1]} (${change[indexDec]})")

file = open("Financial_Analysis.txt", "w")
file.write("Financial Analysis\n")
file.write("------------------------\n")
file.write(f"Total Months: {monthsTotal}\n")
file.write(f"Total: ${nettotal}\n")
file.write(f"Average Change: ${avgChange}\n")
file.write(f"Greatest Increase in Profits: {months[indexInc+1]} (${change[indexInc]})\n")
file.write(f"Greatest Increase in Profits: {months[indexDec+1]} (${change[indexDec]})\n")
file.close()
