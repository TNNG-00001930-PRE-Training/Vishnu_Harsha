import unittest
def string_strip(s):
  strip_string=s.strip()
  return strip_string
class TestString(unittest.TestCase):

    def test_strip(self):
        result=string_strip(" Python ")
        self.assertEqual(result, "Python")
        result=string_strip("   Hello World")
        self.assertEqual(result,"Hello World")
        result=string_strip("Hello World   ")
        self.assertEqual(result,"Hello World")
unittest.main()