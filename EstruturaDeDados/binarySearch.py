def BinarySearch(data, lookingFor):
    start = 0
    end = len(data) - 1

    while start <= end:
        half = int((start + end)/2)
        if lookingFor > data[half]:
            start = half + 1
        elif lookingFor < data[half]:
            end = half - 1
        else:
            return half
    return -1  

lista = [1, 5, 7, 13, 35, 67, 79, 81, 150]
ValueLooked = 5

print("Retorno Pesquisa Binaria (Quantidade de tentativas): {}".format(BinarySearch(lista, ValueLooked)))           