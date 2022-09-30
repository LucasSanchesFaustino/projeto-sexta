import pandas as pd

#Primeira Parte: Isolando 2020,2021 e 2022. Qual foi cidade e em qual dia, apresentou o maior número de mortes e infecções.
#Segunda parte: isolando a cidade de São Paulo que é a maior do estado, quais foram os municípios que apresentaram o maior número de mortes e infecções, durante os anos de 2020, 2021 e 2022.

df = pd.read_csv("dados_limpos.csv", sep=",");

df['new_confirmed_abs'] = df['new_confirmed'].abs();

df['new_deaths_abs'] = df['new_deaths'].abs(); 

# Converte a data para o padrão datetime64
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

print("Em qual cidade e dia ocorreu mais mortes confirmadas em 2020")
print(df.loc[(df['date'] >= '2020-01-01') & (df['date'] < '2020-12-31')].sort_values(by=['new_deaths_abs'], ascending=False));

print("Em qual cidade e dia ocorreu mais mortes confirmadas em 2021")
print(df.loc[(df['date'] >= '2021-01-01') & (df['date'] < '2021-12-31')].sort_values(by=['new_deaths_abs'], ascending=False));

print("Em qual cidade e dia ocorreu mais mortes confirmadas em 2022")
print(df.loc[(df['date'] >= '2021-01-01') & (df['date'] < '2021-12-31')].sort_values(by=['new_deaths_abs'], ascending=False));


print("Máximo de infecções confirmadas em um dia, no ano de 2020")
print(df.loc[(df['date'] >= '2020-01-01') & (df['date'] < '2020-12-31')].sort_values(by=['new_confirmed_abs'], ascending=False));

print("Máximo de infecções confirmadas em um dia, no ano de 2021")
print(df.loc[(df['date'] >= '2021-01-01') & (df['date'] < '2021-12-31')].sort_values(by=['new_confirmed_abs'], ascending=False));

print("Máximo de infecções confirmadas em um dia, no ano de 2022")
print(df.loc[(df['date'] >= '2022-01-01') & (df['date'] < '2022-12-31')].sort_values(by=['new_confirmed_abs'], ascending=False));


print("Mais casos confirmados em todos os anos, isolando cidades com mais de 100 mil habitantes")
print(df.loc[(df['date'] >= '2022-01-01') & (df['date'] < '2022-12-31') & (df['estimated_population'] < 250000)].sort_values(by=['new_confirmed_abs'], ascending=False));

print("Mais mortes confirmadas em todos os anos, isolando cidades com mais de 100 mil habitantes")
print(df.loc[(df['date'] >= '2022-01-01') & (df['date'] < '2022-12-31') & (df['estimated_population'] < 250000)].sort_values(by=['new_deaths_abs'], ascending=False));