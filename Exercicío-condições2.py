#atividade, velocidad y multa:
velocidade = int(input("qual a velocidade: "))
multa = (5 * (velocidade - 80))
if velocidade > 80:
    print("você foi multado")   
if velocidade > 80:
    print("sua multa é de R$%5.2f" % multa)
if velocidade <= 80:
    print("ta liberado")  
