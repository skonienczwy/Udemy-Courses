# Exercise 9
# From data, use map() and a lambda to get only the prices:
# [120, 100, 140]

data = [("Mon", 120), ("Tue", 100), ("Wed", 140)]

# sorted_price = sorted(data, key= lambda x:x[1])

prices = list(map(lambda x:x[1], data))

print(prices)