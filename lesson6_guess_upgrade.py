import random



number_user = int(input("Загадайте число: "))


while True:
    number_bot = random.randint(1, 100)
    print(number_bot)
    if number_user == number_bot:
        print("Бот победил, загаданное число ", number_user)
        break
    elif number_user > number_bot:
        input("Дайте боту подсказку с помощью знаков < , >: ")
    elif number_user < number_bot:
        input("Дайте боту подсказку с помощью знаков < , >: ")
