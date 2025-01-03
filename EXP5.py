import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("exp4.csv")

#plot1:
sns.countplot(x='Age', data = data)
plt.title('Age Description')
plt.show()

#plot2:
sns.countplot(x='Salary', data = data)
plt.title('Salary Description')
plt.show()

#plot3:
sns.countplot(x='Department', data = data)
plt.title('Department Description')
plt.show()

#plot4:
sns.heatmap(data[['Age','Salary']].corr(),annot=True, cmap='coolwarm',linewidth=0.5)
plt.title('Correection Heatmap')
plt.show()