peso = float(input("Digite o peso da pessoa: "))
altura = float(input("Digite a altura da pessoa, ex. 1.67: "))
imc = peso / altura ** 2

print(f"Seu imc calculado foi: {imc:.2f}")
if imc < 18.5:
    print("Situacao: Abaixo do peso")
elif imc < 25:
    print("Situacao: Peso normal")
elif imc < 30:
    print("Situacao: sobrepeso")
else:
    print("Situacao: Obesidade")