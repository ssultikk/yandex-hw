import re

# Считываем строку
input_str = input().lower()

# Проверяем наличие "вор" как отдельного слова и отсутствие "ворона"
if re.search(r'\bвор\b', input_str) and 'ворона' not in input_str:
    print("Полиция!")
# Проверяем наличие "ворон" как отдельного слова
elif re.search(r'\bворон\b', input_str):
    print("Кар!")
