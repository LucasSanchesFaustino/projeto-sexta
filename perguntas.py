from numpy import column_stack
import pandas as pd


df = pd.read_csv("dadosLimpos.csv", sep=",");

# Total de colunas
print(df.columns);

quantidadeColunas = df.shape;

# Total de linhas
print("\n Total de linhas e colunas: " + str(quantidadeColunas));

# Converte a data para o padrão datetime64
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

print("Em qual cidade e dia ocorreu mais mortes confirmadas no ano de 2020") 
print(df.loc[(df['date'] >= '2020-01-01') & (df['date'] < '2020-12-31') & (df['city'] != '')].sort_values(by=['new_deaths'], ascending=False));

print("Em qual cidade e dia ocorreu mais mortes confirmadas do dia 01-01-2021 até 27-03-2022")
print(df.loc[(df['date'] >= '2021-01-01') & (df['date'] < '2022-03-27')].sort_values(by=['new_deaths'], ascending=False));

print("Máximo de infecções confirmadas em um dia, no ano de 2020")
print(df.loc[(df['date'] >= '2020-01-01') & (df['date'] < '2020-12-31')].sort_values(by=['new_confirmed'], ascending=False));

print("Máximo de infecções confirmadas em um dia, no ano de 2021 e 2022")
print(df.loc[(df['date'] >= '2021-01-01') & (df['date'] < '2022-03-27')].sort_values(by=['new_confirmed'], ascending=False));


