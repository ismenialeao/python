#Analisador de textos

nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome..')
print('Seu nome em letras minusculas é {}'. format(nome.upper()))
print('Seu nome em minusculas é {}' .format(nome.lower()))
print('seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome {} letras'.format(nome.find(' ')))