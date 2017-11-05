import os
import csv

cwd = os.getcwd()

file_list = ["budget_data_1.csv", "budget_data_2.csv"]

print()

for filePick in file_list:     
    print("[" + str(file_list.index(filePick)) + "] " + filePick)

print()

usrInput = input("Please select an input file from the list above: ")
usrInput = int(usrInput)

# exception isn't handled in the conditional statement below

if usrInput == 0:
    selectedFile = 'budget_data_1.csv'
if usrInput == 1:
    selectedFile = 'budget_data_2.csv'

print()

print("You have selected: " + selectedFile)

csvpath = os.path.join(cwd, selectedFile)

Date = []
Revenue = []

csvpath = os.path.join(cwd, selectedFile)
with open(csvpath, newline="") as csvfile:  
    inputData = csv.reader(csvfile, delimiter=',')
    monthCount = 0
    for row in inputData:
        monthCount = monthCount +1
        Date.append(row[0])
        Revenue.append(row[1])

    count = 1
    totalRevenue = 0
    grtstRevIncrease = 0
    grtstRevDecrease = 0
    
    while count <= monthCount-1:
        totalRevenue = int(totalRevenue) + int(Revenue[count])
        if grtstRevIncrease < int(Revenue[count]):
            grtstRevIncrease = int(Revenue[count])
            countIncrease = count
        if grtstRevDecrease > int(Revenue[count]):
            grtstRevDecrease = int(Revenue[count])
            countDecrease = count
        count +=1
    
    avgRevChange = totalRevenue/(monthCount - 1)
    avgRevChange = int(avgRevChange)

    print()
    print("Financial Analysis")
    print("- - - - - - - - - - - - - - - - - -")
    print("Total Months: " + str(monthCount-1))
    print("Total Revenue: $" + str(totalRevenue))
    print("Average Revenue Change: $" + str(avgRevChange))
    print("Greatest Increase in Revenue: " + Date[countIncrease] + " " + "($" + str(grtstRevIncrease) + ")")
    print("Greatest Decrease in Revenue: " + Date[countDecrease] + " " + "($" + str(grtstRevDecrease) + ")")
    print()
    
    output_file = 'budget_data_output.txt'

    #call('python main.py >> output_file') - wanted to get this to work, but it didn't

    with open(output_file, 'w') as txtfile:
        txtfile.write("Financial Analysis")
        txtfile.write("\n")
        txtfile.write("- - - - - - - - - - - - - - - - - -")
        txtfile.write("\n")
        txtfile.write("Total Months: " + str(monthCount-1))
        txtfile.write("\n")
        txtfile.write("Total Revenue: $" + str(totalRevenue))
        txtfile.write("\n")
        txtfile.write("Average Revenue Change: $" + str(avgRevChange))
        txtfile.write("\n")
        txtfile.write("Greatest Increase in Revenue: " + Date[countIncrease] + " " + "($" + str(grtstRevIncrease) + ")")
        txtfile.write("\n")
        txtfile.write("Greatest Decrease in Revenue: " + Date[countDecrease] + " " + "($" + str(grtstRevDecrease) + ")")