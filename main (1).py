tam_atual = 0
tam_max = 100
lista = []*tam_max

class vazia():
  if len(lista) == tam_atual:
    print('Lista vazia')
  else:
    print('Lista não vazia')

class cheia():
  if tam_atual == tam_max:
    print("lista cheia")
  else:
    print("lista não cheia")

class tam_lista():
  print(len(lista))
