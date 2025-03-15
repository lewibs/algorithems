import unittest

# convert numbers like 013, 123, 85647 to ints
def str_to_int(s):
    if s[0] == "-":
        s = s[1:]
        mod = -1
    elif s == "0":
        return 0
    elif s[0] == "0":
        return False
    else:
        mod = 1

    number = 0
    for c in s:
        if c.isnumeric():
            number = number * 10 + int(c)
        else:
            return False
    return number * mod

class UnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        tests = {
            "123":123,
            "0":0,
            "01":False,
            "-5":-5,
            "5.5":False,
            "sdf":False,
        }

        for input, output in tests.items():
            with self.subTest():
                self.assertEqual(str_to_int(input), output)