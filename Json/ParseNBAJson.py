import ijson
from Court import Court
import zipfile


class ParseNBAJson:
    Season_2017_2018_File = 'toronto_raptors_play_by_play_2017-2018.json'
    Season_2018_2019_File = 'toronto_raptors_play_by_play_2018-2019.json'
    Standing_Season_2017_File = "Data/standing_season_2017.json"
    Standing_Season_2018_File = "Data/standing_season_2018.json"
    Player_Siakam_File = 'Data/Pascal_Siakam.json'
    Player_DeRozan_File = 'Data/DeMar_DeRozan.json'
    Player_Leonard_File = 'Data/Kawhi_Leonard.json'
    Player_Siakam = 'Pascal Siakam'
    Player_Leonard = 'Kawhi Leonard'
    Player_DeRozan = 'DeMar DeRozan'
    Player_Peoltl = 'Jakob Poeltl'
    Player_Green = 'Danny Green'
    event_types = ('threepointmade', 'threepointmiss', 'twopointmade', 'twopointmiss')
    event_types_missed = ('threepointmiss', 'twopointmiss')
    event_types_made = ('threepointmade', 'twopointmade')
    __team_name = 'Raptors'

    def get_season_shot_chart_as_coordinates(self, season, event_types):
        coordinates = {'x': list(), 'y': list()}

        return self.__json_parse_season(season, event_types, coordinates, self.__season_per_team)

    def get_season_shot_chart_per_area(self, season, event_types):
        area_data = {'underbasket': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'inthepaint': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'insiderightwing': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'insideright': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'insidecenter': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'insideleft': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'insideleftwing': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'outsiderightwing': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'outsideright': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'outsidecenter': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'outsideleft': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'outsideleftwing': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'backcourt': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0}}

        return self.__json_parse_season(season, event_types, area_data, self.__season_per_area)

    def get_season_shot_chart_per_area_and_player(self, season, event_types, player):
        area_data = {'underbasket': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'inthepaint': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'insiderightwing': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'insideright': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'insidecenter': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'insideleft': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'insideleftwing': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'outsiderightwing': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'outsideright': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'outsidecenter': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'outsideleft': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'outsideleftwing': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0},
                     'backcourt': {'x': list(), 'y': list(), 'number': 0, 'made': 0, 'missed': 0}}

        return self.__json_parse_season(season, event_types, area_data, self.__season_per_area_and_player, player)

    def get_season_player_shot_chart_as_coordinates(self, season, player, event_types):
        coordinates = {'x': list(), 'y': list()}

        return self.__json_parse_season(season, event_types, coordinates, self.__season_per_player, player)

    def get_standing_total_games(self, season):
        retval = 0
        return self.__json_parse_standing(season, retval, self.__standing_number_games)

    def get_standing_wins(self, season):
        retval = 0
        return self.__json_parse_standing(season, retval, self.__standing_team_wins, self.__team_name)

    def get_standing_losses(self, season):
        retval = 0
        return self.__json_parse_standing(season, retval, self.__standing_team_losses, self.__team_name)

    def get_standing_number_teams(self, season):
        retval = 0
        return self.__json_parse_standing(season, retval, self.__standing_teams)

    def __json_parse_season(self, season, event_types, retval, filter_method, player=None):
        # read the team json from the zipfile
        archive = zipfile.ZipFile('Data/toronto_raptors_play_by_play.zip', 'r')
        objs = ijson.items(archive.read(season), '')

        # iterate the whole json
        for games in objs:
            for game in games:
                for periode in game['periods']:
                    for event in periode['events']:
                        # select only the events we are interested in
                        if str(event['event_type']) in event_types:
                            # check if location exist in the events
                            if 'location' in event:
                                for stat in event['statistics']:
                                    if player is None:
                                        filter_method(stat, event, retval)
                                    else:
                                        filter_method(stat, event, retval, player)
        return retval

    def __json_parse_standing(self, season, retval: int, filter_method, teamname=None):
        # read the standing json file
        with open(season) as input_file:
            objs = ijson.items(input_file, '')

            # iterate the whole json
            for games in objs:
                for conference in games['conferences']:
                    for division in conference['divisions']:
                        for team in division['teams']:
                            if teamname is None:
                                retval = retval + filter_method(team)
                            else:
                                retval = retval + filter_method(team, teamname)
        if teamname is None:
            return int(retval/2)
        else:
            return retval

    # filter the data for one season per given player
    # return the coordinates from each shot
    def __season_per_player(self, stat, event, retval, player):
        # read only the plays from __team_name and the given player
        if self.__team_name in stat['team']['name'] and player in stat['player']['full_name']:
            x = int(event['location']['coord_x'])
            # swap the data from one end of the field to the other
            if x > (Court.Court.Court_Max_Length/2):
                x = Court.Court.Court_Max_Length - x

            # store the coordinates in a dictonary
            retval['x'].append(x)
            retval['y'].append(event['location']['coord_y'])

    # filter the data for one season per team
    # return the coordinates from each shot
    def __season_per_team(self, stat, event, retval):
        # read only the plays from __team_name and the given player
        if self.__team_name in stat['team']['name']:
            x = int(event['location']['coord_x'])
            # swap the data from one end of the field to the other
            if x > (Court.Court.Court_Max_Length/2):
                x = Court.Court.Court_Max_Length - x

            # store the coordinates in a dictonary
            retval['x'].append(x)
            retval['y'].append(event['location']['coord_y'])

    # filter the data for one season per team
    # return the coordinates from each shot
    def __season_per_area(self, stat, event, retval):
        # read only the plays from __team_name and the given player
        if self.__team_name in stat['team']['name']:
            dict = retval[event['location']['action_area']]
            x = int(event['location']['coord_x'])
            # swap the data from one end of the field to the other
            if x > (Court.Court.Court_Max_Length/2):
                x = Court.Court.Court_Max_Length - x

            # store the coordinates in a dictonary
            dict['x'].append(x)
            dict['y'].append(event['location']['coord_y'])
            dict['number'] = dict['number'] + 1

            if event['event_type'] in self.event_types_missed:
                dict['missed'] = dict['missed'] + 1
            elif event['event_type'] in self.event_types_made :
                dict['made'] = dict['made'] + 1

    # filter the data for one season per team and player
    # return the coordinates from each shot
    def __season_per_area_and_player(self, stat, event, retval, player):
        # read only the plays from __team_name and the given player
        if self.__team_name in stat['team']['name'] and player in stat['player']['full_name']:
            dict = retval[event['location']['action_area']]
            x = int(event['location']['coord_x'])
            # swap the data from one end of the field to the other
            if x > (Court.Court.Court_Max_Length/2):
                x = Court.Court.Court_Max_Length - x

            # store the coordinates in a dictonary
            dict['x'].append(x)
            dict['y'].append(event['location']['coord_y'])
            dict['number'] = dict['number'] + 1

            if event['event_type'] in self.event_types_missed:
                dict['missed'] = dict['missed'] + 1
            elif event['event_type'] in self.event_types_made :
                dict['made'] = dict['made'] + 1

    # calculate all games
    def __standing_number_games(self, team):
        # add wins und losses together for each team
        return int(team['wins']) + int(team['losses'])

    # get wins per team
    def __standing_team_wins(self, team, teamname):
        # add wins und losses together for each team
        if team['name'] == teamname:
            return int(team['wins'])
        else:
            return 0

    # get wins per team
    def __standing_team_losses(self, team, teamname):
        # add wins und losses together for each team
        if team['name'] == teamname:
            return int(team['losses'])
        else:
            return 0

    # calculate number of teams
    def __standing_teams(self, team):
        return 2
