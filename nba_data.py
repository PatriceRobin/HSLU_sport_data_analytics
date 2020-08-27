from Court import Court
from Json import ParseNBAJson
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import numpy as np
import seaborn as sns


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