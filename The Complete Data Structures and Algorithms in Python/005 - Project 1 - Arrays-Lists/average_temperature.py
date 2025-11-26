total = 0
count = 0
my_list = list()
avg = 0

while (True):
    inp = input('Enter a number: ')
    if inp.lower() == 'done': break
    my_list.append(float(inp))
    avg = sum(my_list)/len(my_list)


print(f'Average: {avg}')     