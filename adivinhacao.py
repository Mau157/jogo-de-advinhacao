print("**********************************************************")
print("Bem vindo ao jogos mortais e adivinhe se vc está com sorte")
print("**********************************************************")

numero_secreto = 50
tentativa = 3
rodada = 1

while (tentativa > 0):
    print ("Rodada {} do total de tentativa {}".format(rodada, tentativa))
    chute = int(input("Fale o seu valor e vamos descobrir se vc está com sorte ou azar kkkk?"))
    tentativa = tentativa - 1
    if (chute == numero_secreto):
        print ("vc está com sorte e sai já daqui kkkkk")
        break
    elif (chute >= numero_secreto):
        print ("errou, o número chutado é maior que o valor secreto")
    elif (chute <= numero_secreto):
        print ("errou, o número chutado é menor que o valor secreto")
    rodada = rodada + 1
print ("Game Over")