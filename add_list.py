'''Para adicionar itens em uma lista usamos o metodo `append`
No exemplo, enquanto a variavel for menor que 6, constinuara sendo adicionados itens na lista
em uma contagem crescente.
Ao final é mostrado a lista atualizada.'''


lista = []
contador = 0
while contador < 6:
  itens = input('Digite 6 itens para adicionar a lista ')
  contador = contador + 1
  lista.append(itens)

print('A sua lista é: ', lista)
