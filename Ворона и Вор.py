name1 = input().lower()
if 'вор' in name1 and 'ворон' not in name1:
    print("Полиция!")
elif 'ворон' in name1:
    print("Кар!")
