import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

print()
print("Election Results")
print("------------------------")

votingData = []
KhanCount = 0
CorreyCount = 0
LiCount = 0
TooleyCount = 0

def getCanidates():
    for row in csvreader:
        votingData.append(row[2])

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    getCanidates()
    
totalVotes = len(votingData)
print(f"Total Votes: {totalVotes}")

for c in votingData:
    if c == "Khan":
        KhanCount += 1
    elif c == "Correy":
        CorreyCount += 1
    elif c == "Li":
        LiCount += 1
    else:
        TooleyCount += 1

KhanPercent = round(((KhanCount/totalVotes) * 100), 2)
CorreyPercent = round(((CorreyCount/totalVotes) * 100), 2)
LiPercent = round(((LiCount/totalVotes) * 100), 2)
TooleyPercent = round(((TooleyCount/totalVotes) * 100), 2)

print("------------------------")
print(f"Khan: {KhanPercent}% ({KhanCount})")
print(f"Correy: {CorreyPercent}% ({CorreyCount})")
print(f"Li: {LiPercent}% ({LiCount})")
print(f"O'Tooley: {TooleyPercent}% ({TooleyCount})")
print("------------------------")

canidates = {"Khan":KhanCount, "Correy":CorreyCount, "Li":LiCount, "Tooley":TooleyCount}

winner = max(canidates, key=canidates.get)

print(f"Winner: {winner}")
print("------------------------")

file = open("Election_Results.txt", "w")
file.write("Election Results\n")
file.write("------------------------\n")
file.write(f"Total Votes: {totalVotes}\n")
file.write("------------------------\n")
file.write(f"Khan: {KhanPercent}% ({KhanCount})\n")
file.write(f"Correy: {CorreyPercent}% ({CorreyCount})\n")
file.write(f"Li: {LiPercent}% ({LiCount})\n")
file.write(f"O'Tooley: {TooleyPercent}% ({TooleyCount})\n")
file.write("------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("------------------------\n")
file.close()