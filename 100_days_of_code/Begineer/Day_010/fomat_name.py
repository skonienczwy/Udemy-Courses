def format_name(first_name, last_name):
    first = first_name.title()
    last = last_name.title()
    
    return f"{first} {last}"


f_name = input("Insert your first name: ")
l_name = input("Insert your last name: ")

formatted_string = format_name(first_name=f_name, last_name=l_name)

print(formatted_string)