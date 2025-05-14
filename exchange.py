# Проект 3 из 100

import requests

from datetime import datetime

def exchange(base_currency, target_currency, date):
    API = "API :)" 
    today = datetime.today().strftime("%Y-%m-%d")

    if date >= today:
        print(f"⚠ Дата {date} недоступна. Используем 2025-03-15.")
        date = "2008-07-12"

    url = f"https://api.freecurrencyapi.com/v1/historical?apikey={API}&date={date}&base_currency={base_currency}&currencies={target_currency}"
    
    response = requests.get(url)
    data = response.json()

    if "data" not in data or date not in data["data"] or target_currency not in data["data"][date]:
        print("Ошибка при получении данных. Проверьте дату и коды валют.")
        return None
    
    return data["data"][date][target_currency]

base_currency = input("Введите код первой валюты (например, USD): ").upper()
target_currency = input("Введите код второй валюты (например, EUR): ").upper()
date = input("Введите дату (в формате YYYY-MM-DD): ")

try:
    datetime.strptime(date, "%Y-%m-%d")
except ValueError:
    print("Ошибка: неверный формат даты. Введите в формате YYYY-MM-DD.")
    exit()

rate = exchange(base_currency, target_currency, date)

if rate:
    reverse_rate = 1 / rate 
    print(f"Курс {base_currency} → {target_currency} на {date}: {rate:.2f}")
    print(f"Курс {target_currency} → {base_currency} на {date}: {reverse_rate:.2f}")
else:
    print("Не удалось получить курс валют.")