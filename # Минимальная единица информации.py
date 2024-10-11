# Минимальная единица информации
bits_in_byte = 8  # 1 байт = 8 бит

# 1 Килобит равен 1024 битам
kilobit_in_bits = 1024

# 1 Килобайт равен 1024 байтам
kilobyte_in_bytes = 1024

# Рассчитаем, сколько бит в 1 Килобайте
kilobyte_in_bits = kilobyte_in_bytes * bits_in_byte  # 1024 байта * 8 бит в байте

# Вывод памятки
print("1 bit is the minimum unit of information.")
print(f"1 byte = {bits_in_byte} bits.")
print(f"1 Kilobit = {kilobit_in_bits} bits.")
print(f"1 Kilobyte = {kilobyte_in_bytes} bytes.")
print(f"1 Kilobyte = {kilobyte_in_bits} bits.")