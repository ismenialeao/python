# analizando triangulos

print('_______________________')
r1 = float(input('Primeiro seguimento:'))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um tringulo.')
    if r1 == r2 and r2 == r3:
        print('Equilatero')

    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('isosceles')
else:
    print('Os seguimentos acima n podem formar um tringulo.')