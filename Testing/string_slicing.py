import unittest
def string_slicing(s, start, end):
    return s[start:end]

class TestString(unittest.TestCase):

    def test_slicing(self):
        result=string_slicing("Python",0,3)
        self.assertEqual(result, "Pyt")
        result=string_slicing("Hello World", -5, -1)
        self.assertEqual(result,"Worl")
        
unittest.main()