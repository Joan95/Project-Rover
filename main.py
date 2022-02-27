# coding=utf-8
# A squad of robotic rovers are to be landed by NASA on a plateau on Mars.
# This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board
# cameras can get a complete view of the surrounding terrain to send back to Earth.
# A rover’s position and location is represented by a combination of x and y coordinates and a letter
# representing one of the four cardinal compass points.
# The plateau is divided up into a grid to simplify navigation.
# An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.
# In order to control a rover, NASA sends a simple string of letters.
# The possible letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right
# respectively, without moving from its current spot. ‘M’ means move forward one grid point, and maintain the same
# heading. Assume that the square directly North from (x, y) is (x, y+1).
# INPUT:
# The first line of input is the upper-right coordinates of the plateau, the lower- left coordinates
# are assumed to be 0,0.
# The rest of the input is information pertaining to the rovers that have been deployed. Each
# rover has two lines of input.
# The first line gives the rover’s position, and the second line is a series of instructions telling the
# rover how to explore the plateau.
# The position is made up of two integers and a letter separated by spaces, corresponding to the
# x and y co-ordinates and the rover’s orientation.
# Each rover will be finished sequentially, which means that the second rover won’t start to
# move until the first one has finished moving.

# Python imports
import copy

# Self imports
from rover_exceptions import *

# Define CONST variables
value_zero = 0
value_one = 1
cardinal_points = {
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
# For avoiding Python 2.7 sort dict issue,
# solved in newer versions of Python
sorted_cardinal_points_list = ['N', 'E', 'S', 'W']

coordinates_definition = ['X', 'Y']
set_of_known_movements = {
    'L': -value_one,
    'R': value_one,
    'M': None
}
bottom_left_coordinates = [value_zero, value_zero]
top_right_coordinates = None
first_line_types = [int, int]
second_line_types = [int, int, str]


def read_rover_parameters(reading_message, types_input_list):
    # TODO: Change description according new implementations (possible all exceptions fired)

    # List that will be returned
    final_values = list()

    # Read input, cast it to known type str
    line_input = str(raw_input("{}: ".format(reading_message)))

    # Check for incomplete data
    # TODO: Fix (+ value_one) not working for line_input expected length 5
    if len(line_input) < (len(types_input_list) + value_one):
        # Raise Incomplete Data Received Exception
        raise ExceptionIncompleteDataReceived(len(line_input), len(types_input_list) + value_one)
    else:
        # Complete data received, try to get values, check if provided data is full of spaces only
        values = line_input.split(' ')

        # Process length of values
        if len(values) > len(types_input_list):
            # Raise Extra Values Received incorrect input Exception
            raise ExceptionExtraValuesReceived(len(values), len(types_input_list), [value for value in values])

        # Input must be aligned with types passed over parameter to this function
        for count, (element, expected_type) in enumerate(zip(values, types_input_list), start=value_zero):
            # Try forcing cast on each element depending on type provided, if exception ask for new values
            try:
                # Force the casting on element and wait if accepted or exception is raised
                expected_type(element)
                # If here, there is no exception store value in final_value
                final_values.insert(count, expected_type(element))

                # If int in any case the value provided can be less than 0
                if expected_type is int and expected_type(element) < value_zero:
                    # Check that coordinates are not less than [0, 0] coordinates
                    raise ExceptionValueLessThanZero(count + value_one, element)

                # Check whether top_right_coordinates have been set or not, if so, check if over exceeding them
                if expected_type is int and top_right_coordinates is not None:
                    # Split if to avoid NoneType error for None in top_right_coordinates list
                    # Use final_values, for correct type check
                    if expected_type(element) > top_right_coordinates[count]:
                        # Check that introduced coordinates are not greater than coordinates introduced
                        raise ExceptionRoverPlacedOutOfPlane(count + value_one, element,
                                                             coordinates_definition[count],
                                                             str(top_right_coordinates[count]))

                # If string check whether it is present in cardinal_points or not
                if expected_type is str and element.upper() not in cardinal_points.keys():
                    raise ExceptionOrientationNotKnown(count + value_one, element,
                                                       ', '.join([x for x in cardinal_points.keys()]))

            except ValueError:
                # Raise custom Wrong Type Var exception
                raise ExceptionWrongTypeVar(count + value_one, element, expected_type, type(element))

    return final_values


def read_set_of_instructions(rover_id):
    # TODO: Change description according new implementations (possible all exceptions fired)

    # Read instruction
    line_input = str(raw_input("{} is waiting for instruction: ".format(rover_id)))

    # Process line_input make sure that all commands are known, otherwise ask for them again
    line_input = line_input.replace("\n", "").replace(" ", "")

    # Define list again making sure we are not writing extra values of old requests
    final_set_of_movements = list()

    # Iterate over all commands received
    for count, letter in enumerate(line_input, start=value_zero):
        final_set_of_movements.insert(count, letter.upper())
        # Check whether command is or not known
        if letter.upper() not in set_of_known_movements.keys():
            raise ExceptionInstructionParameterNotKnown(count, letter.upper(),
                                                        ', '.join([x for x in set_of_known_movements.keys()]))
    return final_set_of_movements


def execute_movement(rover_initial_position, requested_set_of_movements):
    # TODO: Change description according new implementations (possible all exceptions fired)

    # Get initial position of rover, set is a current one
    rover_current_position = copy.deepcopy(rover_initial_position)

    # Don't return the complete set of movements till make sure we are not over exceeding the edges of plane
    for command in requested_set_of_movements:
        if command == 'M':
            # Execute forward movement command
            # It will take current letter on rovers position (parameter [2]), according with this and taking as a
            # reference the mapping of cardinal_points, it will execute the movement incrementing accordingly the value
            rover_current_position[
                coordinates_definition.index(cardinal_points[rover_current_position[2]]['Coordinate'])
            ] += cardinal_points[rover_current_position[2]]['Movement']
        else:
            # Other possible command will be rotate
            rover_current_position[2] = sorted_cardinal_points_list[(sorted_cardinal_points_list.index(
                rover_current_position[2]) + set_of_known_movements[str(command).upper()]) % len(
                sorted_cardinal_points_list)]

        # After having performed the action just check whether we are over exceeding the edges of the plane
        for axis in coordinates_definition:
            if value_zero <= rover_current_position[coordinates_definition.index(axis)] <= top_right_coordinates[
               coordinates_definition.index(axis)]:
                # Rover is still in the plane
                pass
            else:
                # Rover is not in the plane raise exception
                raise ExceptionRoverAttemptingToExitKnownPlane(rover_current_position, axis,
                                                               top_right_coordinates[coordinates_definition.index(axis)]
                                                               )
    return rover_current_position


def main():
    """
    main(): Function that will handle all the steps to deploy and move Rovers accordingly.
    :return: Nothing
    """
    not_correct_input = True

    # Read first line, process it accordingly
    global top_right_coordinates

    # Keep reading until correct data to be fully received
    while not_correct_input:
        try:
            # Keep reading input until receive correct data
            top_right_coordinates = read_rover_parameters("Top right coordinates", first_line_types)
            # Break the loop, input is correct
            not_correct_input = False
        except ExceptionIncompleteDataReceived as e:
            print e
        except ExceptionExtraValuesReceived as e:
            print e
        except ExceptionWrongTypeVar as e:
            print e
        except ExceptionValueLessThanZero as e:
            print e

    # Rover's counter
    count = value_zero

    # Keep iterating until end
    # TODO: An end
    no_end = True

    while no_end:
        count += value_one
        # Set loop flags
        not_correct_position_input = True
        not_correct_instruction_input = True

        while not_correct_position_input:
            try:
                # Read second line, process it accordingly
                rover_position = read_rover_parameters("\nRover[{}] start position".format(count), second_line_types)

                # If correct break while
                not_correct_position_input = False

            except ExceptionIncompleteDataReceived as e:
                print e
            except ExceptionExtraValuesReceived as e:
                print e
            except ExceptionWrongTypeVar as e:
                print e
            except ExceptionValueLessThanZero as e:
                print e
            except ExceptionRoverPlacedOutOfPlane as e:
                print '\t[!!]\tOops... Rover, the fearless explorer, should better not be placed there.'
                print e
            except ExceptionOrientationNotKnown as e:
                print e

        while not_correct_instruction_input:
            try:
                # Try to read set of instructions
                requested_set_of_movements = read_set_of_instructions("Rover[{}]".format(count))

                # Try to execute received instruction
                print "Rover[{}] final position: {}".format(count, ' '.join(
                    str(x) for x in execute_movement(rover_position,
                                                     requested_set_of_movements)).replace("'", ""))

                # If here break the while
                not_correct_instruction_input = False
            except ExceptionInstructionParameterNotKnown as e:
                print e
            except ExceptionRoverAttemptingToExitKnownPlane as e:
                print "\t[!!]\tOops... We do know Rover is a fearless explorer but it is better for its own " \
                      "security not letting it going through there!"
                print e
    pass


if __name__ == "__main__":
    """
    Ye ye here we go!
    """
    main()
