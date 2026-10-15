# Receber 10 valores do usuario e apresentar o maior e o menor valor deles.

for i in range(10):
    num = int(input("Digite um valor: "))
    
    if i==0: # Primeira vez
        maior = num
        menor = num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

print(f"O maior é {maior} e o menor é {menor}")