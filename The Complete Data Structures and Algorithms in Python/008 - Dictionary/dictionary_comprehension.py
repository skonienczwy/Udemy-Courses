import random
city_name = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']
county_name = ['France', 'England', 'Italy', 'Germany', 'Spain']


nem_dict = {city : random.randint(20, 30) for city in city_name}
print(nem_dict)

#function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
nem_dict2 = {country : city for country,city in zip(city_name, county_name)}

print(nem_dict2)


above_25 = {city : temp for (city,temp) in nem_dict.items() if temp > 25}
print(above_25)

#If you need to handle lists of different lengths, you can use itertools.zip_longest:
# from itertools import zip_longest

# a = [1, 2, 3, 4]
# b = ['x', 'y']

# print(list(zip_longest(a, b, fillvalue='N/A')))
# # [(1, 'x'), (2, 'y'), (3, 'N/A'), (4, 'N/A')]