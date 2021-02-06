import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('master.csv')
df2 = df.fillna(0)
df3 = df2.sort_values(by='suicides_no', ascending=False)
sns.set_style('darkgrid')
fig, g = plt.subplots(figsize=(13, 6))

g = sns.lineplot(data=df2, x='year', y='suicides_no', hue='sex', palette='Reds_r')
g.set_xlabel('Year')
g.set_ylabel('Deaths')
g.set_title('Suicide Trend')
# print(df2.year.unique())
plt.setp(g.get_xticklabels(), rotation=45)
# g.set_xticks([1987, 1988, 1989, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002
#              , 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 1985, 1986, 1990, 1991, 2012, 2013
#             , 2014, 2015, 2011, 2016])

g.set_xticks(np.arange(1985, 2016 + 1, 1))
# L = plt.legend()
# L.get_texts()[0].set_text('Male')
# plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.,)
# L = plt.legend()
# L.get_texts()[0].set_text('Male')
# plt.legend(['Male', 'Female'])
plt.legend(['Male', 'Female'], bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0, fontsize='large', shadow=False,
           facecolor='white')
# g.annotate('trying to annotate',
#          xy=(1987, 600),
#         xycoords='data',
#      bbox=dict(boxstyle='round', fc='0.8'),  # New param
#      ha='center',
#     va='center')
plt.show()
