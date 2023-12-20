
num1 = float(input())
num2 = float(input())
operation = input()

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':

    if num2 == 0:
        result = "Деление на 0!"
    else:
        result = num1 / num2
elif operation == 'mod':

    if num2 == 0:
        result = "Деление на 0!"
    else:
        result = num1 % num2
elif operation == 'pow':
    result = num1 ** num2
elif operation == 'div':

    if num2 == 0:
        result = "Деление на 0!"
    else:
        result = num1 // num2
else:
    result = "Недопустимая операция"


print(result)
