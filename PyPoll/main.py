import os
import csv

election_file = os.path.join("Resources/election_data.csv")

total_votes = 0
names = []
names2 = []
ticket = []
w = 0
x = 0
y = 0
z = 0


with open(election_file, newline="") as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
    
    next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1

        names.append(row[2])
        names2. append(row[2])
        
    for line in names:
        con = line.split()
        for names in con:
            if names not in ticket:
                ticket.append(names)
                
w = names2.count(str(ticket[0]))
x = names2.count(str(ticket[1]))
y = names2.count(str(ticket[2]))
z = names2.count(str(ticket[3]))


wPer = round(int((w / total_votes) * 100),4)
xPer = round(int((x / total_votes) * 100),4)
yPer = round(int((y / total_votes) * 100),4)
zPer = round(int((z / total_votes) * 100),4)


if w > x and w > y and w > z:
    winner = str(ticket[0])
if x > w and x > y and x > z:
    winner = str(ticket[1])
if y > x and y > z and y > z:
    winner = str(ticket[2])
if z > x and z > y and z > x:
    winner = str(ticket[3])


print("")
print("Election Results")
print("------------------------")
print("Total Votes: " + str(total_votes))
print("------------------------")
print(str(ticket[0]) + ": " + str(wPer) + "%" + " (" + str(w) + ")")
print(str(ticket[1]) + ": " + str(xPer) + "%" + " (" + str(x) + ")")
print(str(ticket[2]) + ": " + str(yPer) + "%" + " (" + str(y) + ")")
print(str(ticket[3]) + ": " + str(zPer) + "%" + " (" + str(z) + ")")
print("------------------------")
print("Winner: " + str(winner))
print("------------------------")


output_path = os.path.join("Resources/PyPoll.txt")

with open(output_path, 'w', newline='') as csvfile:

    
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['--------------------------'])
    csvwriter.writerow(['Total Votes: ' + str(total_votes)])
    csvwriter.writerow(['--------------------------'])
    csvwriter.writerow([str(ticket[0]) + ': ' + str(wPer) + '%' + ' (' + str(w) + ')'])
    csvwriter.writerow([str(ticket[1]) + ': ' + str(xPer) + '%' + ' (' + str(x) + ')'])
    csvwriter.writerow([str(ticket[2]) + ': ' + str(yPer) + '%' + ' (' + str(y) + ')'])
    csvwriter.writerow([str(ticket[3]) + ': ' + str(zPer) + '%' + ' (' + str(z) + ')'])
    csvwriter.writerow(['--------------------------'])                
    csvwriter.writerow(['Winner: ' + str(winner)])
    csvwriter.writerow(['--------------------------'])       
