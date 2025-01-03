
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#load your dataset (adjust path if necessary)
data=pd.read_csv("exp4.csv")

#plot 1: count plot for'age' without palette warning 
sns.countplot(x='age', data=data)
plt.title('age ditribution')
plt.show()

#plot 2:countplot for "salary" without palette warning
sns.countplot(x='salary', data=data)
plt.title('salary ditribution')
plt.show()

#plot 3:countplot for "department" without palette warning
sns.countplot(x='department', data=data)
plt.title('department ditribution')
plt.show()

#plot 4:heatmap for numerical columns only (age and salary)
#since 'name' and 'departmrnt' are strings, they are exculded
sns.heatmap(data[['age','salary']].corr(),annot=True,cmap='coolwarm',linewidth=0.5)
plt.title('correlation heatmap')
plt.show()
