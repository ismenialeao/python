# classico media aula

nota1 = float(input('Primrira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a mededia do aluno é {:.1f}' .format(nota1, nota2, media))

if 7 > media >= 5:
    print('O aluno esta em recuperação.')
elif media < 5:
    print('O aluno esta reprovado.')
else :
print('O aluno esta aprovado.')