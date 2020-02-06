import operator
import collections
import sys

#User enters file line of input as n m k which gets split into the different variables
n, m, k = input("Enter number of teams, matches and stadiums: ").split(' ')

#User enters second line of input as value1 value2 value3......valuen which gets split as an array
money = input("Enter amount of money earned per team in the order of the teams: ").split(' ')

#Defining an empty array to get the list of matches played between the teams.
matches_list = []

#If the number of matches provided was 0 because 𝑛, 𝑚, 𝑘 (3≤𝑛≤100, 0≤𝑚≤1000, 1≤𝑘≤1000), exit the script.
if int(m) == 0:
    print("Sorry. No matches this year :(")
    sys.exit(0)
for i in range(int(m)):
    #User enters team input as team1 team2 which gets split into a tuple which is further appended into the "matches_list"
    team1, team2 = input(f"Enter teams that play match {str(i+1)}: ").split(' ')
    matches_list.append((int(team1), int(team2)))

#It is guaranteed that each pair of teams can play at most one game hence not checking if input is unique

#Generating stadium numbers as an array
stadiums = [i for i in range(1, int(k)+1)]

#Sorting the matches played in the order of most valuable to least valuable matches based on the amount earned from the induvidual teams.
#Doing this will ensure that the matches with the most earning potential will not be left out in case that particular team cannot play all the given matches because of the "not exceeds 2" rule.
matches_on_revenue = {}
for match in matches_list:
    revenue = int(money[match[0]-1]) + int(money[match[1]-1])
    matches_on_revenue[match] = revenue
matches_on_revenue = sorted(matches_on_revenue.items(), key=operator.itemgetter(1), reverse=True)

#Making a note of matches played per stadium so far, number of times a team has played at a stadium and stadium assigned for each match.
#Initial values would be 0 or empty and will be updated as we loop through each match while assigning stadiums
matches_per_stadium = {i : 0 for i in stadiums}
teams_at_stadium = {i : [] for i in stadiums}
stadium_for_match = {i[0] : 0 for i in matches_on_revenue}

#Create a function which assigns stadiums for each match. The dictionary "stadium_for_match" will be passed to this fucntion
def assign_stadium(stadium_for_match):

    #looping through each match in the dictionary in the order of most valuable to least valuable match. Using Python 3.7 so expecting the order of the dictionary to be preserved.
    for key, value in stadium_for_match.items():
        #Assiging variable n to 0 as stadium has not yet been assigned
        n = 0

        #If a stadium is not yet assigned for a particular match, the fucntion will proceed with the logic for that match else it will skip to next match
        if not value:
            try:
                #Try to fetch a stadium where no matches have been played so far. The "matches per stadium" dictionary comes in handy for this
                stadium_no = list(matches_per_stadium.keys())[list(matches_per_stadium.values()).index(0)]

                #if stadium available, setting n to 1 as stadium has been found
                n=1
            except:

                #if no stadium has 0 matches played, sort the stadiums in the order of least to highest matches played and loop through each stadium
                stadiums_by_matches = sorted(matches_per_stadium.items(), key=operator.itemgetter(1))
                for stadium_by_match in stadiums_by_matches:
                    #Get the stadium number
                    stadium_no = stadium_by_match[0]

                    #For that stadium, find the team that has played the lowest number of matches and get the value of how many matches played by that team.
                    # Ignore the matches played by the teams that are present in the current match because even if we add them, it will be a plus one on both ends and so the difference will still be the same 
                    least_common = [i for i in collections.Counter(teams_at_stadium[stadium_no]).most_common() if i[0] != key[0] and i[0] != key[1]][-1][1]

                    #Check the following conditions
                    # 1a) If in current match, team1 has played a match in this stadium.
                    # 1b) If yes, whether the difference between number of matches played by team1 and the number of matches played by the team that has played the lowest in this stadium is less than 2.

                    # 2a) If in current match, team2 has played a match in this stadium.
                    # 2b) If yes, whether the difference between number of matches played by team2 and the number of matches played by the team that has played the lowest in this stadium is less than 2.

                    if ((teams_at_stadium[stadium_no].count(key[0]) == 0) or (abs(teams_at_stadium[stadium_no].count(key[0]) - least_common) < 2)) and ((teams_at_stadium[stadium_no].count(key[1]) == 0) or (abs(teams_at_stadium[stadium_no].count(key[1]) - least_common) < 2) ):
                        #If the above conditions are satisfied, pick this stadium and break the loop. Else move on to the next stadium.
                        n=1
                        break
        
        # If a stadium is found, assign it to the match.
        # Increment the value of this stadium in the "matches_per_stadium" dictionary by 1.
        # Add the team numbers in the match to the teams_at_stadium list of this stadium again.
        if n:
            stadium_for_match[key] = stadium_no
            matches_per_stadium[stadium_no] = matches_per_stadium[stadium_no] + 1
            teams_at_stadium[stadium_no].append(key[0])
            teams_at_stadium[stadium_no].append(key[1])
        #If no stadium is found for this match the value will remain 0.

        #Move to the next match.

    #Return the final dictionary and also if there were any stadiums found for any matches
    return stadium_for_match, n

#Initially assuming there were stadiums found for matches
n = 1
while n:
    #Call the assign stadium function till there were no changes made to any matches.
    #The reason for this instead of a single function call is:
        #Lets say a match was assigned value 0 because it could not fit into any stadium due to the "exceeds 2 rule"
        #After iterating thorugh the entire dictionary, it may be so that this difference had come down from 2. In those cases, there would be a stadium avalible for a match which was previously not available. 
    stadium_for_match, n = assign_stadium(stadium_for_match)

#Once the stadiums are finalized, print the output stadium numbers in the same order as the matches provided in the input.
for i in matches_list:
    print(stadium_for_match[i])