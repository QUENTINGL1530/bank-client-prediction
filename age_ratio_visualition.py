import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Banking_Call_Data.xlsx", engine='openpyxl')
df.replace("unknown", np.nan, inplace=True)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

print("Converting y column values...")
df['y'] = df['y'].map({'yes': 1, 'no': 0})

bins = [0, 20, 30, 40, 50, 60, 100]
labels = ['<20', '20-30', '30-40', '40-50', '50-60', '60+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

df.to_csv("banking_data_cleaned.csv", index=False)

print("\n=== Dataset Information ===")
print(f"\nNumber of rows and columns: {df.shape}")
print("\nColumn list:")
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")
print("\nData preview:")
print(df.head())


print("\n=== Conversion Ratios by Age Group ===")
conversion_by_age = df.groupby('age_group').agg({
    'y': ['count', 'sum']
}).round(2)
conversion_by_age.columns = ['Total count', 'Yes count']
conversion_by_age['Conversion ratio'] = (conversion_by_age['Yes count'] / conversion_by_age['Total count'] * 100).round(2)
print(conversion_by_age)

plt.figure(figsize=(12, 6))
conversion_by_age['Conversion ratio'].plot(kind='bar')
plt.title('Conversion Ratio by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Conversion Ratio (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


