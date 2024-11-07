def approximate_pi(n_terms):
    pi_approximation = 0
    for k in range(n_terms):
        pi_approximation += ((-1) ** k) / (2 * k + 1)
    pi_approximation *= 4
    return pi_approximation

# Запрашиваем количество слагаемых у пользователя
n_terms = int(input("Введите количество слагаемых: "))
pi_value = approximate_pi(n_terms)
print(f"Приближенное значение числа π с {n_terms} слагаемыми: {pi_value}")
