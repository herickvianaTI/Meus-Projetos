import pandas as panda

#carrega arquivo para dataframe Pandas
dados = panda.read_csv('Credit.csv')

#formato
dados.shape

#resumo estatístico de colunas numericas
dados.head()

#últimos registros com parâmetros
dados.tail(2)

#filtros por nome da coluna
dados[["duration"]]

#filtrar linhas por indice
dados.loc[1:3]

#linhas 1 e 3
dados.loc[[1,3]]

#filtro
dados.loc[dados['purpose'] == "radio/tv"]

#outra condição
dados.loc [dados['credit_amount'] > 18000]

#atribuimos resultado a variável, criando outro df
credito2 = dados.loc[dados['credit_amount'] >  18000]
print(credito2)

#serie a partir de um array do numpy
import numpy as np
array1 = np.array([2,5,3,34,54,23,1,16])
s2 = pd.Series(array1)
print(s2)

#series a partir de um dataframe
s3 = dados['purpose']
print(s3)
type(s3)

#note a diferença, temos um data frame
d4= dados[['purpose']]
type(d4)

#renomear
dados.rename(columns={"duration":"duração","purpose":"propósito"})

#porém a alteração não é persistida
dados.head(1)

#para persistir
dados.rename(columns={"duration":"duração","purpose":"propósito"},inplace=True)

dados.head(1)

#excluir coluna
dados.drop('checking_status',axis=1,inplace=True)
print(dados)

dados.head(1)

#verificar dados nulos
dados.isnull()

#verificar dados nulos
dados.isnull().sum()

#retirar colunas com NaN
dados.dropna()

#preencher dados faltantes
dados['duração'].fillna(0,inplace = True)

#iloc
dados.iloc[0:3,0:5]

dados.iloc[[0,1,2,3,7],0:5]

