from Json import ParseNBAJson
import math

parser = ParseNBAJson.ParseNBAJson()
season = ParseNBAJson.ParseNBAJson.Standing_Season_2017_File
#season = ParseNBAJson.ParseNBAJson.Standing_Season_2018_File
#season = ParseNBAJson.ParseNBAJson.Standing_Season_2019_File
total_games = parser.get_standing_total_games(season)
wins = parser.get_standing_wins(season)
losses = parser.get_standing_losses(season)
teams = parser.get_standing_number_teams(season)
games = wins + losses

nags = (teams * games)/2
win_rate = wins / games
game_coin_toss = math.sqrt(0.5 * (0.5 / nags))
real = win_rate
luck = game_coin_toss
skill = real - luck

print("luck:  " + str(luck))
print("skill: " + str(skill))
print("contribution luck:  " + str(luck / real))
print("contribution skill: " + str(skill / real))


