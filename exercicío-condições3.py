#aumento de salario:
salario = int(input("qual valor do seu salario: "))
valor = salario
if valor > 1250:
    print("o seu aumento é de:", (valor * (10 / 100) + valor))
if valor < 1250:
    print(" o seu aumento é de:", (valor * (15 / 100) + valor ))
