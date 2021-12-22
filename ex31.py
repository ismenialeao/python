#Custo da viagem

distancia = float(input('Qual a distancia da viagem: '))
print('Vc esta prestes a começar uma viahem de {} KM'.format(distancia))
if distancia <= 200:

    print('o Preço da sua passagem  sera de {:.2f}'.format(distancia* 0.5))

else:

    print('E o preço da sua passagem sera de R$ {:.2f}' .format(distancia * 0.4))