#Progressao aritimetrica

pri = int(input('Primeiro termo: '))
ra = int(input('Razão :'))
dec = pri + (10 - 1) *ra
for c in range(pri, dec, ra):
    print('{}'.format(c), end='->')
    print('Acabou')