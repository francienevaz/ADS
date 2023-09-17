msg = print('Calculo do consumo de energia em kwh')
tipo_instalacao = int(input('Escolha uma opção: \n [1] - Residência; \n [2] - Comercial; \n [3] - Indutrial: \n'))
kwh = float(input('Digite o seu consumo em kwh: '));

if tipo_instalacao == 1:
    if kwh <= 500:
        taxa_residencia = 0.40
    elif kwh > 500:
        taxa_residencia = 0.65
    print('\nA sua tarifa é R${:.2f}'.format((taxa_residencia * kwh)))
elif tipo_instalacao == 2:
    if kwh <= 100:
        taxa_comercial = 0.55
    elif kwh > 100:
        taxa_comercial = 0.60
    print ('\nA sua tarifa é R${:.2f}'.format ((taxa_comercial* kwh)))
elif tipo_instalacao == 3:
    if kwh <= 5000:
        taxa_industrial = 0.55
    elif kwh > 5000:
        taxa_industrial = 0.60
    print ('A sua tarifa é R${:.2f}'.format (taxa_industrial * kwh))
