palavra_secreta = 'Peixe frito'
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Favor digite apenas letra!')
        continue
#   Aqui verifica se a letra que o jogador digitou está na palavra secreta
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    print(letras_acertadas)
