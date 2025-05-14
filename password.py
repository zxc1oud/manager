# Проект 2 из 100

import random
import string
import re

def generate(length, digits, special, uppercase) -> str:
    characters = string.ascii_lowercase
    
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special:
        characters += string.punctuation
        
    password = ''.join(random.choice(characters) for _ in range(length))
    return password



while True:
    length = input("Введите длину вашего пароля: ")
    length = re.findall(r'\d+', length)

    if length:
        length = int(length[0])
    else:
        print("Введите корректное число.")
        break

    digits = input("Вы желаете видеть в вашем пароле цифры? (Да/Нет): ").lower() == "да"
    special = input("Вы желаете видеть в вашем пароле специальные символы? (Да/Нет): ") == "да"
    uppercase = input("Вы желаете видеть в вашем пароле заглавные буквы? (Да/Нет): ") == "да"

    password = generate(length, digits, special, uppercase)

    print(f"Ваш сгенерированный пароль: {password}")
    break