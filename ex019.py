# Prof sortear alunos para passar, prog que leia o nome deles

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('terceiro aluno aluno: '))
n4 = str(input('quarto aluno: '))

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'. format(escolhido))