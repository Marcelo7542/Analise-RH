import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings('ignore')

BaseDados = pd.read_csv("Salary_Data.csv")

#print(BaseDados.head())
#print(BaseDados.isnull().sum())
#print(BaseDados.describe())

plt.figure(figsize=(13,5))
plt.suptitle('Densidade')

plt.subplot(1, 2, 1)
sns.kdeplot( BaseDados['Salary'], color="black")
plt.title("Análise de renda")
plt.xlabel("Salário")
plt.ylabel("Densidade")

plt.subplot(1, 2, 2)
sns.kdeplot( BaseDados['YearsExperience'], color="black")
plt.title("Análise de experiência")
plt.xlabel("Experiência")
plt.ylabel("Densidade")

plt.show()