import utils

player_team_status = True
while player_team_status:
    player_name = input("\nPlease enter your name: ")
    utils.welcome_message(player_name)
    utils.country_selection()
    utils.team_selection()
    utils.group_generator()
    utils.R32_match_generator()
    utils.groups_stage()
    utils.group_match_results_generator()
    utils.standing_table_generator()
    utils.R16()
    utils.R8()
    utils.R4()
    utils.R2()
    again = utils.play_again()
    if again:
        player_team_status = False


