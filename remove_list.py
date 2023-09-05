'''
Para remover um item uma lista usamos o metodo `pop`.
por padrão ele retira o ultimo item que pertence a lista.
Nesse pequeno exemplo é retirado a quantidade de itens desejado.
Ao final é exibido a lista atualizada.
'''

def remove():
  componentes.pop()

componentes = ['teclado', 'monitor', 'mouse', 'memoria', 'processador', 'fonte', 'fone', 'led']
print(componentes)
print('Quantos itens deseja remover da lista? ')
contador = 0
quantidade = abs(int(input(' ')))
while quantidade > len(componentes):
  print('Indice maior que a lista!')
  quantidade = abs(int(input(' ')))
  
while contador < quantidade:
  remove()
  contador += 1
print(componentes)
if componentes == []:
  print('A lista ficou vazia')
