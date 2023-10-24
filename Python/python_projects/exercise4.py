def main():
    print("----- Seja Bem Vindo ao Controle de Livros da Franciene Vaz -----")
    #Iniciando as variáveis
    lista_livros = []
    id_global = 0

    #Definindo as funções
    def cadastrar_livro(id):
        print("------------------- Menu Cadastrar Livros -------------------")
        print(f'Id do livro {id}')
        livro = input("Por favor digite o nome do livro: ")
        autor = input("Por favor digite o nome do autor: ")
        editora = input("Por favor digite o nome da editora: ")
        
        dicionario = {'id' : id , 'livro' : livro, 'autor' : autor, 'editora' : editora}
        lista_livros.append(dicionario)

    def consultar_livro():
        print("------------------- Menu Consultar Livros -------------------")
        consulta = input(''' 
            Escolha a opção desejada:
            1 - Consultar todos
            2 - Consultar por id
            3 - Consultar por autor
            4 - Retornar ao menu principal
        ''')
        # Se "consulta" não estiver entre os dados dessa array, retorna "opção inválida"
        if consulta not in ['1', '2', '3', '4']:
            print('Opção inválida')
        else:
            if consulta == '1':
                 for livro in lista_livros:
                    print(f"id: {livro['id']}, nome: {livro['livro']}, autor: {livro['autor']}, editora: {livro['editora']}")
            elif consulta == '2':
                id_consulta = int(input("Digite o ID do livro que deseja consultar: "))

                # Verifica se id_consulta é maior ou igual a 1, e se é menor que o tamanho da lista, caso contrário retorna "ID não encontrado."
                if 1 <= id_consulta <= len(lista_livros):
                    
                    # livro recebe o livro correspondente
                    livro = lista_livros[id_consulta - 1]

                    # Imprime o livro com o índice aumentado em 1
                    print(f"ID: {id_consulta}, Livro: {livro['livro']}, Autor: {livro['autor']}")
                else:
                    print("ID não encontrado.")

                # print(lista_livros[id_consulta])

            elif consulta == '3':
                #Solicita o nome do autor a ser consultado  
                autor_consulta = input("Digite o nome do autor que deseja consultar: ")

                #Para cada livro em lista_livros se o nome do autor for igual ao recebido em autor_consulta, livros_autor recebe os dados do livro
                livros_autor = [livro for livro in lista_livros if livro['autor'] == autor_consulta]

                #imprime a lista para cada livro em livros_autor
                for livro in livros_autor:
                    print(f"autor: {livro['autor']}, id: {livro['id']}, nome: {livro['livro']}, editora: {livro['editora']}")
            else:
                return

    def remover_livro():
        print("--------------------- Menu Remover Livros ---------------------")
        remover_id = int(input("Por favor digite o ID do livro que deseja excluir: "))

        # Para cada indice do livro na lista_livros, verifica se o id do livro é igual ao remover_id, depois deleta o indice correspondente e saí do loop
        for i, livro in enumerate(lista_livros):
            if livro['id'] == remover_id:
                del lista_livros[i]
                break

    while True:
        print("----------------------- Menu Principal -----------------------")
        opcao = input('''
            Digite a opção desejada:
            1 - Cadastrar livro
            2 - Consulta livro
            3 - Remover livro
            4 - Encerrar programa
        ''')
        # Se "opcao" não estiver entre os dados dessa array, retorna "opção inválida"
        if opcao not in ['1', '2', '3', '4']:
            print('Opção inválida')
        else:
            if opcao == '1':
            # a id_global é incrementada
                id_global += 1
                cadastrar_livro(id_global)
            elif opcao == '2':
                consultar_livro()
            elif opcao == '3':
                remover_livro()
            else:
                return

# Início do programa - boa prática usar essa estrutura no fim do arquivo python
if __name__ == '__main__':
    main()