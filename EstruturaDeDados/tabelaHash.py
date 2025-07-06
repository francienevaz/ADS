class ElementoDaListaSimples:
    def __init__(self, chave=None, dado=None):
        self.chave = chave
        self.dado = dado
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None

    def inserir(self, chave, dado):
        nodo = ElementoDaListaSimples(chave, dado)
        if self.head == None:
            self.head = nodo
            return 0
        else:
            nodo.proximo = self.head
            self.head = nodo 
            return 0

    def imprimir(self):
        temp = self.head
        while temp:
            print(f"{temp.chave}\t{temp.dado}")
            temp = temp.proximo

class TabelaHash:
    def __init__(self):
        self.tam = 10
        self.length = 0
        self.h = [ListaEncadeadaSimples() for i in range(0, self.tam)]

    def hashFunc(self, k):
        k = list(k)
        return (ord(k[0]) + ord(k[1])) % self.tam

    def inserir(self, chave, dado):
        pos = self.hashFunc(chave)
        add = self.h[pos].inserir(chave, dado)


    def imprimir(self):
        for i in range(0, self.tam):
            self.h[i].imprimir()


#Programa principal
Teste = TabelaHash()
while True:
  print('1 - Inserir na tabela hash')
  print('2 - Remover na tabela hash')
  print('3 - Listar a tabela hash')
  print('4 - Sair')

  op = int(input("Escolha uma opção:"))
  if op == 1:
    chave = input('Digite a sigla de um estado: ')
    dado = input('Digite o nome do estado: ')
    Teste.inserir(chave, dado)
  elif op == 2:
    chave = input('Digite o que deseja remover: ')
    #IMPLEMENTAR
  elif op == 3:
      Teste.imprimir()
  elif op == 4:
    print('Encerrando...')
    break
  else:
    print("Selecione outra opção!\n")