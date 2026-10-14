contador = 0

while contador <= 10:
    contador = contador + 1
    if contador % 2 == 0:
        continue #Continue o laço se o if a cima n estiver certo, caso contrario continua normalmente o codigo

    print(contador)

print("Fim")