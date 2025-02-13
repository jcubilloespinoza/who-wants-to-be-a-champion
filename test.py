import random

player_team = 'Real Madrid'

group_A = ['Group A', 'Red Bull Salzburg', 'Juventus', 'Newcastle United', 'Young Boys']
group_B = ['Group B', 'Lazio', 'Real Madrid', 'Lens', 'Antwerp']
group_C = ['Group C', 'RB Leipzig', 'Paris Saint-Germain', 'Real Sociedad', 'Napoli']
group_D = ['Group D', 'Crvena zvezda', 'Benfica', 'Manchester City', 'PSV Eindhoven']
group_E = ['Group E', 'Braga', 'Feyenoord', 'Manchester United', 'Galatasaray']
group_F = ['Group F', 'Shakhtar Donetsk', 'Atlético Madrid', 'Bayern Munich', 'Porto']
group_G = ['Group G', 'Arsenal', 'Celtic', 'AC Milan', 'Sevilla']
group_H = ['Group H', 'Copenhagen', 'Borussia Dortmund', 'Barcelona', 'Inter Milan']

player_team_group_name = 'B'
player_team_group = ['Group B', 'Lazio', 'Real Madrid', 'Lens', 'Antwerp']
opponent_list = ['Lazio', 'Lens', 'Antwerp']
opponent_results = []

groups_stage = True
player_team_points = 0 #player team points for the group stage
match_counter = 1
print()
while groups_stage:
    for opponent in opponent_list:
        print(f"Match against: {opponent}")
        match_result = random.randint(0,1) #added to track results
        if match_result == 1:
            print("Win")
            player_team_points += 3
            opponent_points = 0
            print(f"\nPoints after this match: {player_team_points}")
            print("-" * 60)
            opponent_results.append([opponent, opponent_points])
        else:
            print("\nLoss")
            opponent_points = 3
            print(f"\nPoints after this match: {player_team_points}")
            print("-" * 60)            
            opponent_results.append([opponent, opponent_points])
    groups_stage = False

print(f"You get {player_team_points} points for the groups stage games.")
"""if player_team_points >= 6:
    print("\nYou have qualified for the Round of 16\n")
else:
    print("\nYou've been disqualified.\n")"""

#Code to generate the results for the matches between opponents:
print("\nOpponent matches:\n")

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


#Code to generate the Standings:
"""print("-"*10 + "Group" + " " + player_team_group_name + " " + "Standings" + " " + "-"*10)
for team in player_team_group[1:]:
    if team == player_team:
        print(f"{team} : {player_team_points}")
    else:
        if team == opponent_results[0][0]:
            print(f"{opponent_results[0][0]} : {opponent_results[0][1]}")
        elif team == opponent_results[1][0]:
            print(f"{opponent_results[1][0]} : {opponent_results[1][1]}")
        elif team == opponent_results[2][0]:
            print(f"{opponent_results[2][0]} : {opponent_results[2][1]}")
        else:
            print("Error")"""

standings = [[player_team, player_team_points], 
            [opponent_results[0][0], opponent_results[0][1]], 
            [opponent_results[1][0], opponent_results[1][1]], 
            [opponent_results[2][0], opponent_results[2][1]]]

# Defining a function to get the key for sorting
def get_key(team):
    return team[1]

# Sorting the list based on the second element of each sublist
sorted_stan = sorted(standings, key=get_key, reverse=True)

# Printing the sorted list
#print(sorted_stan)

print("-"*10 + "Group" + " " + player_team_group_name + " " + "Standings" + " " + "-"*10)
for team_data in sorted_stan:
    print(f"{team_data[0]}: {team_data[1]}")



