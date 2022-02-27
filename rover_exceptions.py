import sys

# Define Python Version for 3.0 or greater
python_version_3 = 3
try_it_again = "\n\t\tTry it again!"


class ExceptionIncompleteDataReceived(Exception):
    """

    """
    def __init__(self, length_received, length_expected, default_message="Length of message received is incorrect"):
        self.length_received = length_received
        self.length_expected = length_expected
        self.message = "\t\t[ERROR] - {}. Message length received: {}. " \
                       "Message length expected: {}.{}".format(default_message, self.length_received,
                                                               self.length_expected, try_it_again)

        if sys.version_info[0] < python_version_3:
            # Python 2.7 or less
            super(ExceptionIncompleteDataReceived, self).__init__(self.message)
        else:
            # Python 3
            # super().__init__(self.message)
            # TODO: Find exception launcher for Python 3
            pass


class ExceptionExtraValuesReceived(Exception):
    def __init__(self, length_received, length_expected, extra_values, default_message="Extra values received"):
        self.length_received = length_received
        self.length_expected = length_expected
        self.extra_values = extra_values
        self.message = "\t\t[ERROR] - {}. Message length received: {}. " \
                       "Message length expected: {}. Message: {}.{}".format(default_message, self.length_received,
                                                                            self.length_expected, self.extra_values,
                                                                            try_it_again)

        if sys.version_info[0] < python_version_3:
            super(ExceptionExtraValuesReceived, self).__init__(self.message)


class ExceptionWrongTypeVar(Exception):
    def __init__(self, error_position_found, affected_element, expected_type, current_type,
                 default_message="Wrong variable type received"):
        self.error_position_found = error_position_found
        self.affected_element = affected_element
        self.expected_type = expected_type
        self.current_type = current_type
        self.message = "\t\t[ERROR] - {}. Variable affected \"{}\" found in position [{}] is type \"{}\" " \
                       "and \"{}\" expected. {}".format(default_message, self.affected_element,
                                                        self.error_position_found, self.current_type,
                                                        self.expected_type, try_it_again)

        if sys.version_info[0] < python_version_3:
            super(ExceptionWrongTypeVar, self).__init__(self.message)


class ExceptionValueLessThanZero(Exception):
    def __init__(self, error_position_found, affected_element, default_message="Value can not be less than zero"):
        self.error_position_found = error_position_found
        self.affected_element = affected_element
        self.message = "\t\t[ERROR] - {}. Variable affected \"{}\" " \
                       "is parameter [{}]. {}".format(default_message, self.affected_element, self.error_position_found,
                                                      try_it_again)

        if sys.version_info[0] < python_version_3:
            super(ExceptionValueLessThanZero, self).__init__(self.message)


class ExceptionRoverPlacedOutOfPlane(Exception):
    def __init__(self, error_position_found, affected_element, axis, delimiter,
                 default_message="Value can not be higher than Plane Axis defined"):
        self.error_position_found = error_position_found
        self.affected_element = affected_element
        self.axis = axis
        self.delimiter = delimiter
        self.message = "\t\t[ERROR] - {}. Variable affected \"{}\" " \
                       "is parameter [{}] and can not be higher than Axis edge \"{}\" previously defined \"{}\". " \
                       "{}".format(default_message, self.affected_element, self.error_position_found, self.axis,
                                   self.delimiter, try_it_again)

        if sys.version_info[0] < python_version_3:
            super(ExceptionRoverPlacedOutOfPlane, self).__init__(self.message)


class ExceptionOrientationNotKnown(Exception):
    def __init__(self, error_position_found, affected_element, list_of_possible_values,
                 default_message="Wrong Orientation, parameter not known"):
        self.error_position_found = error_position_found
        self.affected_element = affected_element
        self.list_of_possible_values = list_of_possible_values
        self.message = "\t\t[ERROR] - {}. Variable affected \"{}\" " \
                       "is parameter [{}] and it is not present in known orientations [{}]. " \
                       "{}".format(default_message, self.affected_element, self.error_position_found,
                                   self.list_of_possible_values, try_it_again)
        if sys.version_info[0] < python_version_3:
            super(ExceptionOrientationNotKnown, self).__init__(self.message)


class ExceptionInstructionParameterNotKnown(Exception):
    def __init__(self, error_position_found, instruction_not_known, list_of_known_instructions,
                 default_message="Instruction not known"):
        self.instruction_not_known = instruction_not_known
        self.error_position_found = error_position_found
        self.list_of_known_instructions = list_of_known_instructions
        self.message = "\t\t[ERROR] - {}. Instruction \"{}\" found at position [{}] is not known. " \
                       "List of possible instructions: [{}].{}".format(default_message, self.instruction_not_known,
                                                                       self.error_position_found,
                                                                       self.list_of_known_instructions, try_it_again)
        if sys.version_info[0] < python_version_3:
            super(ExceptionInstructionParameterNotKnown, self).__init__(self.message)


class ExceptionRoverAttemptingToExitKnownPlane(Exception):
    def __init__(self, first_wrong_position, axis_broken, axis_top_value, default_message=
                 "Pre-processed instructions may result in Rover exceeding plane edge"):
        self.first_wrong_position = first_wrong_position
        self.axis_broken = axis_broken
        self.axis_top_value = axis_top_value
        self.message = "\t\t[ERROR] - {}. Edge broken at point [{}], " \
                       "Axis {}, maximum value for it is \"{}\". {}".format(default_message, self.first_wrong_position,
                                                                            self.axis_broken, self.axis_top_value,
                                                                            try_it_again)

        if sys.version_info[0] < python_version_3:
            super(ExceptionRoverAttemptingToExitKnownPlane, self).__init__(self.message)