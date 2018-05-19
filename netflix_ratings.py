import os
import csv

csvpath = os.path.join('..', 'Resources', 'netflix_ratings.csv')


showName = input("What show would you like to lookup? ")
found = False
		

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
		csvreader = csv.reader(csvfile, delimiter=',')
    
		#  Each row is read as a row
		for row in csvreader:
			show = row[0]
			rating = row[1]
			score = row[5]
			if(show == showName):
				print(show + " has a rating of " + rating + " and a score of " + str(score))
				found = True
				break    	
		
if(found is False):
	print("Sorry about this, we don't seemd to have what you're looking for...")   	
        
