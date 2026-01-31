# Exercise 6
# Given:
# words = ["apple", "hi", "banana", "cat"]
# Use sorted() and a lambda to sort the words by length.




words = ["apple", "hi", "banana", "cat"]

length = sorted(words, key=lambda x: len(x))
print(length)