valor_conta = float(input("Digite o valor da conta do restaurante: "))
taxa_servico = valor_conta * 0.10
total_final = valor_conta + taxa_servico

print(f"A taxa de serviço R$ {taxa_servico:.2f}")
print(f"Total final da conta {total_final:.2f}")
