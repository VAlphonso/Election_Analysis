# The data we need to retrieve.
# 1. The total number of votes case
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read andanalyze the data here.
    # Read the file object with the reader function. 
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print (headers)

    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)



    #Print the file object.
#    print(election_data)


# Using the open() function with the "w" mode we will arite data to the file.
open(file_to_save, "w")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")

# Write some data to the file.
#outfile.write("Hello World")

#outfile.write("Arapahoe, Denver, Jefferson")

#outfile.write("Counties in the Election \n-------------\nArapahoe \nDenver\nJefferson")

# Close the file
outfile.close()
