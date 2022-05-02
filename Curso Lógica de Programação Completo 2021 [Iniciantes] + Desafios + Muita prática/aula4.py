# Coleções(listas)
preco_1 = 20
preco_2 = 50
preco_3 = 200
# Lista
precos = [20,50,200]
#          0, 1, 2
print(precos[0])
print(precos.index(200)) # descobrir qual o índice do item que possui valor 200

# Lista
diversidades = [15,'Dennis',True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])
# Laços em iteráveis
for preco in precos:
    print(preco)
'''
# Exemplo 5 - Scome os valores
Dado uma coleção de dados "idades" [15,46,75,34,23] imprima na tela a soma destes valores

Algorítimo usando pseudo-código:

idades = [15,46,75,34,23]
total = 0
loop idade em idades
    total = total + idade
print total
'''
idades = [15,46,75,34,23]
total = 0
for idade in idades:
    total = total + idade
print(total)