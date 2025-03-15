import unittest

# this is a state machine that takes char, CHAR, num ...
class StateMachine:
    def __init__(self, start, ends, errors, is_done):
        self.start = start
        self.ends = set(ends)
        self.errors = set(errors)
        self.is_done = is_done
    
    def consume(self, value):
        state = self.start
        while not state in self.errors and not self.is_done(value):
            value, state = state(value)
        return state in self.ends
    
def state1(value): 
    if value[0].islower():
        return value[1:], state2
    return value, error

def state2(value):
    if value[0].isupper():
        return value[1:], state3
    return value, error

def state3(value):
    if value[0].isnumeric():
        return value[1:], state1
    return value, error

def error(value):
    return value, error

def is_done(value):
    return value == ""

state_machine = StateMachine(
    start=state1,
    ends=[state1],
    errors=[error],
    is_done=is_done,
)

class TestSM(unittest.TestCase):
    def setUp(self):
        self.state_machine = state_machine

    def test(self):
        test_cases = test_cases = {
            "aA1": True,
            "aA1bB2": True,
            "aA1bB2cC3": True,
            "aA1bB2cC3dD4": True,
            "aA1bB2cC3dD4eE5": True,
            "aA1bB2cC3dD4eE5fF6": True,
            "aA1bB2cC3dD4eE5fF6gG7": True,
            "aA1bB2cC3dD4eE5fF6gG7hH8": True,
            "aA1bB2cC3dD4eE5fF6gG7hH8iI9": True,
            "aAA": False,
            "aA1BB2": False,
            "aA1bB21C3": False,
            "aA1bB2cCddD4": False,
            "aA1bB2cs3dD4eE5": False,
            "aA1bB2cC3dD4eE5ff6": False,
            "aA1bB2cC32D4eE5fF6gG7": False,
            "AA1bB2cC3dD4eE5fF6gG7hH8": False,
            "aA1bB2cC3dD4eE5fF6gG7hH8iIi": False,
            "aA": False,
            "aA1bB": False,
            "aA1bB2cC": False,
            "aA1bB2cC3dD": False,
            "aA1bB2cC3dD4eE": False,
            "aA1bB2cC3dD4eE5fF": False,
            "aA1bB2cC3dD4eE5fF6gG": False,
            "aA1bB2cC3dD4eE5fF6gG7hH": False,
            "aA1bB2cC3dD4eE5fF6gG7hH8iI": False,
        }
        for input_str, expected in test_cases.items():
            with self.subTest(input=input_str):
                self.assertEqual(self.state_machine.consume(input_str), expected)
