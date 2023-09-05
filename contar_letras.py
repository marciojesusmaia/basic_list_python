'''
Neste exemplo temos uma lista com o nome de algumas linguagems de programação.
A função indice verifica se o indice escolhido contem na lista.
Caso seja escolhido um indice dentro do range da lista será contado a quantidade de letras daquela palavra escolhida.
Tambem é verificado se foi digitado algo diferente de numeros.
'''


linguagens=['C','PYTHON','GO LANG','PHP','JAVA','C++','C#','COBOL','JAVA SCRIPIT']
print(linguagens)
def indice():
  indice = int(input('Qual o indice você escolhe? '))
    
  while indice > 8:  
    linguagens.index == indice
    print('index error')
    indice=int(input('Qual o indice você escolhe? '))

  if indice < 9:
    contagem = ''.join(linguagens[indice].split())
    print(linguagens[indice])
    print('O indice escolhido tem ', len(contagem),'letras')

try:
  indice()

except ValueError:
  print('somente números!')
  indice()
