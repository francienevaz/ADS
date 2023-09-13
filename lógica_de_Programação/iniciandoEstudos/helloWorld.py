print("Hello World!");
print(1 + 10); 
print(1.5 + 1 + 0.4);
print(True);
print(False);

# Acima trabalhamos com alguns tipos de dados em python, tipo string, number, booleano

#  formas de executar o python no modo interativo: é só colocar python e apertar o enter; para sair execute exit();

# python -i 'nome do arquivo.py' -- para executar um arquivo que você está trabalhando

dir()  #retorna a lista de nomes no escopo local atual
dir(100) # com um argumento, retorna uma lista de atributos válidos para o objeto. no caso do número int, vai aparecer todos os métodos que podem ser usados no tipo Int
help() #Invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo ou informar por parâmentro qual o nome do módulo, função, classe, método ou variável.
help(100) 