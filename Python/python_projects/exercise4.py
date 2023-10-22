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
	consulta = input(int(''' 
		Escolha a opção desejada:
		1 - Consultar todos
		2 - Consultar por id
		3 - Consultar por autor
		4 - Retornar ao menu principal
	'''))
	
	if consulta not in [1, 2, 3, 4]:
		print('Opção inválida')
	else:
		if consulta == 1 :
			print(lista_livros)
		elif consulta == 2 :
			print(lista_livros[id])
		elif consulta == 3 :	
			print(lista_livros[autor])
		else:
			return menu_principal
def remover_livro():
	remove_id = input("Por favor o ID do livro que deseja excluir: ")
	lista_livros.remove(remove_id)

opcao = input(int('''
	Digite a opção desejada:
	1 - Cadastrar livro
	2 - Consulta livro
	3 - Remover livro
	4 - Encerrar programa
	'''))
if opcao not in [1,2,3,4]:
	print('Opção inválida')
else:
	if opcao == 1:
		id_global += 1
		cadastrar_livro(id_global)
	elif opcao == 2:
		consultar_livro()
	elif opcao == 3:
		remover_livro()
	else:
		return



	