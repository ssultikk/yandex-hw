def main():
    # Запрашиваем имя пользователя
    name = input("Identify yourself, please!\n")
    
    # Запрашиваем первый ввод текста
    original_text = input("Enter the text.\n")
    
    # Запрашиваем повтор текста
    repeated_text = input("Repeat the text.\n")
    
    # Сравниваем два текста
    if original_text == repeated_text:
        print(f"{name}, entered correctly!")
    else:
        print(f"{name}, it didn't work out yet, try again!")

# Запуск программы
if __name__ == "__main__":
    main()
