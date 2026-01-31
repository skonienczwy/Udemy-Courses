# Exercise 8
# Using the same data, use sorted() and a lambda to sort by price.

data = [("Mon", 120), ("Tue", 100), ("Wed", 140)]

sorted_price = sorted(data, key= lambda x:x[1])
print(sorted_price)