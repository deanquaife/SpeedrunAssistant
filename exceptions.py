#raised when user inputs an invalid value
class ChoiceException(Exception):
    pass

#raised every 20 seconds without input in the assistant
#code obtained from https://www.semicolonworld.com/question/44145/python-3-timed-input
class TimeoutExpiredException(Exception):
    pass