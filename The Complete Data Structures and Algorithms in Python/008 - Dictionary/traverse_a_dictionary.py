my_dict = {'Name':'Edy', 'Age':26, 'City': 'Amsterdam'}

def traverse(dict):
    for key in dict:
        print(key, dict[key])
        
traverse(my_dict)