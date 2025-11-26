fruits = {"Apple": "Red ",
           "Pear": "Green",
           "Banana": "Yellow"}
#Inserting the Key of a dic will show you the value, in the example below the key is Apple
print(fruits["Apple"])

#Adding values in a dictionary

fruits["Kiwi"] = "Green"

#declaring a empty dicitionary
new_dict = {}

#Loop through a dictionary
for i in fruits:
    #printing only the keys
    print(i)
    #printing the value assigned to that key
    print(fruits[i])

