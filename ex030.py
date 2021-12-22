# Radar eletronico acima de 80 é multa

velocidade =  float(input('Qual velocidade do carro? '))

if velocidade > 80:
    print('Voce excedeu o limite, MULTADO pois esta acima de 80 km/h!')
    multa = (velocidade -80) * 7
    print('Voce deve pagar uma multa de R$ {:.2f}!' .format(multa))
print('Tenha um boa dia, dirija com segurança.')