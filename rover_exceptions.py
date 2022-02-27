import sys

# Define Python Version for 3.0 or greater
python_version_3 = 3
try_it_again = "\n\t\tTry it again!"


class ExceptionIncompleteDataReceived(Exception):
    """
    Exception raised if incomplete data is received.
    """
    def __init__(self, length_received, length_expected, default_message="Parameters of message received are incorrect"):
        self.length_received = length_received
        self.length_expected = length_expected
        self.message = "\t\t[ERROR] - {}. Number of parameters received: {}. " \
                       "Number of parameters expected: {}.{}".format(default_message, self.length_received,
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
    """
    Exception raised if not expected values received, extra values.
    """
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
        else:
            # Python 3
            # super().__init__(self.message)
            # TODO: Find exception launcher for Python 3
            pass


class ExceptionWrongTypeVar(Exception):
    """
    Exception raised if wrong type of parameter has been received.
    """
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
        else:
            # Python 3
            # super().__init__(self.message)
            # TODO: Find exception launcher for Python 3
            pass


class ExceptionValueLessThanZero(Exception):
    """
    Exception raised if coordinates or values initialized are less than value zero.
    """
    def __init__(self, error_position_found, affected_element, default_message="Value can not be less than zero"):
        self.error_position_found = error_position_found
        self.affected_element = affected_element
        self.message = "\t\t[ERROR] - {}. Variable affected \"{}\" " \
                       "is parameter [{}]. {}".format(default_message, self.affected_element, self.error_position_found,
                                                      try_it_again)

        if sys.version_info[0] < python_version_3:
            super(ExceptionValueLessThanZero, self).__init__(self.message)
        else:
            # Python 3
            # super().__init__(self.message)
            # TODO: Find exception launcher for Python 3
            pass


class ExceptionRoverPlacedOutOfPlane(Exception):
    """
    Exception raised when Rover is attempted to be placed out of known plane.
    """
    def __init__(self, error_position_found, affected_element, axis, top_left_coordinates,
                 default_message="Value can not be higher than Plane Axis defined"):
        self.error_position_found = error_position_found
        self.affected_element = affected_element
        self.axis = axis
        self.top_left_coordinates = top_left_coordinates
        self.message = "\t\t[ERROR] - {}. Variable affected \"{}\" " \
                       "is parameter [{}], can not be higher than Axis edge \"{}\". Top right coordinates previously " \
                       "defined are \"{}\". " \
                       "{}".format(default_message, self.affected_element, self.error_position_found, self.axis,
                                   self.top_left_coordinates, try_it_again)

        if sys.version_info[0] < python_version_3:
            super(ExceptionRoverPlacedOutOfPlane, self).__init__(self.message)
        else:
            # Python 3
            # super().__init__(self.message)
            # TODO: Find exception launcher for Python 3
            pass


class ExceptionOrientationNotKnown(Exception):
    """
    Exception raised when orientation received is not known.
    """
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
        else:
            # Python 3
            # super().__init__(self.message)
            # TODO: Find exception launcher for Python 3
            pass


class ExceptionInstructionParameterNotKnown(Exception):
    """
    Exception raised when Rover receive an unknown instruction.
    """
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
        else:
            # Python 3
            # super().__init__(self.message)
            # TODO: Find exception launcher for Python 3
            pass


class ExceptionRoverAttemptingToExitKnownPlane(Exception):
    """
    Exception raised when Rover is attempting to go through axis out of known plane.
    """
    def __init__(self, first_wrong_position, axis_broken, axis_top_value, default_message=
                 "Pre-processed instructions may result in Rover exceeding plane edge"):
        self.first_wrong_position = first_wrong_position
        self.axis_broken = axis_broken
        self.axis_top_value = axis_top_value
        self.message = "\t\t[ERROR] - {}. Edge broken at point {}, " \
                       "Axis {}, maximum value for it is \"{}\". {}".format(default_message, self.first_wrong_position,
                                                                            self.axis_broken, self.axis_top_value,
                                                                            try_it_again)

        if sys.version_info[0] < python_version_3:
            super(ExceptionRoverAttemptingToExitKnownPlane, self).__init__(self.message)
        else:
            # Python 3
            # super().__init__(self.message)
            # TODO: Find exception launcher for Python 3
            pass

