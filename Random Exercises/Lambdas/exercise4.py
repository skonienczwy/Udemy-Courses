# Exercise 4
# Given:
# numbers = [1, 2, 3, 4, 5]
# Use map() and a lambda to create:
# [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)



# Exercise 5
# Given:
# numbers = [1, 2, 3, 4, 5, 6]
# Use filter() and a lambda to keep only even numbers.

# Exercise 6
# Given:
# words = ["apple", "hi", "banana", "cat"]
# Use sorted() and a lambda to sort the words by length.


# Exercise 7
# Given:
# data = [("Mon", 120), ("Tue", 100), ("Wed", 140)]
# Use min() and a lambda to get:
# ("Tue", 100)

# Exercise 8
# Using the same data, use sorted() and a lambda to sort by price.

# Exercise 9
# From data, use map() and a lambda to get only the prices:
# [120, 100, 140]

# Exercise 10
# Explain in words what this does:
# sorted(data, key=lambda x: x[0])


# Exercise 11
# Rewrite this without lambda:
# min(data, key=lambda x: x[1])
