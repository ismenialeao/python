# CATETO HIPOTENUSA
import math

co = float(input('comprimento do cateto posto: '))
ca = float(input('comprmento do cateto adjascente: '))

hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))