distance = float(input('Digite a distância percorrida em km: '))
tempo = float(input('Digite o tempo de viagem em horas: '))

vm = distance / time

if vm > 110:
    print('Você ultrapassou o limite de velocidade média de 110 km/h.')
else:
    print('Você viajou dentro do limite de velocidade média de 110 km/h.')
