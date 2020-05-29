import random


number_answer = random.randint(1, 100)


while True:
    number_user = int(input("Введите число от 1 до 100: "))
    if number_answer == number_user:
        print("Поздравляем, вы победили! загаданное число: ", number_answer)
        break
    elif number_answer > number_user:
        print("Вы ввели малое число")
    elif number_answer < number_user:
        print("Вы ввели большое число")
