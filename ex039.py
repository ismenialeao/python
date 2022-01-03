#alistamento militar

from datetime import date
atual = date.today().year
nasc = int(input('Ano nascimento: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.' .format(nasc, idade, atual))
if idade == 18:
    print('Vc tem de se alistar')
elif idade < 18:
    saldo = 18 - idade
    print('Vc não tem ainda 18 anos faltam {} para se alistar'.format(saldo))

elif idade > 18:
    saldo = idade - 18
    print('Vc deveria ter se alisatado ha {} anos.'.format(saldo))
