# Election_Analysis

## Project Overview
I was given the task of auditing an election from the Colorado Board of Elections for a local congressional election. I was tasked with counting the total number of votes cast, votes by county in both percentage and total number, votes by candidate in both percentage and total number, the winner of the election in both percentage and total number and the county with the largest turnout.  

## Resources
I was given the following resources to utilize:
- Data Source: election_results.csv
- Software: Python 3.8.5, Visual Studio Code, 1.55.0

## Summary
My analysis concluded that:
1. There were 369,711 votes cast in this congressional election.

2. The candidates were:
   * Charles Casper Stockham
   * Diana DeGette
   * Raymond Anthony Doane

3. The candidate results were:
   * Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
   * Diana DeGette received 73.8% of the vote and 272,892 number of votes.
   * Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.

4. The winner of the election was:
  - Diana Degette, who received 73.8% of the vote and 272,892 number of votes.

## Challenge Overview

### Election-Audit Results

Continuing my audit to the county level:
 - Denver County had the largest number of votes with 82.8% of the vote and 306,055 number of votes.
 - Jefferson County had 10.5% of the vote and 38,855 number of votes.
 - Arapahoe County had 6.7% of the vote and 24,801 number of votes. 

![election_results.png](analysis/election_results.png)

## Challenge Summary

To conclude, this script can be used for any local election and at the state level.  It is flexible enough to be changed to accommodate any level of election and easy enough to be implemented to calculate any results.  

The following code can be changed to retrieve data found in the csv file and iterated to calculate percentage points.

![interchangeable_code.png](analysis/interchangeable_code.png)

Additionally, this code can be modified to calculate the winning object and give its count. 

![interchangeable_results.png](analysis/interchangeable_results.png)

With these two scripts, I can change the variables to count, sum and give a percentile of a specific piece of data that is found in the csv file.  Furthermore, with just minimal input, I can modify the output to audit any number of elections across the state.  
