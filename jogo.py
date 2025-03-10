"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
 - Você vai propor uma palavra secreta qualquer e vai dar a
possibilidade para o usuário digitar apenas uma letra.
 - Quando o usuário digitar uma letra, você vai conferir
se a letra digitada está na palavra secreta.
 - Se a letra digitada estiver na palavra secreta;
exiba a letra;
 - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

print("""
+--------------------------------------+
|------------------Jogo----------------|
|-------------------da-----------------|
|-----------------Forca!---------------|
+----------------------------by-Hyuri--+
""")

from random import choice

palavras = ["cadeira", "cachorro", "caneca", "melancia", "python"]
palavra = choice(palavras)
palavra = palavra.lower()
erro = ''
erros = ''
acerto = ''
acertos = ''

while True:
    print('')
    print('Tente adivinhar a palavra secreta!')
    chute = input('Chute apenas uma letra: ')

    if len(chute) >= 2 or len(chute) <= 0:
        print('Diga apenas uma letra!')
        continue

    if chute in acertos or chute in erro:
        print('Você já chutou essa letra!')
        continue

    if chute in palavra:
        print(f'Parabéns, a palavra secreta contém {chute}!')
        acertos += chute
        acerto = ''
        for i in palavra:
            if i in acertos:
                acerto += i
            if i not in acertos:
                acerto += '_'
        print(acerto)
    
    if len(erros) >= 10:
        print('Droga, você perdeu :(')
        print(f'A palavra era {palavra} !')
        print('Fim de jogo!')
        break

    if chute not in palavra:
        print(f'A palavra não contém {chute}.')
        erro += chute
        erros += 'X'
        if len(erros) > 5:
            print(f'Cuidado! Você só tem mais {10 - len(erros)}!')

    print(f'Erros: {erros}')



    if acerto == palavra:
        print('Parabéns! Você ganhou!')
        print(f'A palavra era {palavra} !')
        print('Fim de jogo!')
        break        
