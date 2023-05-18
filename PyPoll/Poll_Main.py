#Import Dependencies
import os
import csv

#Declare file location
budget_csv= os.path.join('..', 'Resources', 'election_data.csv')

with open('election_data.csv', 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ',')
    header= next(csvreader)

    #Define the variables
    Votes_total= 0
    Stockham_votes= 0
    DeGette_votes= 0
    Doane_votes= 0

    for row in csvreader:

        #Count the unique Voter ID's and store in variable
        Votes_total +=1

        #Now we need to count how many times each candidate's name appears per ID
        if row[2] =="Charles Casper Stockham":
            Stockham_votes+=1
        elif row[2] == "Diana DeGette":
            DeGette_votes+=1
        elif row[2] =="Raymon Anthony Doane":
            Doane_votes+=1
#print(Stockham_votes)
#print(DeGette_votes)
#print(Doane_votes)

#Create a dictionary for the candidates and the votes
candidates= ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes= [Stockham_votes, DeGette_votes, Doane_votes]

#Now zip the files together to get a list candidates and their total votes
dict_Candidate_votes= dict(zip(candidates,votes))
#print(dict_Candidate_votes)
#Return a winner using max function
winner= max(dict_Candidate_votes, key=dict_Candidate_votes.get)

#Print the summary of analysis
Stockham_perc= (Stockham_votes/Votes_total)*100
DeGette_perc= (DeGette_votes/Votes_total)*100
Doane_perc= (Doane_votes/Votes_total)*100

#Print the Results Summary Table
print(f'Election Results')
print(f'-----------------------')
print(f'Total Votes: {Votes_total}')
print(f'-----------------------')
print(f'Charles Casper Stockham: {Stockham_perc:.3f}% ({Stockham_votes})')
print(f'Diana DeGette: {DeGette_perc:.3f}% ({DeGette_votes})')
print(f'Raymon Anthony Doane: {Doane_perc:.3f}% ({Doane_votes})')
print(f'-----------------------')
print(f'Winner: {winner}')
print(f'-----------------------')

#Output File

output_file= '../Election_results.txt'
#Export to txt file
with open(output_file, "w") as outfile:
    outfile.write(f'Election Results')
    outfile.write("\n")
    outfile.write(f'-----------------------')
    outfile.write("\n")
    outfile.write(f'Total Votes: {Votes_total}')
    outfile.write("\n")
    outfile.write(f'-----------------------')
    outfile.write("\n")
    outfile.write(f'Charles Casper Stockham: {Stockham_perc:.3f}% ({Stockham_votes})')
    outfile.write("\n")
    outfile.write(f'Diana DeGette: {DeGette_perc:.3f}% ({DeGette_votes})')
    outfile.write("\n")
    outfile.write(f'Raymon Anthony Doane: {Doane_perc:.3f}% ({Doane_votes})')
    outfile.write("\n")
    outfile.write(f'-----------------------')
    outfile.write("\n")
    outfile.write(f'Winner: {winner}')
    outfile.write("\n")
    outfile.write(f'-----------------------')



