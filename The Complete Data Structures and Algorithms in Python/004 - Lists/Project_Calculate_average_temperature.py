
temperature = list()

number_of_days = int(input("'How many day's temperature? : "))

def average_temperature(days):
    for i in range(1, int(days)+1):
        day =  float(input(f"Day {i}'s hight temp: "))
        temperature.append(day)
        avg_temp = sum(temperature)/days   
            
    return print(f'Average = {avg_temp} \n {above_average(avg_temp, temperature)} day(s) above average')

def above_average(avg, array):
    count = 0
    for i in array:
        if i > avg:
            count += 1   
                     
    return count

  


average_temperature(number_of_days)


