# Exercise 11
# Rewrite this without lambda:
# min(data, key=lambda x: x[1])

data = [("Mon", 120), ("Tue", 100), ("Wed", 140)]

def get_price(item):
    return item[1]

result = min(data, key=get_price)
print(result)

