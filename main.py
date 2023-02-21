print("Bem vindo no jogo de adivinhação")
print("******************************")

numero_secreto=42

chute_str = input("Digite o seu numero: ")

print("Você digitou", chute_str)
chute = int(chute_str)

acertou     = numero_secreto == chute
errou_maior = chute > numero_secreto
errou_menor = chute < numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if(errou_maior):
        print("Você errou :( .O seu chute foi maior que o numero secreto.")
    elif(errou_menor ):
        print("Você errou :( .O seu chute foi menor que o numero secreto.")

print("Fim de jogo")