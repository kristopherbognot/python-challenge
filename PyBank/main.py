import os
import csv

budget_file = os.path.join("Resources/budget_data.csv")

month_count = 0
P_L = 0
Max = 0
Min = 0
data =[]
data2=[]


with open(budget_file, newline="") as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
    
    next(csvreader)
    

    for row in csvreader:    
        if row[0] == "Jan" or "Feb" or "Mar" or "Apr" or "May" or "Jun" or "Jul" or "Aug" or "Sep" or "Oct" or "Nov" or "Dec":
            month_count = month_count + 1


            P_L += int(row[1])


            data.append(int(row[1]))


            data2.append(row[0])
            
        
avgChg = round(int(P_L)/int(month_count),2)

Max = max(data)
Min = min(data)
x = data.index(Max)
y = data.index(Min)
maxMon = data2[x]
minMon = data2[y]


print("")
print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(P_L))
print("Average Change: $" + str(avgChg))
print("Greatest Increase in Profits : " + maxMon + "  ($" + str(Max) + ")")
print("Greatest Decrease in Profits : " + minMon + "  ($" + str(Min) + ")")
print("")



output_path = os.path.join("Resources/PyBank.txt")

with open(output_path, 'w', newline='') as csvfile:

    
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['--------------------------'])
    csvwriter.writerow(['Total Months: ' + str(month_count)])
    csvwriter.writerow(['Total: $' + str(P_L)])
    csvwriter.writerow(['Average Change: $' + str(avgChg)])
    csvwriter.writerow(['Greatest Increase in Profits : ' + maxMon + '  ($' + str(Max) + ')'])
    csvwriter.writerow(['Greatest Decrease in Profits : ' + minMon + '  ($' + str(Min) + ')'])
