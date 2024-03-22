import unittest
def string_concatenate(s1, s2):
    return s1 + s2

class TestString(unittest.TestCase):

    def test_concatenation(self):
        result=string_concatenate("Hello","world")
        self.assertEqual(result, "Helloworld")
        result=string_concatenate("Hello", "")
        self.assertEqual(result,"Hello")
        result=string_concatenate("Hello ", "World")                 
        self.assertEqual(result,"Hello World")   
        result=string_concatenate("The answer is: ", str(42)) 
        self.assertEqual(result,"The answer is: 42")
                  
unittest.main()
