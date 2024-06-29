# Ainda sobre proposições
# ∧ - E lógico
# ∨ - Ou lógico
# ¬ - Não lógico
# → - Implica lógico
# ↔ - Equivalência lógica
# ∼ - negação
# ⊕ - Ou exclusivo, é apenas uma das opções

#  1. Sabendo que uma proposição é um conjunto de palavras ou símbolos que
# retratam um pensamento de sentido completo e que pode ser classificado como
# verdadeiro ou falso, determine o valor lógico das seguintes proposições:
# a) 7<2 - Falso
# b) (3+2=8)’ - Verdadeiro
# c) 50<70 ∨ 4>-2 - Verdadeiro
# d) tg 45°=1 ∧ sen 45°=0,5 - Falso
# e) 4<10 ⊕ 5<9 - Falso
# f) 2+2=4 → 2+3=6 - Falso
# g) 2³=8 ↔ 2²=4 - Verdadeiro


p = True
q = True
r = False

print(p or q)   
print(p or r)
print(q and r)
print(not(q and r))
print(q or r)
print(not p)
print(not(p and r))