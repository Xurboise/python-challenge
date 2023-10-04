import os
import csv

months = []
profLoss = []

change = []
#csv location
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#open said csv location, read it, and append lists needed
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
    #add the values to var list declared above
    for row in csvreader:
        months.append(row[0])
        profLoss.append(int(row[1]))

        total = sum(profLoss)

#find the row that matches the min and max
for i in range(0, len(profLoss), 1):
    #don't go over the length of the list
    if(i < len(profLoss) - 1):
        change.append((profLoss[i+1]) - profLoss[i])

#var data
increaseNum = max(change)
decreaseNum = min(change)
indexHigh = change.index(max(change))
indexLow = change.index(min(change))
increaseDate = months[indexHigh + 1]
decreaseDate = months[indexLow + 1]          
average = sum(change) / len(change)

#print to terminal
print("Finacial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${total}")
print(f"Average Change: ${round(average, 2)}")
print(f"Greatest Increase in Profit: {increaseDate} (${increaseNum})")
print(f"Greatest Decrease in Profit: {decreaseDate} (${decreaseNum})")

#locate the output for a text file
output = os.path.join('PyBank', 'analysis', 'analysis.txt')

#write results in a text file
with open(output, 'w') as txtfile:
    txtfile.writelines("Finacial Analysis\n")
    txtfile.writelines("----------------------------\n")
    txtfile.writelines(f"Total Months: {len(months)}\n")
    txtfile.writelines(f"Total: ${total}\n")
    txtfile.writelines(f"Average Change: ${round(average, 2)}\n")
    txtfile.writelines(f"Greatest Increase in Profit: {increaseDate} (${increaseNum})\n")
    txtfile.writelines(f"Greatest Decrease in Profit: {decreaseDate} (${decreaseNum})")