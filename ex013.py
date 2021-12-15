#REAJUSTE SALARIAL %15 aumento

salario = float(input('Qual é o salrio do funcionario? R$'))
novo =  salario + (salario * 15 / 100)

print('Um funcionario que ganhava R${:.2f} com 15% de aumento agora ganha R${:.2f}? R$' .format(salario, novo))