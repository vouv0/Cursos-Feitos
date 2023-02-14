# Criando modelo de Machine Learning
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier

#Lendo a planilha com os dados
credito = pd.read_csv('Credit.csv')

#Transformando os textos em números
labelencoder = LabelEncoder() # Transforma elementos categoricos em n°
for i in credito.select_dtypes(include='object'): #percorre o arquivo procurando elementos categoricos
    if i != 'class':
        credito[i] = labelencoder.fit_transform(credito[i])

#Transformando a tabela em um array Numpy
previsores = credito.iloc[:, 0:20].values #transforma em um array do Numpy 'todas as linhas e da coluna 0 a 19'
classe = credito.iloc[:, 20].values #transforma em um array do Numpy 'todas as linhas mas somente a coluna 20'


#Dividindo os dados pro Modelo testar e aprender (30% teste e 70% aprender)
##X = provisores e y = classe
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state=0)


#Treinando e Testando o modelo
##Treinando
floresta = RandomForestClassifier(n_estimators=500, random_state=0)
floresta.fit(X_treinamento, y_treinamento)

##Aprendendo
previsoes = floresta.predict(X_teste)

##Comparando e Testando
confusao = confusion_matrix(y_teste, previsoes)

taxa_acerto = accuracy_score(y_teste, previsoes)
print(taxa_acerto)
