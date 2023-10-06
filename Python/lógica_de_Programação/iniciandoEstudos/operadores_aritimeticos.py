# Precedência em python: parênteses >> expoêntes >> multiplicações e divisões >> somas e subtrações

valor_1 = 9;
valor_2 = 3;

print(valor_1 + valor_2);
print(valor_1 - valor_2);
print(valor_1 // valor_2);
print(valor_1 / valor_2);
print(valor_1 * valor_2);
print(valor_1 ** valor_2);

x = 10 + (5 * 4) ** 2 - 10;
print(x)

print(10 - 5 * 2);
print((10 - 5) * 2)
print(10 ** 2 * 2)
print(10 ** (2 * 2))
print(10 // 2 * 4)