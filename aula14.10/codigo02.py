from random import randint # Biblioteca para numeros randomicos
magico = randint(1,1000) # Gerar um valor entre 1 e 1000
cont = 0 # Jogadas começam em 0
palpites = [] # Lista vazia de palpites (Vetor)

while True: # Loop infinito (Forçar encerra com Break)
    cont = cont + 1 # Contagem de jogadas

    if cont == 11: # Antes de jogar a11 vez, encerramos
        print("Suas tentativas acabaram!")

        break # Quebra o laço e vai para o fim
    print(f"Você esta na tentativa {cont}/10")

    palpite = int(input("Digite um palpite [1..1000]: "))
    palpites.append(palpite)

    if palpite == magico:
        print("parabens! Você ganhou")
        break
    else:
        print("Infelimente você não ganhou")
        if magico < palpite:
            print("Seu palpite fou alto...")
        else:
            print("Seu palpite foi baixo...")

print(f"O numero magico é {magico}")
print(f"Seus palpites foram {palpites}")
print("Fim do Jogo!")