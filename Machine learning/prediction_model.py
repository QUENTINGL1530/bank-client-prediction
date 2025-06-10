from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv('data/banking_data_cleaned.csv')
X = df.drop('y', axis=1)
y = df['y']

X_encoded = pd.get_dummies(X, drop_first=True)
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = LogisticRegression()
model.fit(X_train_scaled, y_train)


y_pred = model.predict(X_test_scaled)


plt.figure(figsize=(10, 6))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Résultats du Modèle de Prédiction')
plt.xlabel('Prédictions')
plt.ylabel('Valeurs Réelles')
plt.xticks([0.5, 1.5], ['Non-souscription', 'Souscription'])
plt.yticks([0.5, 1.5], ['Non-souscription', 'Souscription'])

plt.tight_layout()
plt.savefig('results/resultats_simple.png')
plt.close()

print("\nRésultats du modèle :")
print(classification_report(y_test, y_pred))