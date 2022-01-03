 #validação de dados
sexo = str(input('Qual seu sexo [M/F]? ')).strip().upper()[0]    #tira espaço joga pro maiusculo e tira primeira letra
while sexo not in 'MmFf': # enquanto o sexo n tivem em masc fem
  sexo = str(input('Dados invalidos. Por favor informe seu sexo')).strip().upper()[0]
print('Sexo {} registrado com sucesso .' .format(sexo))