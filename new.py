import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv('master.csv')
df2 = df1.fillna(0)
explode1 = (0, 0.1, 0, 0, 0, 0)
g = df2['generation'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
g.set(xlabel='', ylabel='')
plt.title('Startangle = 90$^\circ$')
plt.show()
