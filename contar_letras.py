l1=['C','PYTHON','GO LANG','PHP','JAVA','C++','C#','COBOL','JAVA SCRIPIT']
print(l1)
def indice():
  a = int(input('who the index of list? '))
    
  while a > 8:  
    l1.index == a
    print('index error')
    a=int(input('Qual o indice você escolhe? '))

  if a < 9:
    b = ''.join(l1[a].split())
    print(l1[a])
    print('O indice escolhido tem ', len(b),'letras')

try:
  indice()

except ValueError:
  print('somente números!')
  indice()
