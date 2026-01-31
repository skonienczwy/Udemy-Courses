# Exercise 7
# Given:
# data = [("Mon", 120), ("Tue", 100), ("Wed", 140)]
# Use min() and a lambda to get:
# ("Tue", 100)


data = [("Mon", 120), ("Tue", 100), ("Wed", 140)]

min_value = min(data, key=lambda x : x[1])
print(min_value)