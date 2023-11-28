"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'peixe'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Favor digite apenas letra!')
        continue

#   Aqui verifica se a letra que o jogador digitou está na palavra secreta

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('palavra_formada', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('PARABÉNS VOCÊ ACERTOU!')
        print('A palavra screta é: ', palavra_secreta)
        print('Tentativas', numero_tentativas)
