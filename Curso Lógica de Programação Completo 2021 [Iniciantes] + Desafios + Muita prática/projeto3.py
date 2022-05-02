'''
Projeto 3 - Medidor de Velocidade

Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua, cria um programa que recebe do usuário um valor que representa a velocidade e, com base nessa velocidade, diga se ele tomou uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima, seu programa deve exibir "não houve multa'; caso esteja até 10km acima, deve exibir: "levou multa leve"; caso esteja entre 11 e 20km acima da velocidade máxima, exibir: "levou multa grave"; e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravíssima.
'''
'''
velocidade_maxima = 80
velocidade = int(input('Qual era a sua velocidade? '))
if velocidade <= 80:
    print('Não houve multa.')
elif velocidade > 80 and velocidade <= 90:
    print('Levou multa leve.')
elif velocidade >= 91 and velocidade <=100:
    print('Levou multa grave.')
elif velocidade > 100:
    print('Levou multa gravíssima.')
'''
velocidade_maxima = 80
velocidade = int(input('Digite sua velocidade: '))
if velocidade <= velocidade_maxima:
    print('Não houve multa.')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('Levou multa leve.')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Levou multa grave.')
elif velocidade > velocidade_maxima + 20:
    print('Levou multa gravíssima.')