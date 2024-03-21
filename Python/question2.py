#Program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n. and then the program should print the dictionary.
n = int(input("Enter a number: "))
square_dict = dict((i, i*i) for i in range(1, n+1))
print(square_dict)