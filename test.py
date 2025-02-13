import random  # Importing the random module to generate random match results

# Defining the player's team
player_team = 'Real Madrid'

# Defining the groups for the tournament
# Each group contains a name and four teams
# The player's team is in Group B

group_A = ['Group A', 'Red Bull Salzburg', 'Juventus', 'Newcastle United', 'Young Boys']
group_B = ['Group B', 'Lazio', 'Real Madrid', 'Lens', 'Antwerp']
group_C = ['Group C', 'RB Leipzig', 'Paris Saint-Germain', 'Real Sociedad', 'Napoli']
group_D = ['Group D', 'Crvena zvezda', 'Benfica', 'Manchester City', 'PSV Eindhoven']
group_E = ['Group E', 'Braga', 'Feyenoord', 'Manchester United', 'Galatasaray']
group_F = ['Group F', 'Shakhtar Donetsk', 'Atlético Madrid', 'Bayern Munich', 'Porto']
group_G = ['Group G', 'Arsenal', 'Celtic', 'AC Milan', 'Sevilla']
group_H = ['Group H', 'Copenhagen', 'Borussia Dortmund', 'Barcelona', 'Inter Milan']

# Assigning the player's group and listing its opponents
player_team_group_name = 'B'
player_team_group = ['Group B', 'Lazio', 'Real Madrid', 'Lens', 'Antwerp']
opponent_list = ['Lazio', 'Lens', 'Antwerp']
opponent_results = []  # List to store match results of opponents

groups_stage = True  # Boolean flag to control group stage execution
player_team_points = 0  # Player team's points counter
match_counter = 1  # Counter for matches

print()
while groups_stage:
    for opponent in opponent_list:
        print(f"Match against: {opponent}")
        match_result = random.randint(0,1)  # Randomly deciding match result (win or loss)
        if match_result == 1:
            print("Win")
            player_team_points += 3  # Win gives 3 points
            opponent_points = 0  # Losing team gets 0 points
        else:
            print("\nLoss")
            opponent_points = 3  # Loss means opponent gets 3 points
        
        print(f"\nPoints after this match: {player_team_points}")
        print("-" * 60)
        opponent_results.append([opponent, opponent_points])  # Storing result
    
    groups_stage = False  # End group stage after one iteration

print(f"You get {player_team_points} points for the group stage games.")

# Generating match results between opponents
print("\nOpponent matches:\n")

# Simulating opponent matches using random choice
result = random.choice([0, 1])
if result == 0:
    winner = opponent_results[0][0]
    opponent_results[0][1] += 3
else:
    winner = opponent_results[1][0]
    opponent_results[1][1] += 3
print(f"{opponent_results[0][0]} vs {opponent_results[1][0]}")
print(f"Winner: {winner}\n")

result = random.choice([0, 2])
if result == 0:
    winner = opponent_results[0][0]
    opponent_results[0][1] += 3
else:
    winner = opponent_results[2][0]
    opponent_results[2][1] += 3
print(f"{opponent_results[0][0]} vs {opponent_results[2][0]}")
print(f"Winner: {winner}\n")

result = random.choice([1, 2])
if result == 1:
    winner = opponent_results[1][0]
    opponent_results[1][1] += 3
else:
    winner = opponent_results[2][0]
    opponent_results[2][1] += 3
print(f"{opponent_results[1][0]} vs {opponent_results[2][0]}")
print(f"Winner: {winner}\n")

# Generating and sorting the standings table
standings = [[player_team, player_team_points], 
            [opponent_results[0][0], opponent_results[0][1]], 
            [opponent_results[1][0], opponent_results[1][1]], 
            [opponent_results[2][0], opponent_results[2][1]]]

def get_key(team):
    return team[1]  # Sorting based on points

sorted_stan = sorted(standings, key=get_key, reverse=True)  # Sorting standings in descending order

# Displaying final group standings
print("-"*10 + "Group" + " " + player_team_group_name + " " + "Standings" + " " + "-"*10)
for team_data in sorted_stan:
    print(f"{team_data[0]}: {team_data[1]}")
print("-"*38)

# Logic for determining teams advancing to the Round of 16
# The top two teams from each group qualify

groups = [group_A, group_B, group_C, group_D, group_E, group_F, group_G, group_H]

R16 = []  # List to store Round of 16 qualified teams

for group in groups:
    qualified_1 = random.randint(1, 2)
    qualified_2 = random.randint(3, 4)    
    if group[0] == f"Group {player_team_group_name}":
        R16.append(sorted_stan[0][0])
        R16.append(sorted_stan[1][0])
    else:
        R16.append(group[qualified_1])     
        R16.append(group[qualified_2])           

# Printing Round of 16 qualified teams
R16_index = 1
print("\nRound of 16 Qualified Teams: \n")
for team in R16:
    print(f"{R16_index} - {team}")
    R16_index += 1
print()

# Generating Round of 16 matchups
R16_matches = []
print("Round of 16 Matches:\n")
for index in range(int(len(R16)/2)):
    print(f"{index + 1 } - {R16[index]} vs {R16[len(R16) - index - 1]}")
    R16_matches.append([R16[index], R16[len(R16) - index - 1]])

print()
print(R16_matches)
print()

# Checking if the player's team is in any of the Round of 16 matchups
for match in R16_matches:
    if match[0] == player_team or match[1] == player_team:
        print(str(match) + " " + "Question Round" + " " + "<-----------------")
    else:
        print(match)
