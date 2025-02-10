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

player_name = "kalaka0314"
print(f"\nWelcome, {player_name}! You’ve entered the arena of champions!")
print("Every champion has a homeland!\n")
for index in range(1, len(teams_by_country.keys())):
    print(f"{index} - {list(teams_by_country.keys())[index - 1]}")

country_selection = input("\nType the country of your favorite team to continue: ")

print()
counter_teams = 1
for team in teams_by_country[country_selection]:
    print(f"{counter_teams} - {team}")
    counter_teams += 1
print()

player_team = input("It's time to reveal your loyalty! Type the name of your favorite team: ")

print(f"\nA champion has spoken!, {player_name} stands with {player_team}!\n")






