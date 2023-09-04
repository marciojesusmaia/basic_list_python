'''Para adicionar itens em uma lista usamos o metodo `append`
No exemplo, enquanto a variavel for menor que 6, constinuara sendo adicionados itens na lista
em uma contagem crescente.'''


l2 = []
a=0
while a<6:
  i=input('Digite 6 itens para adicionar a lista ')
  a=a+1
  l2.append(i)

print('A sua lista é: ', l2)
