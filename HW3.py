# 1. Користувач вводить із клавіатури номер дня тижня (1-7).
# Необхідно вивести на екран назви дня тижня.
# Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.
user_select = int(input())
match user_select:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Incorrect menu item")

# 2. Користувач вводить два числа.
# Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання.

number1 = int(input())
number2 = int(input())

if number1 == number2:
    print("equals")
elif number1 < number2:
    print(number1, number2)
else:
    print(number2, number1)

# Користувач вводить два числа та матем дію: + - * або /
# Залежно від введеної матем дії вивести результат

number1 = int(input())
number2 = int(input())

action = input("Choose your action from this 4 options: + - * /")
match action:
    case "+":
        print(number1 + number2)
    case "-":
        print(number1 - number2)
    case "*":
        print(number1 * number2)
    case "/":
        print(number1 / number2)
    case _:
        print("TRY AGAIN")


