# Python imports
import copy

# Custom imports
from common_params import *
from rover_exceptions import ExceptionInstructionParameterNotKnown, ExceptionRoverAttemptingToExitKnownPlane


class Rover:
    """
    Rover Class object.
    """
    def __init__(self, rover_id):
        self.set_of_known_movements = {
                                        'L': -value_one,
                                        'R': value_one,
                                        'M': None
                                      }
        self.rover_id = "Rover[{}]".format(rover_id)
        self.start_position = None
        self.end_position = None
        self.requested_list_of_instructions = None

    def set_rover_start_position(self, start_position):
        """
        Setter for Rover's start position
        """
        self.start_position = start_position

    def request_list_of_instructions(self):
        """
        Rover's function that will call read_set_of_instructions for requesting for instructions to be execute
        lately.
        """
        self.requested_list_of_instructions = read_set_of_instructions(self)

    def execute_movement(self, coordinates):
        """
        Rover's function that will update Rover's end position accordingly with instructions received and
        current coordinates defined.
        """
        self.end_position = execute_movement(self, coordinates)


def read_set_of_instructions(rover):
    """
    read_set_of_instructions(): Function that will read an instruction that we want Rover to execute.
    If the instruction read is not known an exception will be raised.
    :param rover: Rover object.
    :return: Parsed list of known movements, removing additional spaces.
    """
    # Read instruction
    line_input = str(raw_input("{} is waiting for instruction: ".format(rover.rover_id)))

    # Process line_input make sure that all commands are known, otherwise ask for them again
    line_input = line_input.replace("\n", "").replace(" ", "")

    # Define list again making sure we are not writing extra values of old requests
    final_set_of_movements = list()

    # Iterate over all commands received
    for count, letter in enumerate(line_input, start=value_zero):
        final_set_of_movements.insert(count, letter.upper())
        # Check whether command is or not known
        if letter.upper() not in rover.set_of_known_movements.keys():
            raise ExceptionInstructionParameterNotKnown(count, letter.upper(),
                                                        ', '.join([x for x in rover.set_of_known_movements.keys()]))
    return final_set_of_movements


def execute_movement(rover, coordinates):
    """
    execute_movement(): Function that will pre-execute and execute the full list of movements processed lately.
    Whilst pre processing, if Rover gets out of the known plane an exception will be raised.
    :param rover: Rover object.
    :param coordinates: Coordinates object.
    :return: Last position after having executed all the list of movements.
    """
    # Get initial position of rover, set is as current ending one
    estimated_end_position = copy.deepcopy(rover.start_position)

    # Don't return the complete set of movements till make sure we are not over exceeding the edges of plane
    for command in rover.requested_list_of_instructions:
        if command == 'M':
            # Execute forward movement command
            # It will take current letter on rovers position (parameter [2]), according with this and taking as a
            # reference the mapping of cardinal_points, it will execute the movement incrementing accordingly the value
            estimated_end_position[
                coordinates.coordinates_definition.index(
                    coordinates.cardinal_points[estimated_end_position[value_two]]['Coordinate'])] += \
                coordinates.cardinal_points[estimated_end_position[value_two]]['Movement']
        else:
            # Other possible command will be rotate
            estimated_end_position[value_two] = coordinates.sorted_cardinal_points_list[
                (coordinates.sorted_cardinal_points_list.index(estimated_end_position[value_two]) +
                 rover.set_of_known_movements[str(command).upper()]) % len(coordinates.sorted_cardinal_points_list)]

        # After having performed the action just check whether we are over exceeding the edges of the plane
        for axis in coordinates.coordinates_definition:
            if coordinates.bottom_left_coordinates[coordinates.coordinates_definition.index(axis)] > \
                    estimated_end_position[coordinates.coordinates_definition.index(axis)] or \
                    estimated_end_position[coordinates.coordinates_definition.index(axis)] > \
                    coordinates.top_right_coordinates[coordinates.coordinates_definition.index(axis)]:

                # Rover is not in the plane raise exception
                raise ExceptionRoverAttemptingToExitKnownPlane(estimated_end_position, axis,
                                                               coordinates.top_right_coordinates[
                                                                   coordinates.coordinates_definition.index(axis)
                                                               ],
                                                               coordinates.bottom_left_coordinates[
                                                                   coordinates.coordinates_definition.index(axis)
                                                               ])
            else:
                # Rover is still in the plane
                pass
    return estimated_end_position
