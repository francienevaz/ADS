#  Em python os operadores lógicos o && e o || são: and e or, e o ! negação é not;
# Tirando as observações acima, mesmas regras que valem no Javascript vale no python no quesito operadores lógicos.
contatos_emergencia = []

not 1000 > 1500
not contatos_emergencia
not "saque 1500" # retorna False, pois a str em python preenchida é True
not "" # retorna True, pois a str vazia retornaria False por padrão

# Usando o not a gente consegue negar o valor de uma variável por exemplo, se ela foi verdadeira a gente nega ela e a mesma retorna False.

saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print(( saldo >= saque and saque <= limite ) or ( conta_especial and saldo >= saque ))
