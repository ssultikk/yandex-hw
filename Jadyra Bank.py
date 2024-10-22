class ATM:
    def __init__(self, balance=0):
        self.balance = balance
    
    def check_balance(self):
        print(f"Ваш баланс: {self.balance} тенге")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Вы пополнили счёт на {amount} тенге.")
            self.check_balance()
        else:
            print("Введите положительную сумму для пополнения.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на счёте.")
        elif amount <= 0:
            print("Введите положительную сумму для снятия.")
        else:
            self.balance -= amount
            print(f"Вы сняли {amount} тенге.")
            self.check_balance()

def atm_menu():
    atm = ATM(1000)  # Начальный баланс 1000 тенге
    while True:
        print("\nДобро пожаловать на Jadyra Bank! Выберите операцию:")
        print("1. Проверить баланс")
        print("2. Пополнить счёт")
        print("3. Снять деньги")
        print("4. Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Введите сумму для пополнения: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Введите сумму для снятия: "))
            atm.withdraw(amount)
        elif choice == '4':
            print("Спасибо за использование Jadyra Bank!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

# Запуск банкомата
atm_menu()
