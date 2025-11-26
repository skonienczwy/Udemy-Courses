my_dict = {'Name':'Edy', 'Age':26, 'City': 'Amsterdam'}

def searching(dict, value):
    for  key in dict:
        if dict[key]==value:
            return key, value
        
    return 'The value does not exist'  
        
value = 'Amsterdam'     
print(searching(my_dict, value )       )