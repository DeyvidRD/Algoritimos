frutas = ["Abacaxi", "Banana", "Maça"]

fruta = input("Digite uma Fruta: ")

frutas.append(fruta)

print(frutas)

procurada = input("Digite a fruta procurada: ")
tem = False
for fruta in frutas:
    if fruta == procurada:
        tem = True
        break

if tem:
    print("Tem a fruta")
else:
    print("Não tem a fruta")