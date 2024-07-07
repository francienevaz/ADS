# Converter um número decimal para binário
decimal = 12332
binario = bin(decimal)
print(binario)

# Converter um número decimal para hexadecimal
hexadecimal = hex(15487)
print(hexadecimal)

# Converter um número binário para decimal
bin_str = '0b1010'
decimal_from_bin = int(bin_str, 2)   # 2 é a base do número binário
print(decimal_from_bin)

# Converter um número hexadecimal para decimal
hex_str = '0xa'
decimal_from_hex = int(hex_str, 16)   # 16 é a base do número hexadecimal
print(decimal_from_hex)
