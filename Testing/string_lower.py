import unittest
def string_lower(s):
  lower_string=s.lower()
  return lower_string
class TestString(unittest.TestCase):

    def test_lower(self):
        result=string_lower("Python")
        self.assertEqual(result, "python")
        result=string_lower("")
        self.assertEqual(result,"")
        result=string_lower("PYTHON")
        self.assertEqual(result,"python")
        result=string_lower("HeLLo WoRlD")
        self.assertEqual(result,"hello world")
unittest.main()