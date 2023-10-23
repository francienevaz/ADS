print(''' ====== Seja Bem Vindos a Loja da Franciene Vaz! ====== \n''')

def main():

# aqui estou usando o try para tratar os eventuais erros
    try:
        valor_unitario = float(input("Digite aqui o valor do produto adquirido: \n R$"))
        quantidade = float(input("Digite aqui quantos produtos você adquiriu: \n"))
        valor_total_sem_desconto = valor_unitario * quantidade

        porcentagem = 0

        if valor_total_sem_desconto < 1000:
            porcentagem = 0
        elif valor_total_sem_desconto  >= 1000 and valor_total_sem_desconto < 3000:
            porcentagem = 3
        elif valor_total_sem_desconto > 3000 and valor_total_sem_desconto < 5000:
            porcentagem = 5
        else:
            porcentagem = 8

        desconto = (porcentagem/100) * valor_total_sem_desconto
        valor_total_com_desconto = valor_total_sem_desconto - desconto

        print('\n Valor da sua compra sem desconto: R${:.2f}'.format((valor_total_sem_desconto)))
        print('\n Valor da sua compra com o desconto aplicado: R${:.2f}\n'.format((valor_total_com_desconto)))
        print('''
========================================================
                Obrigada e volte sempre!
        ''')

    except ValueError:
        print("Ocorreu um erro, digite um valor válido!")
        main() # chama a função novamente em caso de erro

if __name__ == '__main__':
    main()
