curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
# O Is faz a verificação para saber se o conteúdo das variáveis são idênticos, nesse caso o valor retornado é True

curso is not nome_curso
# False

saldo is limite
# True


alunos = ["Carlos", "Maria", "Luana"];

turma = ["Carlos", "Luana", "Maria"];

print(alunos is turma)

print(alunos is not turma)

alunos = turma

print(alunos is turma)