# Function Sum

# def = definition, function_name(parameters):
def sum(x, y):
    result = x + y
    return result

print('My Calculator')
print('-------------')
number1 = int(input('Type the 1st number: '))
number2 = int(input('Type the 2nd number: '))
calc = sum(number1, number2)
print(f'Result: {calc}')