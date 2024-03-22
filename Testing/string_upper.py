import unittest
def string_upper(s):
    upper_string = s.upper()
    return upper_string
class TestString(unittest.TestCase):

    def test_upper(self):
        result=string_upper("Python")
        self.assertEqual(result, "PYTHON")
        result=string_upper("hello world")
        self.assertEqual(result,"HELLO WORLD")
        result=string_upper("PYTHON")
        self.assertEqual(result,"PYTHON")
        result=string_upper("HeLLo WoRlD")
        self.assertEqual(result,"HELLO WORLD")
unittest.main()