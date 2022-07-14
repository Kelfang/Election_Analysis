# Election Analysis


## Project Overview
The purpose of this project was to assist the Colorado Board of Elections with their election audit by counting the votes and determining the winner of a congressional race. 

1.	Determine the total number of votes that were casted.
2.	Identify the list of candidates who received votes.
3.	Count the total number of votes each candidate received.
4.	Identify the percentage of votes that each candidate won.
5.	Name the winner of the election based on the popular vote.


## Resources
- Software: Python, Visual Studio Code

- Data Source: election_results.csv


## Summary
I was provided with a .csv file that contained the Ballot ID, the county where the vote was cast, and the Candidate's name. The Ballot ID is an unique 6-digit number that was assigned to each vote within the file and is tied to a single unknown resident in the pertinent county. This ensured that there were no duplicate votes listed (or counted) in the analysis of this election. 

### Election Audit Results

- There were 369,711 votes cast in this election.
------------------------------------------------------	
  - The counties and vote counts within this audit:
  	  - Arapahoe: 24,801 votes (6.7%)
	  - Denver: 306,055 votes (82.8%)
	  - Jefferson: 38,855 votes (10.5%)
 ------------------------------------------------------	  
  - The county with the largest voter turnout: Denver
 ------------------------------------------------------	
  - The candidates were:
	  - Charles Casper Stockham
	  - Diana DeGette
	  - Raymon Anthony Doane
 ------------------------------------------------------
  - The results for each candidate are as follows:
	  - Charles Casper Stockham received 23.0% of the vote with a vote count of 85,213.
	  - Diana DeGette received 73.8% of the vote with a vote count of 272,892.
	  - Raymon Anthony Doane received 3.1% of the vote with a vote count of 11,606.
 ------------------------------------------------------
  - The winner of the election was:
	  - Diana DeGette received 73.8% of the vote with a vote count of 272,892.
 ------------------------------------------------------
 A link to the raw output of the Election Results can be found [here](https://github.com/Kelfang/Election_Analysis/blob/main/analysis/election_results.txt).
 
 ### Election Audit Summary
 The code that was used to determine the outcome of this election is written in such a way that it can easily be modified and used in other elections, regardless of location or number of votes. In the images below I have indicated two places where the code could be adjusted to accommodate other elections.
 
 In this image, the code would loop through each row and collect the candidate names all while counting the vote. We would not have to manually identify the names listed within the data. 
 ```
  # 𝘐𝘧 𝘵𝘩𝘦 𝘤𝘢𝘯𝘥𝘪𝘥𝘢𝘵𝘦 𝘥𝘰𝘦𝘴 𝘯𝘰𝘵 𝘮𝘢𝘵𝘤𝘩 𝘢𝘯𝘺 𝘦𝘹𝘪𝘴𝘵𝘪𝘯𝘨 𝘤𝘢𝘯𝘥𝘪𝘥𝘢𝘵𝘦 𝘢𝘥𝘥 𝘪𝘵 𝘵𝘰 𝘵𝘩𝘦 𝘤𝘢𝘯𝘥𝘪𝘥𝘢𝘵𝘦 𝘭𝘪𝘴𝘵.
  if candidate_name not in candidate_options:

      # 𝘈𝘥𝘥 𝘵𝘩𝘦 𝘤𝘢𝘯𝘥𝘪𝘥𝘢𝘵𝘦 𝘯𝘢𝘮𝘦 𝘵𝘰 𝘵𝘩𝘦 𝘤𝘢𝘯𝘥𝘪𝘥𝘢𝘵𝘦 𝘭𝘪𝘴𝘵. 
      candidate_options.append(candidate_name)

      # 𝘈𝘯𝘥 𝘣𝘦𝘨𝘪𝘯 𝘵𝘳𝘢𝘤𝘬𝘪𝘯𝘨 𝘵𝘩𝘢𝘵 𝘤𝘢𝘯𝘥𝘪𝘥𝘢𝘵𝘦'𝘴 𝘷𝘰𝘵𝘦𝘳 𝘤𝘰𝘶𝘯𝘵.
      candidate_votes[candidate_name] = 0

      # 𝘈𝘥𝘥 𝘢 𝘷𝘰𝘵𝘦 𝘵𝘰 𝘵𝘩𝘢𝘵 𝘤𝘢𝘯𝘥𝘪𝘥𝘢𝘵𝘦'𝘴 𝘤𝘰𝘶𝘯𝘵. 
      candidate_votes[candidate_name] += 1
      
```
 Additionally, similar to the image above, this is where we could change the location of where the votes are being counted. We could substitute cities or states here as well. These modest changes make the code very mallable for any kind of election, without completely rewriting the code. 
```
  # 𝘞𝘳𝘪𝘵𝘦 𝘢𝘯 𝘪𝘧 𝘴𝘵𝘢𝘵𝘦𝘮𝘦𝘯𝘵 𝘵𝘩𝘢𝘵 𝘤𝘩𝘦𝘤𝘬𝘴 𝘵𝘩𝘢𝘵 𝘵𝘩𝘦 𝘤𝘰𝘶𝘯𝘵𝘺 𝘥𝘰𝘦𝘴 𝘯𝘰𝘵 𝘮𝘢𝘵𝘤𝘩 𝘢𝘯𝘺 𝘦𝘹𝘪𝘴𝘵𝘪𝘯𝘨 𝘤𝘰𝘶𝘯𝘵𝘺 𝘪𝘯 𝘵𝘩𝘦 𝘤𝘰𝘶𝘯𝘵𝘺 𝘭𝘪𝘴𝘵.
  if county_name not in counties_list:

      # 𝘈𝘥𝘥 𝘵𝘩𝘦 𝘦𝘹𝘪𝘴𝘵𝘪𝘯𝘨 𝘤𝘰𝘶𝘯𝘵𝘺 𝘵𝘰 𝘵𝘩𝘦 𝘭𝘪𝘴𝘵 𝘰𝘧 𝘤𝘰𝘶𝘯𝘵𝘪𝘦𝘴.
      counties_list.append(county_name)

      # 𝘉𝘦𝘨𝘪𝘯 𝘵𝘳𝘢𝘤𝘬𝘪𝘯𝘨 𝘵𝘩𝘦 𝘤𝘰𝘶𝘯𝘵𝘺'𝘴 𝘷𝘰𝘵𝘦 𝘤𝘰𝘶𝘯𝘵.
      county_votes[county_name] = 0

      # 𝘈𝘥𝘥 𝘢 𝘷𝘰𝘵𝘦 𝘵𝘰 𝘵𝘩𝘢𝘵 𝘤𝘰𝘶𝘯𝘵𝘺'𝘴 𝘷𝘰𝘵𝘦 𝘤𝘰𝘶𝘯𝘵.
      county_votes[county_name] += 1
```

## Challenge Overview
The most important aspect was to maintain the integrity of the data; to ensure that each vote was counted and counted correctly. 


## Challenge Summary
This was a straightforward assignment that did not pose any significant challenges. By using Python and Visual Studio Code, we were able to read the data and process the counts with 100% accuracy. In addition, these resources generated the outcome immediately and the code easily outlines the steps taken to retrieve the results. This kind of transparency is imperative when auditing election results. 

