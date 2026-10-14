n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print(f"O maior valor é {maior}")