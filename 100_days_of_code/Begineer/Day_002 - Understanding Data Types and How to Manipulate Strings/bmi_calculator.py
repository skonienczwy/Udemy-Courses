'''BMI Calculator
The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
bmi is equal to the person's weight divided by the person's height squared.
'''

height = int((input('Insert your height in cm:\n')))
height = float(height/100)
weight = int(input('Insert your weight:\n'))
bmi = weight / ( height** 2)
print('You BMI is: ', round(bmi,2 ))
