from Court import Court
from Json import ParseNBAJson
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import numpy as np
import seaborn as sns


def centroid(vertexes, index):
    _list = [vertex [index] for vertex in vertexes]
    _len = len(vertexes)
    if index == 0:
        return 0.2 + (sum(_list) / _len) / 800
    elif index == 1:
        return 0.025 + (sum(_list) / _len) / 600
    return 0

court = Court.Court()
parser = ParseNBAJson.ParseNBAJson()
data = parser.get_season_shot_chart_per_area(ParseNBAJson.ParseNBAJson.Season_2017_2018_File, ParseNBAJson.ParseNBAJson.event_types)
# data = parser.get_season_shot_chart_as_coordinates(ParseNBAJson.ParseNBAJson.Season_2018_2019_File, ParseNBAJson.ParseNBAJson.event_types)
sns.set_style("white")
sns.set_color_codes()
#
# plt.figure(figsize=(12,11))
# plt.scatter(x=data['x'], y=data['y'])
# court.draw_court(outer_lines=True, with_areas=True)
# plt.show()

# court = Court.Court()
# parser = ParseNBAJson.ParseNBAJson()
# data = parser.get_season_shot_chart_as_coordinates(ParseNBAJson.ParseNBAJson.Season_2018_2019_File, ParseNBAJson.ParseNBAJson.event_types)
cmap = plt.cm.gist_heat_r
fig, ax = plt.subplots()
court.draw_court(ax, outer_lines=True)
patches: list = []
density = [data[rec]['number'] for rec in data.keys()]
density = np.array(list(map(float,density)))
colors = density / max(density)
p = PatchCollection(court.get_areas(patches, True), cmap = cmap)
p.set_array(colors)
ax.add_collection(p)
props = dict(boxstyle='round', facecolor='darkseagreen', alpha=0.75)
for key in data.keys():
    #print(key + ": " + str(centroid(court.Areas[key], 0)) + " / " + str(centroid(court.Areas[key], 1)))
    #print(str(data[key]['made']) + " / " + str(data[key]['number']))
    textstr = str(data[key]['made']) + ' / ' + str(data[key]['number']) + '\n' + str(round((100 / data[key]['number'] * data[key]['made']), 2)) + " %"
    ax.text(centroid(court.Areas[key], 0), centroid(court.Areas[key], 1), textstr, transform=ax.transAxes, fontsize=8, color='black', verticalalignment='top', bbox=props, zorder=15)
plt.show()

# joint_shot_chart = sns.jointplot(data['x'], data['y'], stat_func = None, kind = 'hex', space = 0, color = cmap(0.2), cmap = cmap)
#
# #cmap=plt.cm.YlOrRd_r
# #joint_shot_chart = sns.jointplot(data['x'], data['y'], stat_func=None, kind='kde', space=0, color=cmap(0.2), cmap=cmap, n_levels=50)
#
# joint_shot_chart.fig.set_size_inches(15, 15)
# ax = joint_shot_chart.ax_joint
# court.draw_court(ax, outer_lines = True, with_areas = True)
# ax.set_xlabel('')
# ax.set_ylabel('')
# ax.tick_params(labelbottom = 'off', labelleft = 'off')
# ax.set_title("Shot Chart 2018-2019 Reg. Season", y = 1, fontsize = 18)
# plt.show()