# Analizador completo
# nome idade e sexo de 4 pessoas, mais velhos e menor de 20 anos

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totalmulher20 = 0
for p in range(1, 5):
    print('---------{}º pessoa -------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade :'))
    sexo = str(input('sexo [M/F] : ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm' : #coloca Mm no lugar de  == para aceitar maiusculo ou minusculo
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1

mediaidade = somaidade / 4
print('A media de idade é de {}'.format(mediaidade))
print('O homem mais velho tem {}'.format(maioridadehomem, nomevelho))
print('São {} mulheres com menos de 20 anos' .format(totalmulher20))