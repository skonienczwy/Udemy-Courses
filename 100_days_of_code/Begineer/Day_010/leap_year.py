def is_leap_year(check_year):
    result = True
    if check_year % 4 == 0 and check_year % 100 != 0:
        result = True
    elif check_year % 4 != 0 and check_year % 400 != 0:
        result = False
    elif check_year % 4 == 0 and check_year % 400 == 0:
        result = True
    else:
        result = False

        

    return  result

print(is_leap_year(2000))
