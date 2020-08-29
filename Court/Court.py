from matplotlib.patches import Circle, Rectangle, Arc, Polygon
import matplotlib.pyplot as plt
import numpy as np


class Court:
    Court_Max_Length = 1128
    Court_Max_Width = 600
    Areas = {"underbasket": ((48, 252), (77, 258), (111, 300), (77, 342), (48, 348)),
             "inthepaint": ((0, 204), (228, 204), (228, 396), (0, 396)),
             "insiderightwing": ((0, 36), (115, 36), (77, 204), (0, 204)),
             "insideright": ((115, 36), (245, 87), (309, 156), (225, 204), (77, 204)),
             "insidecenter": ((225, 204), (309, 156), (342, 223), (352, 300), (340, 385), (309, 445), (225, 396)),
             "insideleft": ((115, 564), (245, 513), (309, 445), (225, 396), (77, 396)),
             "insideleftwing": ((0, 564), (115, 564), (77, 396), (0, 396)),
             "outsiderightwing": ((0, 0), (122, 0), (115, 36), (0, 36)),
             "outsideright": ((122, 0), (492, 0), (492, 69), (342, 223), (309, 156), (245, 87), (115, 36)),
             "outsidecenter": ((342, 223), (492, 69), (492, 531), (340, 385), (352, 300)),
             "outsideleft": ((122, 600), (492, 600), (492, 531), (340, 385), (309, 445), (245, 513), (115, 564)),
             "outsideleftwing": ((0, 600), (122, 600), (115, 564), (0, 564)),
             "backcourt": ((492, 0), (564, 0), (564, 600), (492, 600))}

    Areas_Label_Position: dict = {"underbasket": {'x': 0.2, 'y': 0.525, 'xn': 0.31, 'yn': 0.515},
                                  "inthepaint": {'x': 0.375, 'y': 0.525, 'xn': 0.375, 'yn': 0.515},
                                  "insiderightwing": {'x': 0.265, 'y': 0.265, 'xn': 0.265, 'yn': 0.265},
                                  "insideright": {'x': 0.4, 'y': 0.265, 'xn': 0.4, 'yn': 0.265},
                                  "insidecenter": {'x': 0.525, 'y': 0.525, 'xn': 0.525, 'yn': 0.515},
                                  "insideleft": {'x': 0.4, 'y': 0.765, 'xn': 0.4, 'yn': 0.765},
                                  "insideleftwing": {'x': 0.265, 'y': 0.765, 'xn': 0.265, 'yn': 0.765},
                                  "outsiderightwing": {'x': 0.265, 'y': 0.1, 'xn': 0.265, 'yn': 0.0925},
                                  "outsideright": {'x': 0.55, 'y': 0.15, 'xn': 0.55, 'yn': 0.15},
                                  "outsidecenter": {'x': 0.675, 'y': 0.525, 'xn': 0.675, 'yn': 0.515},
                                  "outsideleft": {'x': 0.55, 'y': 0.9, 'xn': 0.55, 'yn': 0.9},
                                  "outsideleftwing": {'x': 0.265, 'y': 0.95, 'xn': 0.265, 'yn': 0.935},
                                  "backcourt": {'x': 0.825, 'y': 0.525, 'xn': 0.8, 'yn': 0.515}}

    # draw the court of a half basketball court
    # credits goes to the author http://savvastjortjoglou.com/nba-shot-sharts.html
    # the print of the court is copied from the mentioned website but is turned by 90°
    def draw_court(self, ax=None, color='black', lw=2, outer_lines=False, with_areas=False):
        # If an axes object isn't provided to plot onto, just get current one
        if ax is None:
            ax = plt.gca()

        # Create the various parts of an NBA basketball court

        # Create the basketball hoop
        # Diameter of a hoop is 18" so it has a radius of 9", which is a value
        # 7.5 in our coordinate system
        hoop = Circle((48, 300), radius=9, linewidth=lw, color=color, fill=False, zorder=10)

        # Create backboard
        backboard = Rectangle((40, 264), -1, 72, linewidth=lw, color=color, zorder=10)

        # The paint
        # Create the outer box 0f the paint, width=16ft, height=19ft
        outer_box = Rectangle((0, 204), 228, 192, linewidth=lw, color=color,
                              fill=False, zorder=10)
        # Create the inner box of the paint, width=12ft, height=19ft
        inner_box = Rectangle((0, 228), 228, 144, linewidth=lw, color=color,
                              fill=False, zorder=10)

        # Create free throw top arc
        top_free_throw = Arc((228, 300), 144, 144, theta1=270, theta2=90,
                             linewidth=lw, color=color, fill=False, zorder=10)
        # Create free throw bottom arc
        bottom_free_throw = Arc((228, 300), 144, 144, theta1=90, theta2=270,
                                linewidth=lw, color=color, linestyle='dashed', zorder=10)
        # Restricted Zone, it is an arc with 4ft radius from center of the hoop
        restricted = Arc((48, 300), 96, 96, theta1=270, theta2=90, linewidth=lw,
                         color=color, zorder=10)

        # Three point line
        # Create the side 3pt lines, they are 14ft long before they begin to arc
        corner_three_a = Rectangle((0, 564), 89.5, 0, linewidth=lw,
                                   color=color, zorder=10)
        corner_three_b = Rectangle((0, 36), 89.5, 0, linewidth=lw, color=color, zorder=10)
        # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
        # I just played around with the theta values until they lined up with the
        # threes
        three_arc = Arc((89.5, 300), 528, 528, theta1=270, theta2=90, linewidth=lw,
                        color=color, zorder=10)

        # Center Court
        center_outer_arc = Arc((564, 300), 144, 144, theta1=90, theta2=270,
                               linewidth=lw, color=color, zorder=10)
        center_inner_arc = Arc((564, 300), 48, 48, theta1=90, theta2=270,
                               linewidth=lw, color=color, zorder=10)

        # List of the court elements to be plotted onto the axes
        court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                          bottom_free_throw, restricted, corner_three_a,
                          corner_three_b, three_arc, center_outer_arc,
                          center_inner_arc]

        if outer_lines:
            # Draw the half court line, baseline and side out bound lines
            outer_lines = Rectangle((0, 0), 564, 600, linewidth=lw,
                                    color=color, fill=False, zorder=10)
            court_elements.append(outer_lines)

        if with_areas:
            self.get_areas(court_elements)

        # Add the court elements onto the axes
        for element in court_elements:
            ax.add_patch(element)

        return ax

    # define the areas for the shot chart
    def get_areas(self, court_elements, plot=False):
        # Draw the official areas on the court
        self.__add_areas(court_elements, "underbasket", plot)
        self.__add_areas(court_elements, "inthepaint", plot)
        self.__add_areas(court_elements, "insiderightwing", plot)
        self.__add_areas(court_elements, "insideright", plot)
        self.__add_areas(court_elements, "insidecenter", plot)
        self.__add_areas(court_elements, "insideleft", plot)
        self.__add_areas(court_elements, "insideleftwing", plot)
        self.__add_areas(court_elements, "outsiderightwing", plot)
        self.__add_areas(court_elements, "outsideright", plot)
        self.__add_areas(court_elements, "outsidecenter", plot)
        self.__add_areas(court_elements, "outsideleft", plot)
        self.__add_areas(court_elements, "outsideleftwing", plot)
        self.__add_areas(court_elements, "backcourt", plot)
        return court_elements

    # create all the Polygons for the areas on the court
    def __add_areas(self, court_elements, area, plot, lw=2, color='red'):
        xy = np.array(self.Areas[area])
        if plot:
            x = list()
            y = list()
            x = [x.append(i) for i in self.Areas[area]]
            y = [y.append(i) for i in self.Areas[area]]
            plt.plot(x, y, "k")
        area = Polygon(xy, linewidth=lw, color='red', fill=False, closed=True, zorder=5)
        court_elements.append(area)