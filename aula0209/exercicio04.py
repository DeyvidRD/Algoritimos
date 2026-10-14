num1 = int(input("Digite o valor do primeiro número: "))
num2 = int(input("Digite o valor do segundo número: "))

"""
if num1 > num2:
    print(f"O número {num1} é o maior")
elif num2 > num1:
    print(f"O número {num2} é o maior")
else:
    print("Os números são iguais")
"""

maior = num1
if num2 > maior:
    maior = num2
print(f"O maior número é {maior}")


    