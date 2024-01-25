import random

def escolher_palavra():
    palavras = ['python', 'funcao', 'django', 'estudar', 'programacao']
    return random.choice(palavras)

def inicializar_palavra_secreta(palavra):
    return ['_'] * len(palavra)

def exibir_palavra_secreta(palavra_secreta):
    print(palavra_secreta)

def jogar_forca():
    palavra_secreta = escolher_palavra()
    palavra_secreta_atual = inicializar_palavra_secreta(palavra_secreta)
    tentativas_maximas = 6
    tentativas = 0

    print('Bem-vinda ao jogo da forca!')

    while True:
        exibir_palavra_secreta(palavra_secreta_atual)
        letra = input('Digite uma letra: ').lower()

        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    palavra_secreta_atual[i] = letra
            print('Letra correta!')
        else:
            print('Letra incorreta.')
            tentativas += 1

        if '_' not in palavra_secreta_atual:
            print(f'Parabéns! Você adivinhou a palavra:{palavra_secreta}')
            break

        if tentativas == tentativas_maximas:
            print(f'Enforcado. Você atingiu o número máximo de tentativas. A palavra era:{palavra_secreta}')
            break

    print("Fim do jogo.")


jogar_forca()