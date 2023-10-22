def main():
    print("Seja Bem Vindos!")
    lista_livros = []
    id_global = 0

    def cadastrar_livro(id):
        livro = input("Por favor digite o nome do livro: ")
        autor = input("Por favor digite o nome do autor: ")
        editora = input("Por favor digite o nome da editora: ")
        
        dicionario = {'id' : id , 'livro' : livro, 'autor' : autor, 'editora' : editora}
        lista_livros.append(dicionario)

    def consultar_livro():
        consulta = input(''' 
            Escolha a opção desejada:
            1 - Consultar todos
            2 - Consultar por id
            3 - Consultar por autor
            4 - Retornar ao menu principal
        ''')
        
        if consulta not in ['1', '2', '3', '4']:
            print('Opção inválida')
        else:
            if consulta == '1':
                print(lista_livros)
            elif consulta == '2':
                id_consulta = int(input("Digite o ID do livro que deseja consultar: "))
                print(lista_livros[id_consulta])
            elif consulta == '3':    
                autor_consulta = input("Digite o nome do autor que deseja consultar: ")
                livros_autor = [livro for livro in lista_livros if livro['autor'] == autor_consulta]
                print(livros_autor)
            else:
                return

    def remover_livro():
        remove_id = int(input("Por favor digite o ID do livro que deseja excluir: "))
        for i, livro in enumerate(lista_livros):
            if livro['id'] == remove_id:
                del lista_livros[i]
                break

    while True:
        opcao = input('''
            Digite a opção desejada:
            1 - Cadastrar livro
            2 - Consulta livro
            3 - Remover livro
            4 - Encerrar programa
        ''')
        
        if opcao not in ['1', '2', '3', '4']:
            print('Opção inválida')
        else:
            if opcao == '1':
                id_global += 1
                cadastrar_livro(id_global)
            elif opcao == '2':
                consultar_livro()
            elif opcao == '3':
                remover_livro()
            else:
                return

if __name__ == '__main__':
    main()