import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('master.csv')
df2 = df.fillna(0)
df3 = df2.sort_values(by='suicides_no', ascending=False)
sns.set_style('darkgrid')
fig, g = plt.subplots(figsize=(13, 6))


#For Verticle Graphs
# splot = sns.barplot(data=df3, x='age', y='suicides_no', ci=None, palette='RdYlGn')
# for p in splot.patches:
#   splot.annotate(format(p.get_height(), '.1f'),
#                 (p.get_x() + p.get_width() / 2., p.get_height()),
#                 ha='center', va='top',
#                xytext=(0, 12), size=15,
#                textcoords='offset points')
# splot.set_xlabel('Age')
# splot.set_ylabel('Suicide Cases')
# splot.set_title('Number of Deaths in Different Age Groups', fontsize=15)

#For Horizontal graphs
splot = sns.barplot(data=df3, y='age', x='suicides_no', ci=None, palette='RdYlGn')
for p in splot.patches:
    width = p.get_width()
    plt.text(2 + p.get_width(), p.get_y() + 0.55 * p.get_height(),
             '{:1.0f}'.format(width),
             ha='left', va='center', size=11)
splot.set_xlabel('Age')
splot.set_ylabel('Suicide Cases')
splot.set_title('Number of Deaths in Different Age Groups', fontsize=15)


plt.show()
