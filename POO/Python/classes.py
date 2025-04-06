# Definir classe Cat e instanciar o objeto no main

# class Cat:
#     def __init__(self):
#         pass


# Mia = Cat()
# print(Mia)    

# Inserir Atributos com valor fixo

# class Cat:
#     def __init__(self): # Todos os atributos sao instanciados dentro do init
#         self.age = 5

# Maizikeen = Cat()
# print(f'A idade da Maizi e: {Maizikeen.age}')

# Tom = Cat()
# print(f'A idade do Tom e: {Tom.age}')

# Inserir Atributos com passagem de parametros no construtor da class

# class Cat:
#     def __init__(self, age):
#         self.age = age

# Maizikeen = Cat(3)
# print(f'A idade da Maizi e: {Maizikeen.age}')

# Tom = Cat(6)
# print(f'A idade do Tom e: {Tom.age}')

# Atributos de Classe

# class Cat:
#     family = 'Felineos'

#     def __init__(self, age):
#         self.age = age



# Maizikeen = Cat(3)
# print(f'A idade da Maizi e: {Maizikeen.age} e ela pertence a familia: {Maizikeen.family}')

# Tom = Cat(6)
# print(f'A idade do Tom e: {Tom.age}')

# Tipagem

# class Cat:
#     family = 'Felineos'

#     def __init__(self, age: int):
#         self.age: int = age



# Maizikeen = Cat(3)
# print(f'A idade da Maizi e: {Maizikeen.age} e ela pertence a familia: {Maizikeen.family}')

# Tom = Cat(6)
# print(f'A idade do Tom e: {Tom.age}')

# Verificando qual o tipo da classe do objeto

# class Cat:
#     family = 'Felineos'

#     def __init__(self, age):
#         self.age = age



# Maizikeen = Cat(3)
# print(f'A Maizikeen e um objeto de qual classe? R: {Maizikeen.__class__.__name__}')

# Atributos protegidos

class Cat:
    family = 'Felineos'

    def __init__(self, age: int, weight: int):
        self.__age = age;
        self.__weight = weight;

    def get_age(self) -> int:
        return self.__age

    def get_weight(self) -> int:
        return self.__weight 

    def set_weight(self, weight: int):
        self__weight = weight          


Chloe = Cat(7, 5)

print(f'Minha gata tem {Chloe.get_age()} anos e esta pesando {Chloe.get_weight()} quilos')
