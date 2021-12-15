#DOBRO TRIPLO RAIZ
##leia um numero mostre o dobro triplo e raiz qudarrada
n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro do {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. A raiz quadrade de {} é igual a {:.2f}.'.format(n,t,n,r))