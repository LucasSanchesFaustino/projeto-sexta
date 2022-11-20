import pandas as pd
import matplotlib.pyplot as plt
import datetime as datetime
import numpy as np
import matplotlib.dates as mdates

#Primeira Parte: Isolando 2020,2021 e 2022. Qual foi cidade e em qual dia, apresentou o maior número de mortes e infecções.
#Segunda parte: isolando a cidade de São Paulo que é a maior do estado, quais foram os municípios que apresentaram o maior número de mortes e infecções, durante os anos de 2020, 2021 e 2022.

df = pd.read_csv("dadosLimpos.csv", sep=",");


# Converte a data para o padrão datetime64
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

print(df['date']);

dfPorMes = df[['new_confirmed', 'date']];
print(dfPorMes['new_confirmed'])

fig, axes = plt.subplots(nrows=1, ncols=1, figsize = (10,10));

axes.xaxis.set_major_locator(mdates.MonthLocator())
axes.xaxis.set_major_formatter(mdates.DateFormatter('%m/%y'))
axes.xaxis.set_label_text("Mês/Ano")

axes.yaxis.set_label_text("Casos confirmados")

dfTeste = dfPorMes.groupby(pd.Grouper(key='date', freq='M'), ).sum()
dfTeste.to_csv("dfTeste.csv", sep=',')

plt.plot(dfTeste);
plt.yticks(np.arange(0, 500000, 50000))
import pandas as pd
import matplotlib.pyplot as plt
import datetime as datetime
import numpy as np
import matplotlib.dates as mdates

#Primeira Parte: Isolando 2020,2021 e 2022. Qual foi cidade e em qual dia, apresentou o maior número de mortes e infecções.
#Segunda parte: isolando a cidade de São Paulo que é a maior do estado, quais foram os municípios que apresentaram o maior número de mortes e infecções, durante os anos de 2020, 2021 e 2022.

df = pd.read_csv("dadosLimpos.csv", sep=",");


# Converte a data para o padrão datetime64
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

print(df['date']);

dfPorMes = df[['new_confirmed', 'date']];
print(dfPorMes['new_confirmed'])

fig, axes = plt.subplots(nrows=1, ncols=1, figsize = (10,10));

axes.xaxis.set_major_locator(mdates.MonthLocator())
axes.xaxis.set_major_formatter(mdates.DateFormatter('%m/%y'))
axes.xaxis.set_label_text("Mês/Ano")

axes.yaxis.set_label_text("Casos confirmados")

dfTeste = dfPorMes.groupby(pd.Grouper(key='date', freq='M'), ).sum()
# dfTeste.to_csv("dfTeste.csv", sep=',')

plt.plot(dfTeste);
plt.yticks(np.arange(0, 500000, 50000))

plt.show()