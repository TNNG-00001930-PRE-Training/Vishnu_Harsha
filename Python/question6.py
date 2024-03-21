#Program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
str1=input("enter strings:")
words=str1.split(" ")
words1=set(words)
print(sorted(words1))