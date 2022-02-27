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

# Self imports
from common_params import *
from rover import Rover as Rover
from coordinates import Coordinates as myCoordinate
from rover_exceptions import *

# Init coordinates Class object
coordinates = myCoordinate()

first_line_types = [int, int]
second_line_types = [int, int, str]


def read_rover_parameters(reading_message, types_input_list):
    """
    read_rover_parameters(): function which will read input parameters and process them accordingly, those values
    can be:
        - First coordinates which will refer to top right coordinates of the plane
        - Rover start coordinates: Known point where Rover will be deployed. That known point must be
        inside the known plane, for obvious reasons: known plane is secure, not known plane may result with
        undiscovered threatening harmful events.
    :param reading_message: Text that will be displayed whilst asking for keyboard inputs.
    :param types_input_list: List of types we are expecting to read.
    :return: Return parameters read without extra spaces and parsed with known data.
    """

    # List that will be returned
    final_values = list()

    # Read input, cast it to known type str
    line_input = str(raw_input("{}: ".format(reading_message)))

    # Gather all values which are not blank spaces, put them into a list
    values = [param for param in line_input.split(' ') if param is not '']

    # Check for incomplete data
    if len(values) < (len(types_input_list)):
        # Raise Incomplete Data Received Exception
        raise ExceptionIncompleteDataReceived(len(values), len(types_input_list))
    else:
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

                if expected_type is str:
                    # If here, there is no exception store value in final_value
                    # Corrected issue with lower case for letter when storing string
                    final_values.insert(count, expected_type(element).upper())
                else:
                    # If here, there is no exception store value in final_value
                    final_values.insert(count, expected_type(element))

                # If int in any case the value provided can be less than 0
                if expected_type is int and expected_type(element) < value_zero:
                    # Check that coordinates are not less than [0, 0] coordinates
                    raise ExceptionValueLessThanZero(count + value_one, element)

                # Check whether top_right_coordinates have been set or not, if so, check if over exceeding them
                if expected_type is int and coordinates.top_right_coordinates is not None:
                    # Split if to avoid NoneType error for None in top_right_coordinates list
                    # Use final_values, for correct type check
                    if expected_type(element) > coordinates.top_right_coordinates[count]:
                        # Check that introduced coordinates are not greater than coordinates introduced
                        raise ExceptionRoverPlacedOutOfPlane(count + value_one, element,
                                                             coordinates.coordinates_definition[count],
                                                             [str(coordinate) for coordinate in
                                                              coordinates.top_right_coordinates])

                # If string check whether it is present in cardinal_points or not
                if expected_type is str and element.upper() not in coordinates.cardinal_points.keys():
                    raise ExceptionOrientationNotKnown(count + value_one, element,
                                                       ', '.join([x for x in coordinates.cardinal_points.keys()]))

            except ValueError:
                # Raise custom Wrong Type Var exception
                raise ExceptionWrongTypeVar(count + value_one, element, expected_type, type(element))

    return final_values


def main():
    """
    main(): Function that will handle all the steps to deploy and move Rovers accordingly.
    :return: Nothing
    """
    not_correct_input = True

    # Read first line, process it accordingly, access global coordinates object
    global coordinates

    # Keep reading until correct data to be fully received
    while not_correct_input:
        try:
            # Keep reading input until receive correct data
            coordinates.set_top_right_coordinates(read_rover_parameters("Top right coordinates", first_line_types))
            # If here, break the loop, input is correct
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

        # Init rover Class object
        rover = Rover(count)

        # Set loop flags
        not_correct_position_input = True
        not_correct_instruction_input = True

        while not_correct_position_input:
            try:
                # Read second line, process it accordingly
                rover.set_rover_start_position(read_rover_parameters("\n{} start position".format(rover.rover_id),
                                                                     second_line_types))

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
                print '\t[!!]\tOops... Rover, the fearless explorer, should better not to be placed there.'
                print e
            except ExceptionOrientationNotKnown as e:
                print e

        while not_correct_instruction_input:
            try:
                # Try to read set of instructions
                rover.request_list_of_instructions()

                # Try to execute received instruction
                rover.execute_movement(coordinates)
                print "{} final position: {}".format(rover.rover_id, rover.end_position)

                # If here break the while
                not_correct_instruction_input = False
            except ExceptionInstructionParameterNotKnown as e:
                print e
            except ExceptionRoverAttemptingToExitKnownPlane as e:
                print "\t[!!]\tOops... We do know Rover is a fearless explorer but it is better for its own " \
                      "security not letting it going through there!"
                print e


if __name__ == "__main__":
    """
    Ye ye here we go!
    """
    main()
