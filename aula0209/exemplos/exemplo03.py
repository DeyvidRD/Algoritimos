valor_pizza = 49.90
desconto = 0.10

valor_do_desconto = valor_pizza * desconto
valor_com_desconto = valor_pizza - (valor_pizza * desconto)

print(f"Valor da pizza    R${valor_pizza:6.2f}")
print(f"Valor do desconto R${valor_do_desconto:6.2f}")
print(f"Valor a pagar     R${valor_com_desconto:6.2f}")