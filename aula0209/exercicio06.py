salario = float(input("Digite o salario atual: "))
if salario <= 2000:
    reajuste = salario * 0.15
elif salario <= 5000:
    reajuste = salario * 0.10
else:
    reajuste = salario * 0.05

novo_sal = salario + reajuste

print(f"Novo salario R$ {novo_sal:.2f}")