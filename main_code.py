import random  # Import the random module for random team selection

# Dictionary mapping countries to their respective teams
teams_by_country = {
    "England": ["Arsenal", "Manchester City", "Manchester United", "Newcastle United"], 
    "Spain": ["Atlético Madrid", "Barcelona", "Real Madrid", "Real Sociedad", "Sevilla"], 
    "Italy": ["Inter Milan", "Lazio", "AC Milan", "Napoli"],
    "Germany": ["Bayern Munich", "Borussia Dortmund", "RB Leipzig", "Union Berlin"],
    "France": ["Lens", "Paris Saint-Germain"],
    "Portugal": ["Benfica", "Braga", "Porto"],
    "Netherlands": ["Feyenoord", "PSV Eindhoven"],
    "Austria": ["Red Bull Salzburg"],
    "Scotland": ["Celtic"],
    "Serbia": ["Crvena zvezda"],
    "Ukraine": ["Shakhtar Donetsk"],
    "Belgium": ["Antwerp"],
    "Switzerland": ["Young Boys"],
    "Denmark": ["Copenhagen"],
    "Turkey": ["Galatasaray"] 
}

# Placeholder for the player's name
player_name = "kalaka0314"
print(f"\nWelcome, {player_name}! You’ve entered the arena of champions!")
print("Every champion has a homeland!\n")

# Display available countries to choose from
for index in range(1, len(teams_by_country.keys())):
    print(f"{index} - {list(teams_by_country.keys())[index - 1]}")

# Prompt player to select a country
country_selection = input("\nType the country of your favorite team to continue: ")

print()

# Display teams from the chosen country
counter_teams = 1
for team in teams_by_country[country_selection]:
    print(f"{counter_teams} - {team}")
    counter_teams += 1
print()

# Prompt player to select a team
player_team = input("It's time to reveal your loyalty! Type the name of your favorite team: ")

print(f"\nA champion has spoken!, {player_name} stands with {player_team}!")
print("It’s time for the big draw! Let’s determine the groups for the group stage!")

# Create a list of all 32 teams
group_stage_teams = []
for country_teams in teams_by_country.values():
    for team in country_teams:
        group_stage_teams.append(team)
    
# List to track used indexes to avoid duplicates
used_index_list = []

# Initialize groups
group_A = ["Group A"]
group_B = ["Group B"]
group_C = ["Group C"]
group_D = ["Group D"]
group_E = ["Group E"]
group_F = ["Group F"]
group_G = ["Group G"]
group_H = ["Group H"]

groups = [group_A, group_B, group_C, group_D, group_E, group_F, group_G, group_H]

# Flag to control the random team assignment loop
ACTIVE = True

group_stage_teams_counter = 1  # Counter for team assignment tracking

# Randomly distribute teams into 8 groups
while ACTIVE:
    if len(used_index_list) < 32:
        index = random.randint(1, 32)  # Generate a random index between 1 and 32
        
        if index in used_index_list:
            continue  # Skip if the index has already been used
        else:
            used_index_list.append(index)  # Add to used index list
            
            # Assign teams to groups based on the number of selected teams
            if len(used_index_list) <= 4:
                group_A.append(group_stage_teams[index-1])
            elif 4 < len(used_index_list) <= 8:
                group_B.append(group_stage_teams[index-1])
            elif 8 < len(used_index_list) <= 12:
                group_C.append(group_stage_teams[index-1])
            elif 12 < len(used_index_list) <= 16:
                group_D.append(group_stage_teams[index-1])
            elif 16 < len(used_index_list) <= 20:
                group_E.append(group_stage_teams[index-1])
            elif 20 < len(used_index_list) <= 24:
                group_F.append(group_stage_teams[index-1])
            elif 24 < len(used_index_list) <= 28:
                group_G.append(group_stage_teams[index-1])
            elif 28 < len(used_index_list) <= 32:
                group_H.append(group_stage_teams[index-1])
            else:
                print("ERROR")
            
            print(f"{group_stage_teams_counter} - {group_stage_teams[index-1]}")
            group_stage_teams_counter += 1  # Increment counter
    else:
        ACTIVE = False  # Stop loop when all teams have been assigned

# Print out the final groups
print()
for group in groups:
    print("-"*10 + group[0] + " " + "-"*10)
    for team in group[1:]:  # Skip group name when printing teams
        if team == player_team: # If the team is the player's chosen team, add an identifier "*" before its name.
            print(f"* {team}")
        else:
            print(f"{team}")

# Uncomment the lines below for debugging purposes to view groups
"""
print(group_A)
print(group_B)
print(group_C)
print(group_D)
print(group_E)
print(group_F)
print(group_G)
print(group_H)
"""
