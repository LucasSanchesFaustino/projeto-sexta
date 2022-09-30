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

db1 = db.drop(['city_ibge_code', 'state', 'estimated_population_2019', 'epidemiological_week'], axis=1, inplace=True);
print(db1);
print("---------------\n\n\n\n");

db1 = db[db['place_type'] == 'city']
print(db1);
print("---------------\n\n\n\n");

# db1.to_csv(r'C:\Users\lucas\Desktop\trabalho-sexta\dados_nulos_mas_limpos.csv', index=False);

# Remove qualquer linha que possua valores nulos, independente de qual valor esteja nulo.
db1.dropna(axis=0, how='any', inplace=True);

db1 = db1.Amount.abs();
print(db1)

# Exportando .csv de controle
db1.to_csv(r'C:\Users\lucas\Desktop\proj-sexta\dados_limpos.csv', index=False);

