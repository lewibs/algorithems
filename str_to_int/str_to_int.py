import unittest

# convert numbers like 013, 123, 85647 to ints
def str_to_int(s):
    number = 0
    for c in s:
        number = number * 10 + int(c)
    return number

class UnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        tests = {
            "123":123,
            "5644": 5644,
            "19": 19,
            "0": 0,
        }

        for input, output in tests.items():
            with self.subTest():
                self.assertEqual(str_to_int(input), output)