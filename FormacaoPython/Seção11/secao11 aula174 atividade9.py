import xml.etree.ElementTree as xml
import os

def cria_estado(nome, cidades):
    element_estado = xml.Element('Estado', attrib={'Nome': nome})
    for cidade in cidades:
        element_cidade = xml.SubElement(element_estado, 'Cidade')
        element_cidade.text = cidade
    return element_estado


no_raiz = xml.Element('DadosRaiz')
no_estado = cria_estado('Rio Grande do Sul', ['Santa Maria', 'Porto Alegre'])
no_estado2 = cria_estado('São Paulo', ['Campinas', 'Serrana'])

no_raiz.append(no_estado)
no_raiz.append(no_estado2)

arvore = xml.ElementTree(no_raiz)

with open('exercicio9.xml', 'wb') as arquivo:
    arvore.write(arquivo)
