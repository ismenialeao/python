# Procurando um string dentro da outra

nome = str(input('Qual seu nome CompleTo?')).strip().upper()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))