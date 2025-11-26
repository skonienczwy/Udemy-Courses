def is_prime(number):
    
    if number == 0:
        return print(f"{number} is not a prime number.")
    if number == 1:
        return print(f"{number} is not a prime number.")
    else:
        count = 0
        for i in range(1,number+1):
            if number % i == 0:
                count += 1
        if count == 2:
            return print(f"{number} is a prime number.")
        else:
            return print(f"{number} is not a prime number.")

is_prime(75)
