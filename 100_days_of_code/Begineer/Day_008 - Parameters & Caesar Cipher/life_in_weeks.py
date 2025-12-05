'''Create a function called life_in_weeks() using maths and f-Strings that tells us 
how many weeks we have left, if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:'''


def life_in_weeks(age):
    weeks_left = (90 - age)*52
    print(f"You have {weeks_left} weeks left.")

age = 20

life_in_weeks(age)