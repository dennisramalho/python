# Laços de Repetição + Listas
'''
print('carregando...')
print('carregando...')
print('carregnado...')
'''
'''
for palavra in range(1,4):
    print('carregando...')
'''    
'''
for item in coleção:
    espressão
'''
'''
for item in range (1,21):
    print(item)
for item in range(1,20,2):
    print(item)

nomes = ['Dennis','Rubens','Ricardo','Socorro','Isis']
for nome in nomes:
    print(nome)
'''
'''
Problema 1 a N - Imprima os valores de 1 a N
input numero maximo
valor inicial = 1
loop de valor_inicial a numero_maximo
    print valor
'''
valor_maximo = int(input('Digite o valor máximo: '))
valor_inicial = 1
for numero in range(valor_inicial,valor_maximo + 1):
    print(numero)