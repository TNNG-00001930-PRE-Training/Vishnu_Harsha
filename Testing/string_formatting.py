import unittest
def string_formatting(name, age):
    return "My name is {} and I'm {} years old".format(name, age)
class TestString(unittest.TestCase):

    def test_formatting(self):
        result=string_formatting("Lucky",10)
        self.assertEqual(result, "My name is Lucky and I'm 10 years old")
unittest.main()