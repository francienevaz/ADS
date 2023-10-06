def sacar (self, valor: float) -> None:
                                          # início do bloco do método
     if self.saldo >= valor:
                              # início do bloco do if
         self.saldo -= valor
     # fim do bloco do if
 # fim do bloco do método



# ISSO NÂO FUNCIONA EM PYTHON:
# def sacar (self, valor: float) -> None: # início do bloco do método
#  if self.saldo >= valor:
                         # início do bloco do if
#  self. saldo - = valor
# fim do bloco do if
# fim do bloco do método

# void sacar(double valor) {
#  if (this.saldo >= valor) {
# this.saldo -= valor;}}

def sacar (self, valor: float) -> None:
     if self.saldo >= valor:
         self. saldo -= valor

# A indentação em python é obrigatória para que o código funcione, sendo necessário separar os blocos por 4 espaços para delimitar o início de e fechamento de um bloco, como nos exemplos anteriores

def saque (valor):
    saldo  = 500

    if saldo >= valor:
        print("valor sacado!")
    

saque(500)