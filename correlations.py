# Analysis of correlations between variables and identification of key factors influencing banking subscription
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('banking_data_cleaned.csv')

main_columns = [
    'age', 'job', 'marital', 'education', 'default', 'balance',
    'housing', 'loan', 'contact', 'day', 'duration',
    'campaign', 'pdays', 'previous', 'poutcome', 'y'
]

df_main = df[main_columns]
df_encoded = pd.get_dummies(df_main)
correlation_matrix = df_encoded.corr()

plt.figure(figsize=(20, 16))  
sns.heatmap(correlation_matrix, 
            annot=True,  
            cmap='coolwarm',  
            center=0,  
            fmt='.2f')  

plt.title('Correlation Matrix of Main Variables')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.tight_layout()
plt.show()

# Visualization of the 10 variables most correlated with y
correlations_y = correlation_matrix['y'].sort_values(ascending=False)
plt.figure(figsize=(12, 6))
correlations_y[1:11].plot(kind='bar')  
plt.title('Top 10 Variables Most Correlated with Subscription')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
