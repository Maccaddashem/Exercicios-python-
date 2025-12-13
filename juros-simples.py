#calculo de juros simples
capital = float(input("Introduzir valor do capital: "))
taxa = float(input("Introduzir porcentagem de juros mensais: "))
tempo = int(input("Introduzir tempo em meses: "))

juros = capital * (taxa / 100) * tempo

print(f"Os juros serão de R$ {juros:.2f}")
