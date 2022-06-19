import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,21)
tentativa = 0
print("escolha o nivel digitando de 1 a 3")
print("(1) nivel facil (2) nivel médio (3) nivel dificil")
nivel = int (input("escolha a dificuldade: "))

if (nivel == 1):
    tentativa = 6
elif (nivel == 2):
    tentativa = 4
elif (nivel == 3):
    tentativa = 2



for rodada in range (1 , tentativa +1):
    print ("tentativa {} de {}". format(rodada,tentativa))
    print("Advinhe de 1 a 20")
    chute_str = input("Digite seu numero= ")
    chute = int(chute_str)
    print("você digitou", chute)

    maior = (numero_secreto > chute)
    menor = (numero_secreto < chute)
    acertou = (numero_secreto == chute)

    if (chute > 20 or chute < 1):
        print("use numeros de 1 a 20")
        continue
        

    if (acertou):
        print("Acertou!!")
        break
    else:
        if (maior):
            print("Dica: este numero é menor que o escolhido")
        elif (menor):
            print("Dica: este numero é maior que o escolhido")
    rodada = rodada + 1
print("fim do jogo!")
