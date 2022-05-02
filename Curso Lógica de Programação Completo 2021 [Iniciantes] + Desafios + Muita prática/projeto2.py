'''
Escreva um programa que, ao iniciar, gere um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.
'''

import random
numero_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um número de 1 a 10: '))
    if chute > numero_aleatorio:
        print('Você chutou acima!')
    elif chute < numero_aleatorio:
        print('Você chutou abaixo!')
    elif chute > 10:
        print('Chute apenas de 1 a 10!')
    else:
        acertou = True
        print('Você chutou certo!')