'''
Para remover um item em especifico usamos o metodo `remove`.
No exemplo abaixo, podemos escolher qual o item da lista desejamos escolher,
e ao final exibimos o resultado sem o item que foi escolhido para retirada.
'''


sistemas = ['linux', 'solaris', 'windows', 'unix', 'android', 'ios', 'chromeOs']
print(sistemas)
escolha = input('Qual item deseja remover da lista? ')
sistemas.remove(escolha)
print(sistemas)
