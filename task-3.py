def get_correct_ending(number):
    if 11 <= number % 100 <= 19:
        return 'программистов'
    elif number % 10 == 1:
        return 'программист'
    elif 2 <= number % 10 <= 4:
        return 'программиста'
    else:
        return 'программистов'

n = int(input("Введите число программистов: "))

ending = get_correct_ending(n)
print(f"{n} {ending}")
