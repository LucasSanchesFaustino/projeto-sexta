import pandas as pd

#Primeira Parte: Isolando 2020,2021 e 2022. Qual foi cidade e em qual dia, apresentou o maior número de mortes e infecções.
#Segunda parte: isolando a cidade de São Paulo que é a maior do estado, quais foram os municípios que apresentaram o maior número de mortes e infecções, durante os anos de 2020, 2021 e 2022.

df = pd.read_csv("dados_limpos.csv", sep=",");

df['new_confirmed_abs'] = df['new_confirmed'].abs();

df['new_deaths_abs'] = df['new_deaths'].abs(); 

# Converte a data para o padrão datetime64
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Filtrando e separando em três dataframes distintos para cada ano (2020, 2021 e 2022)
df_filtrado2020 = df.loc[(df['date'] >= '2020-01-01') & (df['date'] < '2020-12-31')]
df_filtrado2021 = df.loc[(df['date'] >= '2021-01-01') & (df['date'] < '2021-12-31')]
df_filtrado2022 = df.loc[(df['date'] >= '2022-01-01') & (df['date'] < '2022-12-31')]


# Dia que mais teve mortes em 2020
print("Máximo de mortes confirmadas em 2020")
print(df_filtrado2020.sort_values(by=['new_deaths_abs'], ascending=False));

# Dia que mais teve mortes em 2021
print("Máximo de mortes confirmadas em 2021")
print(df_filtrado2021.sort_values(by=['new_deaths_abs'], ascending=False));

# Dia que mais teve mortes em 2022
print("Máximo de mortes confirmadas em 2022")
print(df_filtrado2022.sort_values(by=['new_deaths_abs'], ascending=False));





# Dia que mais teve infecções confirmadas em 2020
print("Máximo de infecções confirmadas em 2020")
print(df_filtrado2020.sort_values(by=['new_confirmed_abs'], ascending=False));

# Dia que mais teve infecções confirmadas em 2021
print("Máximo de infecções confirmadas em 2021")
print(df_filtrado2021.sort_values(by=['new_confirmed_abs'], ascending=False));

# Dia que mais teve infecções confirmadas em 2022
print("Máximo de infecções confirmadas em 2022")
print(df_filtrado2022.sort_values(by=['new_confirmed_abs'], ascending=False));




# Segunda Parte
df_filtro_sem_sp = df[df['city'] != 'São Paulo'];

print("Mais casos confirmadas, isolando SP")
print(df_filtro_sem_sp.sort_values(by=['new_confirmed_abs'], ascending=False));

print("Mais mortes confirmadas, isolando SP")
print(df_filtro_sem_sp.sort_values(by=['new_deaths_abs'], ascending=False));