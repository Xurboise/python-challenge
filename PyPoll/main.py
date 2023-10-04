import os
import csv

votes = []
candidates = []
county = []

#csv location
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

#open said csv location, read it, and append lists needed
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
    #add the values to var list declared above
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
        county.append(row[1])

#using candidiates list, find the name of each candidate
canOutput = []
for x in candidates:
    if x not in canOutput:
        canOutput.append(x)

#votes per candidate and their percentage
voterOut1 = candidates.count(canOutput[0])
percent1 = (candidates.count(canOutput[0]) / len(votes)) * 100
voterOut2 = candidates.count(canOutput[1])
percent2 = (candidates.count(canOutput[1]) / len(votes)) * 100
voterOut3 = candidates.count(canOutput[2])
percent3 = (candidates.count(canOutput[2]) / len(votes)) * 100

#Who has the most votes
def mostvotes(list1):
    return max(set(list1), key=list1.count)



#print to terminal
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {len(votes)}")
print(f"-------------------------")
print(f"{canOutput[0]}: {round(percent1, 3)}% ({voterOut1})")
print(f"{canOutput[1]}: {round(percent2, 3)}% ({voterOut2})")
print(f"{canOutput[2]}: {round(percent3, 3)}% ({voterOut3})")
print(f"-------------------------")
print(f"Winner: {mostvotes(candidates)}")
print(f"-------------------------")

#find location for text file
output = os.path.join('PyPoll', 'analysis', 'analysis.txt')

#write results in a text file
with open(output, 'w') as txtfile:
    txtfile.writelines(f"Election Results\n")
    txtfile.writelines(f"-------------------------\n")
    txtfile.writelines(f"Total Votes: {len(votes)}\n")
    txtfile.writelines(f"-------------------------\n")
    txtfile.writelines(f"{canOutput[0]}: {round(percent1, 3)}% ({voterOut1})\n")
    txtfile.writelines(f"{canOutput[1]}: {round(percent2, 3)}% ({voterOut2})\n")
    txtfile.writelines(f"{canOutput[2]}: {round(percent3, 3)}% ({voterOut3})\n")
    txtfile.writelines(f"-------------------------\n")
    txtfile.writelines(f"Winner: {mostvotes(candidates)}\n")
    txtfile.writelines(f"-------------------------\n")
