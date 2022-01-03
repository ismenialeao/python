# Indice de massa corporal

peso = float(input('Qual seuu peso ? (kg)'))
altura = float(input('Qual sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format((imc)))

if imc < 18.5:
    print('Vc esta abaixo do pesso normal')
elif imc >= 18.5 and imc < 25:
    print('Faixa de pesso normal')
elif imc <= 25 and imc < 30:
    print('Vc esta com sobrepeso')
