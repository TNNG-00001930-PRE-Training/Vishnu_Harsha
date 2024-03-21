#Program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
input_str = input("Enter a sequence of words: ")
words_list = input_str.split(',')
sorted_words = sorted(words_list)
print(','.join(sorted_words))
