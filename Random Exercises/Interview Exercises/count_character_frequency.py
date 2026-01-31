text = "banana"
count = {}



for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
        
print(count)




















# for char in text:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1
    
# print(count)    