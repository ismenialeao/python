# detector de palidromo / frases ao contario

frase = str(input('Digite uma frase:')).strip().upper() #tira o espaço e colca em maiuscula
palavras = frase.split() #separando palavras
juntar = ''.join(palavras) # junta os espaços
inverso = ''

for letra in range(len(juntar) -1, -1, -1): # vai a te letra 1 e vai voltando ao contario tras p frente
    print(juntar[letra])

#print('Vc digitou {}'.format(juntar))