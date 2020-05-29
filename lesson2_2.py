number = None

while True:
    number = int(input("Введите число "))
    if number <= 10 and number > 0:
        number = number ** 2
        print(number)
        break
    else:
        print("Число не верное, введите число от 0 до 10")
