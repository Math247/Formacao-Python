def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False

    acertou = False

    tentativas = 5

    while(not enforcou and not acertou):
        print("Você tem {} tentativas.".format(tentativas))
        print("Deseja chutar a palavra ou uma letra?")
        escolha = int(input("(1) Chutar | (2) Letra"))
        if escolha == 1:
            palavra = str(input("Digite uma palavra:"))
            if palavra == palavra_secreta:
                print("Você acertou!!")
                acertou = True
            else:
                print("Você errou...")
                tentativas -= 1
        if escolha == 2:
            palavra = str(input("Digite uma letra:"))
            for caractere in palavra_secreta:
                if caractere == palavra:
                    print("Tem essa letra na palavra!")
                    break
                else:
                    print("Não tem essa letra na palavra...")
                    tentativas -= 1
        if tentativas == 0:
            enforcou = True

    print ("Fim do jogo")

if(__name__ == "__main__"):
    jogar()