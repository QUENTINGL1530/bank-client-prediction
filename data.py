import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data and clean it
print("Chargement du fichier Excel...")
df = pd.read_excel("Banking_Call_Data.xlsx", engine='openpyxl')

print("Nettoyage des données...")
df.replace("unknown", np.nan, inplace=True)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Conversion de la colonne y en numérique (yes=1, no=0)
print("Conversion des valeurs de la colonne y...")
df['y'] = df['y'].map({'yes': 1, 'no': 0})

print("Création des tranches d'âge...")
bins = [0, 20, 30, 40, 50, 60, 100]
labels = ['<20', '20-30', '30-40', '40-50', '50-60', '60+']
df['tranche_age'] = pd.cut(df['age'], bins=bins, labels=labels)

# display the dataset information
print("\n=== Informations sur le dataset ===")
print(f"\nNombre de lignes et colonnes : {df.shape}")
print("\nListe des colonnes :")
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")
print("\nAperçu des données :")
print(df.head())

# calculate the conversion ratio by age
print("\n=== Ratios de conversion par tranche d'âge ===")
conversion_par_age = df.groupby('tranche_age').agg({
    'y': ['count', 'sum']
}).round(2)
conversion_par_age.columns = ['Nombre total', 'Nombre de oui']
conversion_par_age['Ratio de conversion'] = (conversion_par_age['Nombre de oui'] / conversion_par_age['Nombre total'] * 100).round(2)
print(conversion_par_age)

# Visualisation of the conversion ratio
plt.figure(figsize=(12, 6))
conversion_par_age['Ratio de conversion'].plot(kind='bar')
plt.title('Ratio de conversion par tranche d\'âge')
plt.xlabel('Tranche d\'âge')
plt.ylabel('Ratio de conversion (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


