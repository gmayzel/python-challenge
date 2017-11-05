import os
import csv

cwd = os.getcwd()

file_list = ["election_data_1.csv", "election_data_2.csv"]

print()

for filePick in file_list:     
    print("[" + str(file_list.index(filePick)) + "] " + filePick)

print()

usrInput = input("Please select an input file from the list above: ")
usrInput = int(usrInput)

# exception isn't handled in the conditional statement below

if usrInput == 0:
    selectedFile = 'election_data_1.csv'
if usrInput == 1:
    selectedFile = 'election_data_2.csv'

print()

print("You have selected: " + selectedFile)

csvpath = os.path.join(cwd, selectedFile)

voterID = []
county = []
candidate = []
uniqueCandidate =[]
voteCount = []
votePercentage = []

csvpath = os.path.join(cwd, selectedFile)
with open(csvpath, newline="") as csvfile:  
    inputData = csv.reader(csvfile, delimiter=',')
   
    for row in inputData:
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

print()
totVotes = len(voterID) - 1

for x in candidate:
    if x not in uniqueCandidate:
        uniqueCandidate.append(x)

del uniqueCandidate[0]    

for y in uniqueCandidate:  
    candidateCount = str(candidate.count(y))
    candidateCount = "(" + candidateCount + ")"
    voteCount.append(candidateCount)
    percentage = round(int((candidate.count(y)/totVotes)*100), 2)
    percentage = str(percentage)
    percentage = percentage + "%"
    votePercentage.append(percentage)

print()
print("Election Results")
print("- - - - - - - - - - - - - - - - - -")
print("Total Votes: " + str(totVotes))
print("- - - - - - - - - - - - - - - - - -")
for a, b, c in zip(uniqueCandidate, votePercentage, voteCount):
    print(a + "\t\t" + b + "\t" + c)
print("- - - - - - - - - - - - - - - - - -")
winner = max(zip(voteCount, uniqueCandidate))
print("Winner: " + winner[1])
print("- - - - - - - - - - - - - - - - - -")
    
output_file = 'election_results_output.txt'
    
with open(output_file, 'w') as txtfile:     
    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("- - - - - - - - - - - - - - - - - -")
    txtfile.write("\n")
    txtfile.write("Total Votes: " + str(totVotes))
    txtfile.write("\n")
    txtfile.write("- - - - - - - - - - - - - - - - - -")
    txtfile.write("\n")
    for a, b, c in zip(uniqueCandidate, votePercentage, voteCount):
        txtfile.write(a)
        txtfile.write("\t\t")
        txtfile.write(b)
        txtfile.write("\t")
        txtfile.write(c)
        txtfile.write("\n")
    txtfile.write("- - - - - - - - - - - - - - - - - -")
    txtfile.write("\n")
    txtfile.write("Winner: " + winner[1])
    txtfile.write("\n")
    txtfile.write("- - - - - - - - - - - - - - - - - -")