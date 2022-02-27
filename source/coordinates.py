# Python imports

# Custom imports
from common_params import *


class Coordinates:
    def __init__(self):
        self.coordinates_definition = ['X', 'Y']
        self.bottom_left_coordinates = [value_zero, value_zero]
        # For avoiding Python 2.7 sort dict issue,
        # solved in newer versions of Python
        self.sorted_cardinal_points_list = ['N', 'E', 'S', 'W']
        self.cardinal_points = {
                                'N': {
                                    'Coordinate': 'Y',
                                    'Movement': value_one
                                },
                                'E': {
                                    'Coordinate': 'X',
                                    'Movement': value_one
                                },
                                'S': {
                                    'Coordinate': 'Y',
                                    'Movement': -value_one
                                },
                                'W': {
                                    'Coordinate': 'X',
                                    'Movement': -value_one
                                }
                            }
        self.top_right_coordinates = None

    def set_top_right_coordinates(self, top_right_coordinates):
        self.top_right_coordinates = top_right_coordinates
