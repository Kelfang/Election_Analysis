# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies (the necessary tools to read the csv file and write the results.)
import csv
import os

# Assign a variable to load a file from the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis','election_analysis.txt')

# Initialize a total vote counter.
total_votes = 0

# Create Candidate Options list.
candidate_options = []

# Create an empty dictionary to house the candidates and their vote count.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file. Keep this 'for' indented since it references the 'with' action.
    for row in file_reader:
        # Add to the total vote count. 
        total_votes += 1

        # Print the candidate name from each row
        candidate = row[2]

        # If the candidate does not match any existing candidate...
        if candidate not in candidate_options:          

            # Add the candidate name to the candidate options list. 
            candidate_options.append(candidate)

            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate] = 0

        # Adding the votes by candidate.
        candidate_votes[candidate] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file, print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
# Determine the percentage of votes for each candidate by looping thru the counts.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate. 
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes. 
        vote_percentage = float(votes) / float(total_votes) * 100

        # Identify the candidate's results.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

         # Print the candidate name and percentage of votes to the terminal.
        print(candidate_results)

        # Save the candidate results to our text file. 
        txt_file.write(candidate_results)

        # Determine winning vote count, voting percentage and winning candidate.
        # Must identify by establishing votes vs. the winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true than set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate to equal the candidate's name. 
            winning_candidate = candidate

            # Format the winning_candidate summary. 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # Print the winning candidate's summary to the terminal.
    print(winning_candidate_summary)
    
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

