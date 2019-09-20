import os
import csv


csv_path = os.path.join( '..','Resources','election_data.csv')

totalcount = 0
kcount = 0
ccount = 0
lcount = 0
ocount = 0
max_votecount = 0

#Function for % calculation
def percentage (part, whole):
    return 100 * float(part)/float(whole)

#Open and read CSV file
with open(csv_path, newline='') as csvfile:
     csv_reader = csv.reader(csvfile, delimiter=',')

     for i in csvreader:
         voterid = i[0]
         country = i[1]
         candidate = i[2]
         # Find Total Vote Count
         totalcount = totalcount + 1

         # Find votecount by candidates
         if candidate =="Khan":
            kcount = kcount + 1
         if candidate =="Correy":
            ccount = ccount + 1
         if candidate =="Li":
            lcount = lcount + 1
         if candidate =="O'Tooley":
            ocount = ocount + 1
            
# Define (dictionary) list : candidate and votes
     candidatevote = {"Khan": kcount,"Correy": ccount,"Li" :lcount, "O'Tooley": ocount}
     # Find winner 
     for candidate, value in candidatevote.items():
         if value > max_votecount:
            max_votecount = value
            winner = candidate
# Display results       
print(Election Results)
print(Total Votes: {totalcount})

print('Khan: {percentage(kcount,totalcount):.3f}%  ({kcount})')
print('Correy: {percentage(ccount,totalcount):.3f}%  ({ccount})')
print('Li: {percentage(lcount,totalcount):.3f}%  ({lcount})')
print('Tooley: {percentage(ocount,totalcount):.3f}%  ({ocount})')
print('Winner: {winner}')

