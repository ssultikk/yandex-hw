def main():
    # Функция для определения подарка
    def determine_gift(good_count, bad_count, last_type):
        if good_count > bad_count and last_type == "добрый":
            return "серебряный шиллинг"
        elif bad_count > good_count and last_type == "злой":
            return "золотой"
        else:
            return "Ах, не знаю!"

    good_count = 0  # Счётчик строк "добрый"
    bad_count = 0   # Счётчик строк "злой"
    last_type = None  # Последний введённый тип строки

    while True:
        line = input().strip()
        
        if line == "":
            break
        
        if line == "добрый":
            good_count += 1
            last_type = "добрый"
        elif line == "злой":
            bad_count += 1
            last_type = "злой"
        elif line == "Какой подарок?":
            gift = determine_gift(good_count, bad_count, last_type)
            print(gift)
            # Обнуляем счётчики и последний тип строки после вопроса
            good_count = 0
            bad_count = 0
            last_type = None

# Запуск основной функции
main()
