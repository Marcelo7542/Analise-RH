import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings('ignore')

BaseDados = pd.read_csv("Salary_Data.csv")
BaseDados.rename(columns={
    "YearsExperience": "Experiência",
    "Salary": "Salário"
}, inplace=True)

Correlação = BaseDados.corr()

plt.figure(figsize=(13,5))
plt.suptitle("Correlação")

plt.subplot(1,2,1)
sns.heatmap(Correlação, annot=True)
plt.xlabel("Salário")

plt.subplot(1,2,2)
sns.regplot(x=BaseDados['Salário'], y=BaseDados['Experiência'])


plt.show()