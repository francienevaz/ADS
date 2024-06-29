renda = float(input('Digite a sua renda mensal:'))
percentual = 0.20
limiteFinanciamento = renda * percentual

outrosFinanciamentos = int(input('''Você possui outros financiamentos?'
                             1 - Sim
                             2 - Não '''))

if outrosFinanciamentos == 1:
    outrosFinanciamentos = float(input('Digite o valor dos outros financiamentos: '))
    if renda >= 8500 and outrosFinanciamentos < limiteFinanciamento:
        print('Seu financiamento foi Aprovado!')
    else:
        print('Seu financiamento foi Negado!')
elif outrosFinanciamentos == 2:
    outrosFinanciamentos = 0
    if renda >= 8500 and outrosFinanciamentos < limiteFinanciamento:
        print('Seu financiamento foi Aprovado!')
    else:
        print('Seu financiamento foi Negado!')
else:
    print('Valor inválido!')
