# Exercise 5
# Given:
# numbers = [1, 2, 3, 4, 5, 6]
# Use filter() and a lambda to keep only even numbers.
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
