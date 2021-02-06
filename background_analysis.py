import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv('master.csv')
fig, axes = plt.subplots(figsize=(14, 10))
df2 = df1.sort_values(by='population', ascending=False)
s=sns.barplot(data=df2, x='population', y='country', palette='CMRmap', ci=None)
for p in s.patches:
    width = p.get_width()
    plt.text(5 + p.get_width(), p.get_y() + 0.55 * p.get_height(),
             '{:1.0f}'.format(width),
             ha='left', va='center', size=11)
s.set_xlabel('Country')
s.set_ylabel('Population')
s.set_title('Top 15 Countries with highest Population', fontsize=15)
s.set_ylim([9, 0])
plt.show()