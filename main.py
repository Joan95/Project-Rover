# coding=utf-8
# A squad of robotic rovers are to be landed by NASA on a plateau on Mars.
# This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board
# cameras can get a complete view of the surrounding terrain to send back to Earth.
# A rover’s position and location is represented by a combination of x and y coordinates and a letter
# representing one of the four cardinal compass points.
# The plateau is divided up into a grid to simplify navigation.
# An example position might be 0, 0, N, which means the rover is in the bottom left corner and
# facing North.
# In order to control a rover, NASA sends a simple string of letters.
# The possible letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right
# respectively, without moving from its current spot. ‘M’ means move forward one grid point, and
# maintain the same heading. Assume that the square directly North from (x, y) is (x, y+1).

# Define CONST variables
cardinal_points = ['N', 'E', 'S', 'W']
set_of_movements = ['L', 'R', 'M']
bottom_left_coordinates = [0, 0]
first_line_types = [int, int]
second_line_types = [int, int, str]


def read_rover_parameters(reading_message, types_input_list):
    not_correct_input = True

    # Keep reading until correct data to be fully received
    while not_correct_input:
        line_input = str(raw_input("\n{}: ".format(reading_message)))

        # Check for incomplete data
        if len(line_input) < (len(types_input_list) + 1):
            print '\t[!!]\tLength is incorrect, try it again!'
        else:
            # Complete data received, try to get values, check if provided data is full of spaces only
            values = line_input.split(' ')
            try:
                # Process length of values
                if len(values) > len(types_input_list):
                    print '\t[!!]\tFollowing extra values entered will be discarded: "{}"'.format(', '.join([values[count] for count, x in enumerate(range(len(values) - len(types_input_list)), start=len(types_input_list))]))
                    values = values[0:2]

                # Number of parameters are correct, start processing type, but first set it as correct,
                # change it if needed in next loop
                not_correct_input = not not_correct_input

                # must be aligned with types passed over parameter to this function
                for count, (element, expected_type) in enumerate(zip(values, types_input_list), start=0):
                    # Try forcing cast on each element depending on type provided, if exception ask for new values
                    try:
                        # Force the casting on element and wait if accepted or exception is raised
                        expected_type(element)

                        # If string check whether it is present in cardinal_points or not
                        if expected_type is str and element.upper() not in cardinal_points:
                            print '\t[!!]\tOops... Value in position {} "{}" may be not the correct one, ' \
                                  'try it again!\n\t\tNOTE: Possible values: {}'.format(count + 1, element, ', '.join([x for x in cardinal_points]))
                            not_correct_input = True

                    except ValueError:
                        print '\t[!!]\tOops... Value in position {} "{}" may be not the correct one, ' \
                              'try it again!'.format(count + 1, element)
                        not_correct_input = True

            except IndexError:
                print '\t[!!]\tOops... I\'m afraid Rover shouldn\'t be here, try it again!'
                pass
    return values


def read_set_of_instructions():
    pass


def main():
    num_of_rovers = int(raw_input("How many Rovers do we have in Mars? "))

    # Read first line, process it accordingly
    top_right_coordinates = read_rover_parameters("Top right coordinates", first_line_types)

    # TODO: Check that coordinates are not less than [0, 0] coordinates
    for count, x in enumerate(range(num_of_rovers), start=1):
        # Read second line, process it accordingly
        rover_position = read_rover_parameters("Rover position", second_line_types)


    pass


if __name__ == "__main__":
    main()
