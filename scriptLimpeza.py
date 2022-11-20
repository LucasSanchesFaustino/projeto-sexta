from typing import Any
import pandas as pd

imported = pd.read_csv("caso_full.csv", sep=',');

# print("---------------\n\n\n\n");
# print(imported);

#Isolando apenas para o Estado de SP
db = imported[imported['state'] == 'SP'];

# print("---------------\n\n\n\n");
# print(db);

# Exportando .csv de controle
# db.to_csv(r'dados_isolados.csv', index=False);

db.drop(['city_ibge_code', 'last_available_death_rate', 'state', 'estimated_population_2019', 'epidemiological_week', 'last_available_confirmed_per_100k_inhabitants', 'order_for_place', 'last_available_deaths' , 'last_available_confirmed', 'is_last', 'is_repeated'], axis=1, inplace=True);  
print(db);
print("---------------\n\n\n\n");

# Criando dois dataframes para isolar e separar dados de reports de municípios e estados.
db1 = db.loc[(db['place_type'] == 'city') & (db['date'] < '2021-12-12')];
db = db.loc[(db['place_type'] == 'state') & (db['date'] > '2021-12-12')];

print("\n\nDataframe filtrado apenas com reports de cidades");
print(db1);
print("\n\nDataframe filtrado apenas com reports de estados");
print(db);

# Limpa todos os registros que contenham algum valor nulo.
db1.dropna(axis=1, how='any');

# Criando objeto que contém os dois dataframes.
dataframes = [db1, db];

# Concatenando os dataframes.
db_isolado = pd.concat(dataframes);
# db_isolado.drop(['place_type']);

print("\n\nDataframe isolado e concatenado, pronto para a limpeza:");
print(db_isolado);

# db1.to_csv(r'dados_nulos_mas_limpos.csv', index=False);

# Remove qualquer linha que possua valores nulos, independente de qual valor esteja nulo.
# db_isolado.dropna(axis=1, how='any');

# db1 = db1.fillna(db1.mean());

# Converte todos os valores númericos para seus valor absoluto, eliminando quaisquer dados negativos.

db_isolado['new_confirmed'] = db_isolado['new_confirmed'].abs();

db_isolado['new_deaths'] = db_isolado['new_deaths'].abs(); 

#print(db1)

# Exportando .csv do dataframe limpo
db_isolado.to_csv(r'dadosLimpos.csv', index=False);

