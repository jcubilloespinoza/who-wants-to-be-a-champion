import data
import random

def welcome_message(name):
    # Prints a personalized welcome message with the player's name.
    print(f"\nWelcome, {name}! You’ve entered the arena of champions!")

    # Displays an additional message about the origin of each champion.
    print("Every champion has a homeland!\n")

def country_selection():
    # Initialize a counter for country selection numbering.
    country_selection_counter = 1

    # Iterate through the list of countries in data.teams_by_country.
    for country in data.teams_by_country:
        # Print each country with a corresponding number.
        print(f"{country_selection_counter} - {country}")

        # Increment the counter for the next country.
        country_selection_counter += 1

def team_selection():
    # Store the selected team in a global variable
    global player_team    
    # Prompt player to select a country by entering a number
    country_selection_number = int(input("\nType the country of your favorite team to continue: "))
    
    # Convert the dictionary keys (country names) into a list for indexing
    countries = list(data.teams_by_country.keys())

    # Access the selected country using the provided number (adjusting for zero-based indexing)
    player_country = countries[country_selection_number - 1]  # Example: "England"
    
    # Retrieve the list of teams from the selected country
    teams_in_player_country = data.teams_by_country[player_country]  # Example: ["Arsenal", "Manchester City", "Manchester United", "Newcastle United"]

    # Display the selected country
    print(f"\nSelected country: {player_country}\n")

    # Initialize a counter for team selection numbering
    team_selection_counter = 1 
    teams_in_player_country_list = []

    # Iterate through the teams in the selected country and display them with corresponding numbers
    for team in teams_in_player_country:
        print(f"{team_selection_counter} - {team}")
        teams_in_player_country_list.append(team)  # Store the team in a list for selection
        team_selection_counter += 1
    
    # Prompt player to select their favorite team by entering a number
    player_team_selection_number = int(input("\nWhat is your favorite team?: "))
    player_team = teams_in_player_country_list[player_team_selection_number - 1]

    # Display the selected team
    print(f"\nSelected Team: {player_team}\n")

    # Announce the start of the group stage draw
    print("It’s time for the big draw! Let’s determine the groups for the group stage!")

    # Wait for the player to press Enter before proceeding
    input("\nHit Enter to continue! ")

def group_generator():
    global player_group
    global player_team_group_name
    global groups
    # Create a list of all 32 teams
    group_stage_teams = []

    for country_teams in data.teams_by_country.values():
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
                
                group_stage_teams_counter += 1  # Increment counter
        else:
            ACTIVE = False  # Stop loop when all teams have been assigned

    # Print out the final groups
    print()
    for group in groups:
        print("-"*10 + group[0] + "-"*10)
        for team in group[1:]:  # Skip group name when printing teams
            if team == player_team:  # If the team is the player's chosen team, add an identifier "*" before its name.
                print(f"* {team}")
            else:
                print(f"{team}")

    # Find and display the player's team group
    for group in groups:
        if player_team in group:  # Loop through groups to find the player's team
            player_team_group_name = group[0]  # Store the group name
            player_team_group = group  # Store the group itself
            print(f"\n\nYour team: {player_team} has been assigned to {group[0]}!")
            player_group = group  # Assign the found group to player_group

    input("\n\nLet's generate the group stage matches. Press Enter to continue. \n")

def R32_match_generator():
    # Generate matches for the player's group
    global opponent_list  # Declare global variable to store opponents
    
    opponent_counter = 1  # Counter for match numbering
    opponent_list = []  # List to store opponents
    
    print("\n")  # Print a blank line for formatting
    
    # Iterate through the teams in the player's group, excluding the group name
    for opponent in player_group[1:]:  
        if opponent != player_team:  # Ensure the player's team is not included as an opponent
            print(f"Match #{opponent_counter}: {opponent}")  # Display match number and opponent
            opponent_list.append(opponent)  # Add opponent to the list
            opponent_counter += 1  # Increment match counter
    
    print("\n")  # Print a blank line for formatting

def groups_stage():
    global opponent_results
    global player_team_points

    # Select a random question index
    question_number = random.randint(1, 10)
    groups_stage = True
    player_team_points = 0
    match_counter = 1
    opponent_results = []

    print("-" * 60)

    while groups_stage:
        for opponent in opponent_list:
            oponnent_question_index = 1
            print(f"\nMatch against: {opponent}\n")
            print(data.questions[opponent][question_number - 1][1])
            print("\n")
            
            # Display answer choices
            for option in data.questions[opponent][question_number - 1][2]:
                print(f"{oponnent_question_index} - {option}")
                oponnent_question_index += 1
            print("\n")

            # Display correct answer (debugging or test purpose)
            print(f"Answer: {data.questions[opponent][question_number - 1][3]}")
            
            # Get player input
            answer = int(input("Type your answer: "))
            print(f"Your Answer: {data.questions[opponent][question_number - 1][2][answer - 1]}")
            
            # Check if answer is correct
            if data.questions[opponent][question_number - 1][2][answer - 1] == data.questions[opponent][question_number - 1][3]:
                print("\nWin")
                player_team_points += 3  # Win gives 3 points
                opponent_points = 0  # Losing team gets 0 points
            else:
                print("\nLoss")
                opponent_points = 3  # Loss means opponent gets 3 points

            print(f"\nPoints after this match: {player_team_points}")
            print("-" * 60)

            # Store opponent's match result
            opponent_results.append([opponent, opponent_points])
        
        groups_stage = False  # Exit loop after all matches are played

    print(f"You get {player_team_points} points for the group stage games.")
    input("Press Enter to reveal the opponent's match results!")

def group_match_results_generator():
    # Generate match results between opponents
    print("-" * 60)

    # First match between first two opponents
    result = random.choice([0, 1])  # Randomly choose a winner
    if result == 0:
        winner = opponent_results[0][0]
        opponent_results[0][1] += 3  # Winner gets 3 points
    else:
        winner = opponent_results[1][0]
        opponent_results[1][1] += 3
    print(f"{opponent_results[0][0]} vs {opponent_results[1][0]}")
    print(f"Winner: {winner}\n")

    # Second match between first and third opponent
    result = random.choice([0, 2])
    if result == 0:
        winner = opponent_results[0][0]
        opponent_results[0][1] += 3
    else:
        winner = opponent_results[2][0]
        opponent_results[2][1] += 3
    print(f"{opponent_results[0][0]} vs {opponent_results[2][0]}")
    print(f"Winner: {winner}\n")

    # Third match between second and third opponent
    result = random.choice([1, 2])
    if result == 1:
        winner = opponent_results[1][0]
        opponent_results[1][1] += 3
    else:
        winner = opponent_results[2][0]
        opponent_results[2][1] += 3
    print(f"{opponent_results[1][0]} vs {opponent_results[2][0]}")
    print(f"Winner: {winner}\n")

def standing_table_generator():
    global sorted_stan
    
    # Generate and sort the standings table based on points
    standings = [[player_team, player_team_points], 
                [opponent_results[0][0], opponent_results[0][1]], 
                [opponent_results[1][0], opponent_results[1][1]], 
                [opponent_results[2][0], opponent_results[2][1]]]

    # Key function to sort based on points
    def get_key(team):
        return team[1]  # Sorting based on points

    # Sort standings in descending order of points
    sorted_stan = sorted(standings, key=get_key, reverse=True)

    input("Press Enter to display the final group standings...")
    
    # Display the final group standings
    print("-"*10 + player_team_group_name + " " + "Standings" + " " + "-"*10)
    for team_data in sorted_stan:
        print(f"{team_data[0]}: {team_data[1]}")
    print("-"*38)

def R16():
    # Logic for determining teams advancing to the Round of 16
    # The top two teams from each group qualify

    global R16_matches
    global R16_opponent_list
    global R16_player_result
    R16 = []  # List to store Round of 16 qualified teams

    # Determine the two qualified teams from each group
    for group in groups:
        qualified_1 = random.randint(1, 2)
        qualified_2 = random.randint(3, 4)    
        if group[0] == player_team_group_name:
            # Always include player's team if it's in the group
            R16.append(sorted_stan[0][0])
            R16.append(sorted_stan[1][0])
        else:
            R16.append(group[qualified_1])     
            R16.append(group[qualified_2])           

    # Printing Round of 16 qualified teams
    input("Press Enter to display the qualified teams for the Round of 16! ")
    R16_index = 1
    print("\nRound of 16 Qualified Teams: \n")
    for team in R16:
        print(f"{R16_index} - {team}")
        R16_index += 1
    print()

    # Generating Round of 16 matchups
    R16_matches = []
    input("Press Enter to display the matchups for the Round of 16! ")
    print("Round of 16 Matchups:\n")
    for index in range(int(len(R16)/2)):
        print(f"{index + 1 } - {R16[index]} vs {R16[len(R16) - index - 1]}")
        R16_matches.append([R16[index], R16[len(R16) - index - 1]])

    print()

    # List to store the opponents for the player's team
    R16_opponent_list = []

    # Check if the player's team is in any of the matchups
    for match in R16_matches:
        if match[0] == player_team or match[1] == player_team:
            if match[0] == player_team:
                R16_opponent_list.append(match[1])
            else:
                R16_opponent_list.append(match[0])
        else:
            continue

    # Set random question number for R16 matches
    R16_question_number = random.randint(1,10)

    # R16 match stage loop
    R16_stage = True
    while R16_stage:
        for opponent in R16_opponent_list:
            oponnent_question_index = 1            
            print(f"\nMatch against: {opponent}\n")
            print(data.questions[opponent][R16_question_number - 1][1])
            print("\n")
            for option in data.questions[opponent][R16_question_number - 1][2]:
                print(f"{oponnent_question_index} - {option}")
                oponnent_question_index += 1
            print("\n")

            # Display the correct answer
            print(f"Answer: {data.questions[opponent][R16_question_number - 1][3]}")
            answer = int(input("Type your answer: "))
            print(f"Your Answer: {data.questions[opponent][R16_question_number - 1][2][answer - 1]}")
            if data.questions[opponent][R16_question_number - 1][2][answer - 1] == data.questions[opponent][R16_question_number - 1][3]:
                R16_player_result = True
                print("\nWin")
                print(f"\nYou advance to the next round.")
            else:
                R16_player_result = False
                print("\nLoss")
                print(f"\nYou've been disqualified")
                player_team_status = False
            
            print("-" * 60)
        
        R16_stage = False

def R8():
    # Initialize an empty list to store teams advancing to Round of 8 (R8)
    global R8_matches
    global R8_opponent_list
    global R8_player_result

    R8 = []

    # Loop through all Round of 16 (R16) matches
    for match in R16_matches:
        # Check if the player_team is in the current match
        if match[0] == player_team or match[1] == player_team:
            # If player_team is the first team, add the opponent to the opponent list
            if match[0] == player_team:
                R16_opponent_list.append(match[1])
            else:
                # If player_team is the second team, add the opponent to the opponent list
                R16_opponent_list.append(match[0])
        else:
            continue

    # Print an empty line for clarity
    print()

    # Loop through all Round of 16 (R16) matches again to determine who advances to Round 8 (R8)
    for match in R16_matches:
        # Check if player_team is in the current match
        if match[0] == player_team or match[1] == player_team:
            # If player_team won, add it to the R8 list
            if R16_player_result == True:
                R8.append(player_team)
            else:
                # If player_team lost, add the opponent from the opponent list
                R8.append(R16_opponent_list[0])
        else:
            # For other matches, randomly determine the winner between the two teams
            R16_match_winner = random.randint(0, 1)
            # Add the winner to the R8 list
            R8.append(match[R16_match_winner])

    # Printing Round of 8 qualified teams
    input("Press Enter to display the qualified teams for the Quarter-Finals! ")
    R8_index = 1
    print("\nQuarter-Finals qualified Teams: \n")
    for team in R8:
        print(f"{R8_index} - {team}")
        R8_index += 1
    print()

    # Generating Round of 8 matchups
    input("Press Enter to display the matchups for the Quarter-Finals! ")
    R8_matches = []
    print("Quarter-Finals Matchups:\n")
    for index in range(int(len(R8)/2)):
        print(f"{index + 1 } - {R8[index]} vs {R8[len(R8) - index - 1]}")
        R8_matches.append([R8[index], R8[len(R8) - index - 1]])

    print()

    R8_opponent_list = []

    # Checking if the player's team is in any of the Round of 8 matchups
    for match in R8_matches:
        if match[0] == player_team or match[1] == player_team:
            if match[0] == player_team:
                R8_opponent_list.append(match[1])
            else:
                R8_opponent_list.append(match[0])
        else:
            continue

    # Set random question number for R8 matches
    R8_question_number = random.randint(1,10)

    # R8 match stage loop
    R8_stage = True
    while R8_stage:
        for opponent in R8_opponent_list:
            oponnent_question_index = 1            
            print(f"\nMatch against: {opponent}\n")
            print(data.questions[opponent][R8_question_number - 1][1])
            print("\n")
            for option in data.questions[opponent][R8_question_number - 1][2]:
                print(f"{oponnent_question_index} - {option}")
                oponnent_question_index += 1
            print("\n")

            # Display the correct answer
            print(f"Answer: {data.questions[opponent][R8_question_number - 1][3]}")
            answer = int(input("Type your answer: "))
            print(f"Your Answer: {data.questions[opponent][R8_question_number - 1][2][answer - 1]}")
            if data.questions[opponent][R8_question_number - 1][2][answer - 1] == data.questions[opponent][R8_question_number - 1][3]:
                R8_player_result = True
                print("\nWin")
                print(f"\nYou advance to the next round.")
            else:
                R8_player_result = False
                print("\nLoss")
                print(f"\nYou've been disqualified")
                player_team_status = False

            print("-" * 60)
        
        R8_stage = False

def R4():
    # Initialize an empty list to store teams advancing to Round of 4 (R4)
    global R4_matches
    global R4_opponent_list
    global R4_player_result
    R4 = []

    # Loop through all Round of 4 (R4) matches
    for match in R8_matches:
        # Check if the player_team is in the current match
        if match[0] == player_team or match[1] == player_team:
            # If player_team is the first team, add the opponent to the opponent list
            if match[0] == player_team:
                R8_opponent_list.append(match[1])
            else:
                # If player_team is the second team, add the opponent to the opponent list
                R8_opponent_list.append(match[0])
        else:
            continue

    # Print an empty line for clarity
    print()

    # Loop through all Round of 8 (R8) matches to determine who advances to Round 4 (R4)
    for match in R8_matches:
        # Check if player_team is in the current match
        if match[0] == player_team or match[1] == player_team:
            # If player_team won, add it to the R4 list
            if R8_player_result == True:
                R4.append(player_team)
            else:
                # If player_team lost, add the opponent from the opponent list
                R4.append(R8_opponent_list[0])
        else:
            # For other matches, randomly determine the winner between the two teams
            R8_match_winner = random.randint(0, 1)
            # Add the winner to the R4 list
            R4.append(match[R8_match_winner])

    # Printing Round of 4 qualified teams
    input("Press Enter to display the qualified teams for the Semi-Finals! ")
    R4_index = 1
    print("\nSemi Finals Qualified Teams: \n")
    for team in R4:
        print(f"{R4_index} - {team}")
        R4_index += 1
    print()

    # Generating Round of 4 matchups
    input("Press Enter to display the Semi-Finals matchups! ")
    R4_matches = []
    print("Semi Final Matchups:\n")
    for index in range(int(len(R4)/2)):
        print(f"{index + 1 } - {R4[index]} vs {R4[len(R4) - index - 1]}")
        R4_matches.append([R4[index], R4[len(R4) - index - 1]])

    print()

    R4_opponent_list = []

    # Checking if the player's team is in any of the Round of 4 matchups
    for match in R4_matches:
        if match[0] == player_team or match[1] == player_team:
            if match[0] == player_team:
                R4_opponent_list.append(match[1])
            else:
                R4_opponent_list.append(match[0])
        else:
            continue

    # Set random question number for R4 matches
    R4_question_number = random.randint(1,10)

    # R4 match stage loop
    R4_stage = True
    while R4_stage:
        for opponent in R4_opponent_list:
            oponnent_question_index = 1            
            print(f"\nMatch against: {opponent}\n")
            print(data.questions[opponent][R4_question_number - 1][1])
            print("\n")
            for option in data.questions[opponent][R4_question_number - 1][2]:
                print(f"{oponnent_question_index} - {option}")
                oponnent_question_index += 1
            print("\n")

            # Display the correct answer
            print(f"Answer: {data.questions[opponent][R4_question_number - 1][3]}")
            answer = int(input("Type your answer: "))
            print(f"Your Answer: {data.questions[opponent][R4_question_number - 1][2][answer - 1]}")
            if data.questions[opponent][R4_question_number - 1][2][answer - 1] == data.questions[opponent][R4_question_number - 1][3]:
                R4_player_result = True
                print("\nWin")
                print(f"\nYou advance to the next round.")
            else:
                R4_player_result = False
                print("\nLoss")
                print(f"\nYou've been disqualified")
                player_team_status = False

            print("-" * 60)
        
        R4_stage = False

def R2():
    # Initialize an empty list to store teams advancing to Round of 2 (R2)
    R2 = []

    # Loop through all Round of 4 (R4) matches
    for match in R4_matches:
        # Check if the player_team is in the current match
        if match[0] == player_team or match[1] == player_team:
            # If player_team is the first team, add the opponent to the opponent list
            if match[0] == player_team:
                R4_opponent_list.append(match[1])
            else:
                # If player_team is the second team, add the opponent to the opponent list
                R4_opponent_list.append(match[0])
        else:
            continue

    # Print an empty line for clarity
    print()

    # Loop through all Round of 4 (R4) matches again to determine who advances to Round 2 (R2)
    for match in R4_matches:
        # Check if player_team is in the current match
        if match[0] == player_team or match[1] == player_team:
            # If player_team won, add it to the R2 list
            if R4_player_result == True:
                R2.append(player_team)
            else:
                # If player_team lost, add the opponent from the opponent list
                R2.append(R4_opponent_list[0])
        else:
            # For other matches, randomly determine the winner between the two teams
            R4_match_winner = random.randint(0, 1)
            # Add the winner to the R2 list
            R2.append(match[R4_match_winner])

    # Printing Round of 2 qualified teams
    input("Press Enter to display the qualified teams for the Final! ")
    R2_index = 1
    print("\nFinal Qualified Teams: \n")
    for team in R2:
        print(f"{R2_index} - {team}")
        R2_index += 1
    print()

    # Generating Round of 2 matchups
    R2_matches = []
    print("Final Match:\n")
    for index in range(int(len(R2)/2)):
        print(f"{index + 1 } - {R2[index]} vs {R2[len(R2) - index - 1]}")
        R2_matches.append([R2[index], R2[len(R2) - index - 1]])

    print()

    R2_opponent_list = []

    # Checking if the player's team is in any of the Round of 2 matchups
    for match in R2_matches:
        if match[0] == player_team or match[1] == player_team:
            if match[0] == player_team:
                R2_opponent_list.append(match[1])
            else:
                R2_opponent_list.append(match[0])
        else:
            continue

    # Set random question number for R2 matches
    R2_question_number = random.randint(1,10)

    # R2 match stage loop
    R2_stage = True
    opponent_question_index = 1
    while R2_stage:
        if len(R2_opponent_list) == 0:
            # Randomly choose the champion if there are no opponents left
            champion_index = random.randint(0,1) 
            print(f"The Champion is {R2[champion_index]}!!!!")
        else:    
            for opponent in R2_opponent_list:
                print(f"\nMatch against: {opponent}\n")
                print(data.questions[opponent][R2_question_number - 1][1])
                print("\n")
                for option in data.questions[opponent][R2_question_number - 1][2]:
                    print(f"{opponent_question_index} - {option}")
                    opponent_question_index += 1
                print("\n")
                print(f"Answer: {data.questions[opponent][R2_question_number - 1][3]}")
                answer = int(input("Type your answer: "))
                print(f"Your Answer: {data.questions[opponent][R2_question_number - 1][2][answer - 1]}")
                if data.questions[opponent][R2_question_number - 1][2][answer - 1] == data.questions[opponent][R2_question_number - 1][3]:
                    R2_player_result = True
                    print("\nWin")
                    print(f"\nYou are the Champion!!!!.")
                else:
                    R2_player_result = False
                    print("\nLoss")
                    print(f"\nYou've been disqualified")
                    print(f"\nThe Champion is {R2_opponent_list[0]}")
                player_team_status = False

                print("-" * 60)
        
        R2_stage = False

def play_again():
    # Prompt the user to decide if they want to play again
    new_game = input("\nDo you want to play again? (Y/N): ")
    
    # If the user wants to play again, do nothing and continue
    if new_game == "Y":
        pass
    else:
        # If the user doesn't want to play again, return "N" to indicate they are done
        return "N"
