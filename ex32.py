# Ano bisesto

ano = int(input('Que ano quer analisar? coloque 0 para o ano atual: '))

if ano == 0:
    ano = datetime.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSESTO'.format(ano))
else:
    print('O ano {} não é bissesto' .format(ano))