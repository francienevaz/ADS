atividade_praticaI = float(input('Digite a nota obtida na atividade 1: '))
atividade_praticaII = float(input('Digite a nota obtida na atividade 2: '))
prova = float(input('Digite a nota obtida na prova: '))

apolI = atividade_praticaI * 0.20
apolII = atividade_praticaII * 0.30
nota_prova = prova * 0.50

nota = apolI + apolII + nota_prova

print(atividade_praticaI)
print(atividade_praticaII)
print(prova)
print(nota)

if nota < 30:
    print("Reprovado")
elif nota >= 30 and nota < 70:
    print("Recuperação")
elif nota >= 70:
    print("Aprovado")
else:
    print("Nota inválida")
    
