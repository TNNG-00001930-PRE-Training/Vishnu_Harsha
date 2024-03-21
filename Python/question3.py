#Program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
input_str = input("Enter a sequence numbers: ")
numbers_list = input_str.split(',')
numbers_tuple = tuple(numbers_list)
print(numbers_list)
print(numbers_tuple)
