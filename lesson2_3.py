FERST_NAME = input("Ваше имя: ")

LAST_NAME = input("Ваша фамилию: ")

AGE = int(input("Ваш возраст: "))

WEIGHT = int(input("Ваш вес: "))

if AGE <= 30 and (WEIGHT >= 50 or WEIGHT <= 120):
    print("хорошее состояние")
elif (AGE > 30 and AGE <= 39) and (WEIGHT < 50 or WEIGHT > 120):
    print("следует заняться собой")
elif AGE >= 40 and (WEIGHT < 50 or WEIGHT >= 120):
    print("следует обратится к врачу!")
else:
    print("Вы в хорошем состоянии!")
