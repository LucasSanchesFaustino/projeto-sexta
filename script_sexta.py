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
# db.to_csv(r'C:\Users\lucas\Desktop\trabalho-sexta\dados_isolados.csv', index=False);

db1 = db.drop(['city_ibge_code', 'state', 'estimated_population_2019', 'epidemiological_week', 'last_available_confirmed_per_100k_inhabitants', 'order_for_place', 'last_available_deaths' , 'last_available_confirmed', 'is_last', 'is_repeated'], axis=1, inplace=True);  
print(db1);
print("---------------\n\n\n\n");

db1 = db[db['place_type'] == 'city']
print(db1);
print("---------------\n\n\n\n");

db_prelimpo = db1.drop(['place_type'], axis=1)

# db1.to_csv(r'C:\Users\lucas\Desktop\trabalho-sexta\dados_nulos_mas_limpos.csv', index=False);

# Remove qualquer linha que possua valores nulos, independente de qual valor esteja nulo.
db_limpo = db_prelimpo.dropna(axis=0, how='any');

#db1 = db1.fillna(db1.mean())

#db1 = db1.Amount.abs();
#print(db1)

# Exportando .csv de controle
db_limpo.to_csv(r'C:\Users\Lucas Faustino\Desktop\projeto_sexta\projeto-sexta\dados_limpos.csv', index=False);

