valor_total = float(input("digite o valor total da conta: "))

if valor_total > 200:
    desconto = valor_total * 0.15
    valor_final = valor_total - desconto
else:
    valor_final = valor_total

print(f"Valor total final em R${valor_final:.2f}")