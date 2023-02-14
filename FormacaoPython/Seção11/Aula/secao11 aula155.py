#Open ('nome_do_arquivo.txt', 'rt')
#1a Parte:
#'r' - Abre arquivo pra leitura, precisa existir, caso não (erro).
#'a' - Abre arquivo pra anexar qlq coisa, caso não exita ele cria.
#'w' - Abre arquivo para escrita, caso não exita ele cria.
#'x' - Cria um arquivo, se existir retorna um erro.

#2a Parte:
#'t' - Abre um arquivo em modo texto
#'b' - Abre um arquivo em modo binário


# arquivo = open('exemplo.txt', 'wt') #Nome do arquivo + 'w' = cria e escreve no arquivo e 't = formato texto
# arquivo.write('Olá esse é um arquivo de teste.\n')
# arquivo.write('Segunda linha do arquivo.')
# arquivo.close() #Sempre tem que fechar o arquivo


lista = ['Ana', 'João', 'Maria', 'José']
arquivo = open('nomes.txt', 'wt')
for i in lista:
    arquivo.write(f'{i}\n')
arquivo.close()
