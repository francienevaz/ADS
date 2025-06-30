#Cria cada elemento da lista
class ElementoDaListaSimples:
# construtor de inicialização da classe
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

#__repr__ é um método especial do Python
#use-o para criar a maneira como objeto 
#é mostrado fora da função print
    def __repr__(self):
        return self.dado

#Cria a lista encadeada simples
class ListaEncadeadaSimples:
  def __init__(self, nodos=None):
    self.head = None
    if nodos is not None:
        nodo = ElementoDaListaSimples(dado=nodos.pop(0))
        self.head = nodo
        for elem in nodos:
            nodo.proximo = ElementoDaListaSimples(dado=elem)
            nodo = nodo.proximo

  def __repr__(self):
      nodo = self.head
      nodos = []
      while nodo is not None:
          nodos.append(nodo.dado)
          nodo = nodo.proximo
      nodos.append("None")
      return " -> ".join(nodos)

#Varre a lista
  def __iter__(self):
    nodo = self.head
    while nodo is not None:
        yield nodo
        nodo = nodo.proximo

  def inserirNoInicio(self, nodo):
    nodo.proximo = self.head
    self.head = nodo

  def inserirNoFinal(self, nodo):
    if self.head is None:
        self.head = nodo
        return

    nodo_atual = self.head
    while nodo_atual.proximo != None:
        nodo_atual = nodo_atual.proximo

    nodo_atual.proximo = nodo
    return

  def deletar(self, dado):
    if self.head is None:
        raise Exception("A lista está vazia!")

    if self.head.dado == dado:
        self.head = self.head.proximo
        return

    nodo_anterior = self.head
    for nodo in self:
        if nodo.dado == dado:
            nodo_anterior.proximo = nodo.proximo
            return
        nodo_anterior = nodo

    raise Exception("Nó com o dado '%s' não foi econtrado." % dado)

Teste = ListaEncadeadaSimples()

while True: 
  print('1 - Inserir na início da lista encadeada')
  print('2 - Inserir na final da lista encadeada')
  print('3 - Remover da lista encadeada')
  print('4 - Imprimir a lista encadeada')
  print('5 - Sair')

  op = int(input("Escolha uma opção:")) 
  if op == 1: 
    dado = input('Qual número deseja inserir?')
    Teste.inserirNoInicio(ElementoDaListaSimples(dado))
  if op == 2: 
    dado = input('Qual número deseja inserir?')
    Teste.inserirNoFinal(ElementoDaListaSimples(dado))
  elif op == 3: 
    dado = input('Qual número deseja remover?')
    Teste.deletar(dado)
  elif op == 4:
    for nodo in Teste:
      print(nodo, end=' -> ')
    print('None')
  elif op == 5: 
    print('Encerrando...')
    break
  else: 
    print("Selecione outra opção!\n")