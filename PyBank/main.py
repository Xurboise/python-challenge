import os
import csv
months = []
profLoss = []
average = 69
increaseDate = "Date1"
increaseNum = 999
decreaseDate = "Date2"
decreaseNum = -999

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    for row in csvreader:
        months.append(row[0])
        profLoss.append(int(row[1]))

        total = sum(profLoss)


print("Finacial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")

print(f"Total: ${total}")

print("Average Change: $" + str(average))



print(f"Greatest Increase in Profit:{increaseDate} ({increaseNum})")

print(f"Greatest Decrease in Profit: {decreaseDate} ({decreaseNum})")

#output_file = os.path.join("output.csv") but to text