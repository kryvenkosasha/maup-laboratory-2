ticket = input().strip()

first_half = sum(int(digit) for digit in ticket[:3])
second_half = sum(int(digit) for digit in ticket[3:])

if first_half == second_half:
    print("Счастливый")
else:
    print("Обычный")
