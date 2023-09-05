'''
Para remover um item uma lista usamos o metodo `pop`.
por padrão ele retira o ultimo item que pertence a lista.
Nesse pequeno exemplo é retirado a quantidade de itens desejado.
'''

def remove():
  l.pop()

l = ['teclado', 'monitor', 'mouse', 'memoria', 'processador', 'fonte', 'fone', 'led']
print(l)
print('Quantos itens deseja remover da lista? ')
a=0
q = abs(int(input(' ')))
while q > len(l):
  print('Indice maior que a lista!')
  q = abs(int(input(' ')))
  
while a < q:
  remove()
  a+=1
print(l)
if l == []:
  print('A lista ficou vazia')
