'''
No exemplo, a variavel c recebe uma palavra ou frase.
Logo abaixo, usando o metodo `join` e `split` juntamos tudo e retiramos os espaços.
Em seguida com o metodo `len` contamos quantas letras possuem na palavra ou frase digitada
'''

palavra = input('Digite uma palavra/frase para saber quantas letras tem: ')
palavra = ''.join(palavra.split())
print('Sua palavra/frase tem ',len(palavra),' letras.')
