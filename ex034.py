#Aumento de multiplos, porcentagem

salario = float(input('Qual é o salario do funcionario: '))
if salario <= 1250:
    novo = salario + (salario *15 / 100)
else:
    novo = salario +(salario *10 / 100)
print('Quem ganhava {:.2f} passa a ganhar agora {:.2f}'.format(salario , novo))