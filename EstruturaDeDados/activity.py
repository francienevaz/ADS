# Cria cada elemento da lista
class ElementoDaListaSimples:
    # construtor de inicialização da classe
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

    #__repr__ é um método especial do Python
    # use-o para criar a maneira como objeto 
    # é mostrado fora da função print
    def __repr__(self):
        return f"{self.cor}, {self.numero}"

# Cria a lista encadeada simples
class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None
        self.proximo_numero_verde = 1
        self.proximo_numero_amarelo = 201

    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(str(nodo))
            nodo = nodo.proximo
        nodos.append("None")
        return " -> ".join(nodos)

    # Varre a lista
    def __iter__(self):
        nodo = self.head
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

    def inserirSemPrioridade(self, nodo):
        """
        Deve-se andar pela lista a partir da cabeça (head) e inserir o nodo no final da lista.
        """
        if self.head is None:
            self.head = nodo
            return

        nodo_atual = self.head
        while nodo_atual.proximo is not None:
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = nodo

    def inserirComPrioridade(self, novo_nodo):
        """
        Deve-se andar pela lista a partir da cabeça (head) e inserir o nodo após todos os nodos com cor “A” que estão na lista.
        O nodo inserido deve sempre estar antes de todos os nodos com cor “V”.
        """
        if self.head is None:
            self.head = novo_nodo
            return

        # Se o novo nodo é 'A' e o head é 'V', insere no início
        if novo_nodo.cor == 'A' and self.head.cor == 'V':
            novo_nodo.proximo = self.head
            self.head = novo_nodo
            return

        nodo_atual = self.head
        # Encontra o último nodo 'A' ou o nodo antes do primeiro 'V'
        while nodo_atual.proximo is not None and nodo_atual.proximo.cor == 'A':
            nodo_atual = nodo_atual.proximo

        novo_nodo.proximo = nodo_atual.proximo
        nodo_atual.proximo = novo_nodo

    def inserir(self):
        """
        Solicita ao usuário a cor, atribui o número automaticamente e insere o nodo na fila.
        """
        while True:
            cor = input("Qual a cor do cartão? (A - Amarelo, V - Verde): ").upper()
            if cor in ['A', 'V']:
                break
            else:
                print("Cor inválida! Por favor, digite 'A' ou 'V'.")

        if cor == 'V':
            numero = self.proximo_numero_verde
            self.proximo_numero_verde += 1
        else: # cor == 'A'
            numero = self.proximo_numero_amarelo
            self.proximo_numero_amarelo += 1

        novo_paciente = ElementoDaListaSimples(numero=numero, cor=cor)

        if self.head is None:
            self.head = novo_paciente
        elif novo_paciente.cor == 'V':
            self.inserirSemPrioridade(novo_paciente)
        elif novo_paciente.cor == 'A':
            self.inserirComPrioridade(novo_paciente)
        
        print(f"Paciente {novo_paciente.cor}{novo_paciente.numero} adicionado à fila.")


    def imprimirListaEspera(self):
        """
        Imprime todos os cartões e seus respectivos números a partir do primeiro até o último da lista.
        """
        if self.head is None:
            print("A fila de espera está vazia.")
            return

        print("--- Pacientes na fila ---")
        for nodo in self:
            print(nodo, end=' -> ')
        print('None')
        print("-------------------------")

    def atenderPaciente(self):
        """
        Remove o primeiro paciente da fila e imprime uma mensagem chamando o paciente para atendimento.
        """
        if self.head is None:
            print("Não há pacientes na fila para atendimento.")
            return

        paciente_atendido = self.head
        self.head = self.head.proximo
        print(f"Chamando paciente: {paciente_atendido.cor}{paciente_atendido.numero}. Dirija-se ao consultório.")


# --- Menu ---
fila_hospital = ListaEncadeadaSimples()

while True:
    print("\n--- Menu do Sistema de Triagem ---")
    print("1 - Adicionar paciente à fila")
    print("2 - Mostrar pacientes na fila")
    print("3 - Chamar paciente")
    print("4 - Sair")

    op = int(input("Escolha uma opção: "))
    if op == 1:
        fila_hospital.inserir()
    elif op == 2:
        fila_hospital.imprimirListaEspera()
    elif op == 3:
        fila_hospital.atenderPaciente()
    elif op == 4:
        print('Encerrando...')
        break
    else:
        print("Selecione outra opção!\n")