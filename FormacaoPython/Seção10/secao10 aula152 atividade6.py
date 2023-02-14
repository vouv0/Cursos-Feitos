def junta_frase(lista):
    frase_junta = '.'.join([str(i) for i in lista])
    return frase_junta


lista1 = ['casa carro', 'casa moto', 'casa caminhao']
print(junta_frase(lista1))
