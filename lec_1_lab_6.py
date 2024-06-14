print("Здравствуйте, не могли бы вы указать немного информации о себе?)")
old = int(input("Введите ваш возраст: "))
male = str(input("Введите ваш пол (М | Ж): "))
username = str(input("Введите ваше имя: "))
town = str(input("Введите ваш город: "))
shl_class = int(input("Введите цифру вашего класса: "))
user = [old, male, username, town, shl_class]
print(user)