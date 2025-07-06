class ElementoDaListaSimples:
    def __init__(self, sigla=None, nomeEstado=None):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None

    def inserir(self, sigla, nomeEstado):
        nodo = ElementoDaListaSimples(sigla, nomeEstado)
        if self.head is None:
            self.head = nodo
        else:
            nodo.proximo = self.head
            self.head = nodo
        return 0

    def remover(self, sigla):
        current = self.head
        previous = None

        while current is not None:
            if current.sigla == sigla:
                if previous is None:
                    self.head = current.proximo
                else:
                    previous.proximo = current.proximo
                return True
            previous = current
            current = current.proximo
        return False

    def imprimir(self):
        temp = self.head
        elementos_na_posicao = []
        while temp:
            elementos_na_posicao.append(temp.sigla)
            temp = temp.proximo
        return " -> ".join(elementos_na_posicao) if elementos_na_posicao else "Vazio"

class TabelaHash:
    def __init__(self):
        self.tam = 10
        self.length = 0
        self.h = [ListaEncadeadaSimples() for _ in range(0, self.tam)]

    def hashFunc(self, k):
        if k == "DF":
            return 7
        else:
            if len(k) < 2:
                raise ValueError("A sigla deve ter pelo menos duas letras.")
            char1_ascii = ord(k[0])
            char2_ascii = ord(k[1])
            return (char1_ascii + char2_ascii) % self.tam

    def inserir(self, sigla, nomeEstado):
        pos = self.hashFunc(sigla)
        self.h[pos].inserir(sigla, nomeEstado)

    def remover(self, sigla):
        pos = self.hashFunc(sigla)
        return self.h[pos].remover(sigla)

    def imprimir(self):
        for i in range(0, self.tam):
            print(f"{i}: {self.h[i].imprimir()}")

# Programa principal
Teste = TabelaHash()
Teste.inserir("FR", "Franciene Vaz")

while True:
    print('\n--- Menu da Tabela Hash ---')
    print('1 - Inserir um novo estado na tabela hash')
    print('2 - Remover um estado da tabela hash')
    print('3 - Listar a tabela hash')
    print('4 - Sair')
    
    op = int(input("Escolha uma opção: "))
    if op == 1:
        chave = input('Digite a sigla do estado (2 letras): ').upper()
        dado = input('Digite o nome completo do estado: ')
        Teste.inserir(chave, dado)
        print(f"Estado {chave} - {dado} inserido com sucesso!")
    elif op == 2:
        chave = input('Digite a sigla do estado que deseja remover: ').upper()
        if Teste.remover(chave):
            print(f"Estado com sigla '{chave}' removido com sucesso!")
        else:
            print(f"Estado com sigla '{chave}' não encontrado na tabela.")
    elif op == 3:
        Teste.imprimir()
    elif op == 4:
        print('Encerrando...')
        break
    else:
        print("Selecione outra opção!\n")
   