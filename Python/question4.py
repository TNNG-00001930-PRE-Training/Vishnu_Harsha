#A class which has at least two methods:getString: to get a string from console input ,printString: to print the string in upper case.Also it include simple test function to test the class methods.
class StringProcessor:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

def test_StringProcessor():
    processor = StringProcessor()
    processor.getString()
    processor.printString()
test_StringProcessor()
