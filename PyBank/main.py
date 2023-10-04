import os
import csv
months = []
profLoss = []
change = []
csvpath = os.path.join('GitHub','python-challenge','PyBank', 'Resources', 'budget_data.csv')
#C:\Users\etchb\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        months.append(row[0])
        profLoss.append(int(row[1]))

        total = sum(profLoss)

for i in range(0, len(profLoss), 1):

    if(i < len(profLoss) - 1):
        change.append((profLoss[i+1]) - profLoss[i])

increaseNum = max(change)
decreaseNum = min(change)
indexHigh = change.index(max(change))
indexLow = change.index(min(change))
increaseDate = months[indexHigh + 1]
decreaseDate = months[indexLow + 1]          
average = sum(change) / len(change)

print("Finacial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${total}")
print(f"Average Change: ${round(average, 2)}")
print(f"Greatest Increase in Profit: {increaseDate} (${increaseNum})")
print(f"Greatest Decrease in Profit: {decreaseDate} (${decreaseNum})")

output = os.path.join('PyBank', 'analysis', 'analysis.txt')
#output_file = os.path.join("output.csv") but to text
with open(output, 'w') as txtfile:
    txtwriter = csv.writer(txtfile, delimiter=',')
    txtwriter.writerow("Finacial Analysis")
    txtwriter.writerow("----------------------------")
    txtwriter.writerow(f"Total Months: {len(months)}")
    txtwriter.writerow(f"Total: ${total}")
    txtwriter.writerow(f"Average Change: ${round(average, 2)}")
    txtwriter.writerow(f"Greatest Increase in Profit: {increaseDate} (${increaseNum})")
    txtwriter.writerow(f"Greatest Decrease in Profit: {decreaseDate} (${decreaseNum})")