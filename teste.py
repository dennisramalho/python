# Python

# RESOLUÇÃO 1: recebendo do usuário os valores (com uso do input):

comprimento_da_pista = int(input('Qual o comprimento da pista? '))
numeros_de_voltas_a_percorrer = int(input('Qual o número de voltas a percorrer? '))
numero_de_voltas_ate_o_primeiro_abastecimento = int(input('Qual o número de voltas até o primeiro abastecimento? '))
consumo_do_carro = int(input('Qual o consumo do carro? '))

min_gas_primeiro_abastecimento = comprimento_da_pista * numero_de_voltas_ate_o_primeiro_abastecimento / consumo_do_carro

print(f'O número mínimo de litros necessários para percorrer até o primeiro reabastecimento é {min_gas_primeiro_abastecimento} litros.')


#RESOLUÇÃO 2: já com valores atribuídos:

comprimento_da_pista = 8000
numeros_de_voltas_a_percorrer = 50
numero_de_voltas_ate_o_primeiro_abastecimento = 8
consumo_do_carro = 10000

min_gas_primeiro_abastecimento = comprimento_da_pista * numero_de_voltas_ate_o_primeiro_abastecimento / consumo_do_carro

print(f'O número mínimo de litros necessários para percorrer até o primeiro reabastecimento é {min_gas_primeiro_abastecimento} litros.')