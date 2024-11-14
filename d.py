last_input = None  # Переменная для хранения последнего введенного значения

while True:
    current_input = input("Введите что-то (или 'exit' для выхода): ")
    if current_input == 'exit':
        break
    last_input = current_input  # Обновляем значение последнего введенного текста

print("Последний введенный input:", last_input)
