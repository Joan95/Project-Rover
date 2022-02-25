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

# Define CONST variables
value_zero = 0
value_one = 1
cardinal_points = {
                      'N': {
                          'Coordinate': 'Y',
                          'Movement': 1
                      },
                      'E': {
                          'Coordinate': 'X',
                          'Movement': 1
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
    """
    read_rover_paramenters(): A function that will be used in order to read either initial coordinates for the
     or Rover's
    position when requested. This function requires two main inputs.

    :param reading_message: Message displayed when asking for input.
    :param types_input_list: A list of values which are expected to be received whilst reading from keyboard. Those
    parameters would be used in order to finally crosscheck whether the types are the correct ones or not.
    :return: correct values read from keyboard, only once they are correct, otherwise it will keep asking for a
    correct input to be provided.
    """
    not_correct_input = True
    final_values = list()

    # Keep reading until correct data to be fully received
    while not_correct_input:
        line_input = str(raw_input("{}: ".format(reading_message)))

        # Check for incomplete data
        if len(line_input) < (len(types_input_list) + value_one):
            print '\t[!!]\tLength is incorrect, try it again!'
        else:
            # Complete data received, try to get values, check if provided data is full of spaces only
            values = line_input.split(' ')
            try:
                # Process length of values
                if len(values) > len(types_input_list):
                    print '\t[!!]\tFollowing extra values entered will be discarded: "{}"'.format(', '.join(
                        [values[count] for count, x in
                         enumerate(range(len(values) - len(types_input_list)), start=len(types_input_list))]))
                    # Take exactly very expected first values
                    values = values[value_zero:len(types_input_list)]

                # Number of parameters are correct, start processing type, but first set it as correct,
                # change it if needed in next loop
                not_correct_input = not not_correct_input

                # Init list again, just in case wrong values have been set there
                final_values = list()

                # must be aligned with types passed over parameter to this function
                for count, (element, expected_type) in enumerate(zip(values, types_input_list), start=value_zero):
                    # Try forcing cast on each element depending on type provided, if exception ask for new values
                    try:
                        # Force the casting on element and wait if accepted or exception is raised
                        expected_type(element)
                        # If here, there is no exception store value in final_value, it might be overwritten if
                        # it is not correct, but there would be the type accordingly
                        final_values.insert(count, expected_type(element))

                        # If int in any case the value provided can be less than 0
                        if expected_type is int and expected_type(element) < value_zero:
                            # Check that coordinates are not less than [0, 0] coordinates
                            print '\t[!!]\tOops... Value in position {} "{}" may be wrong, ' \
                                  'try it again!\n\t\tNOTE: Value can not be less than 0'.format(count + 1, element)
                            not_correct_input = True

                        # Check whether top_right_coordinates have been set or not, if so, check if over exceeding
                        if expected_type is int and top_right_coordinates is not None:
                            # Split if to avoid NoneType error for None in top_right_coordinates list
                            # Use final_values, for correct type check
                            if expected_type(element) > top_right_coordinates[count]:
                                # Check that introduced coordinates is not greater than coordinates introduced
                                print '\t[!!]\tOops... I\'m afraid Rover shouldn\'t be here. ' \
                                      'Value in position {} "{}" is out of plane, ' \
                                      'try it again!\n\t\tNOTE: Value must be less than ' \
                                      '[{}]'.format(count + value_one, element, str(top_right_coordinates[count]))
                                not_correct_input = True

                        # If string check whether it is present in cardinal_points or not
                        if expected_type is str and element.upper() not in cardinal_points.keys():
                            print '\t[!!]\tOops... Value in position {} "{}" may be not the correct one, ' \
                                  'try it again!\n\t\tNOTE: Possible values: {}'.format(
                                   count + value_one, element, ', '.join([x for x in cardinal_points.keys()]))
                            not_correct_input = True

                    except ValueError:
                        print '\t[!!]\tOops... Value in position {} "{}" may be not the correct one, ' \
                              'try it again!'.format(count + value_one, element)
                        not_correct_input = True

            except IndexError:
                print '\t[!!]\tOops... I\'m afraid Rover should not be here, try it again!'
                pass
    return final_values


def read_set_of_instructions(rover_id):
    """
    read_set_of_instructions(): This function will read the set of instructions passed by which would be loaded lately
    into Rover accordingly. Instructions will be check whether they are known or not. If not, function will ask
    for new valid values again.

    :param rover_id: For properly printing the valid information.
    :return: cleaned list of movements to be executed in another function.
    """
    not_correct_input = True
    final_set_of_movements = list()

    # Keep reading until correct data to be fully received
    while not_correct_input:
        line_input = str(raw_input("{} is waiting for instruction: ".format(rover_id)))
        print '\n'

        # Process line_input make sure that all commands are known, otherwise ask for them again
        line_input = line_input.replace("\n", "").replace(" ", "")

        # Take input as valid, check below if some of commands are not present in list of commands known
        not_correct_input = not not_correct_input

        # Define list again making sure we are not writing extra values of old requests
        final_set_of_movements = list()

        # Iterate over all commands received
        for count, letter in enumerate(line_input, start=value_zero):
            final_set_of_movements.insert(count, letter.upper())
            # Check whether command is or not known
            if letter.upper() not in set_of_known_movements.keys():
                print '\t[!!]\tOops... Rover does not know command in position {} [{}], ' \
                      'send it again!'.format(count, letter.upper())
                not_correct_input = True

                # Stop iterating, send the response wait for new set of instructions
                break
    return final_set_of_movements


def execute_movement(rover_position, requested_set_of_movements):
    """
    execute_movement(): This function will take both parameters filled previously with valid data and will attempt
    performing the movement of Rover.
    :param rover_position: This is the initial position of the Rover.
    :param requested_set_of_movements: This is the list of valid movements asked to be performed by Rover.
    :return:
    """
    # Get initial position of rover, set is a current one
    rover_current_position = rover_position

    # TODO: Check we are not over exceeding edges of plane

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
    return rover_current_position


def main():
    """
    main(): Function that will handle all the steps to deploy and move Rovers accordingly.
    :return: Nothing
    """
    # Read first line, process it accordingly
    global top_right_coordinates
    top_right_coordinates = read_rover_parameters("Top right coordinates", first_line_types)

    # Rover's counter
    count = value_zero

    # Keep iterating until end
    # TODO: An end
    no_end = True

    while no_end:
        count += value_one
        # Read second line, process it accordingly
        rover_position = read_rover_parameters("\nRover[{}] start position".format(count), second_line_types)
        requested_set_of_movements = read_set_of_instructions("Rover[{}]".format(count))

        # Execute instruction
        print "Rover[{}] final position: {}".format(count, ' '.join(
            str(x) for x in execute_movement(rover_position, requested_set_of_movements)).replace("'", ""))
    pass


if __name__ == "__main__":
    """
    Ye ye here we go!
    """
    main()
