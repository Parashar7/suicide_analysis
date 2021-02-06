import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('master.csv')
df2 = df.fillna(0)
df3 = df2.sort_values(by='suicides_no', ascending=False)
sns.set_style('darkgrid')
fig, g = plt.subplots(figsize=(13, 6))

g = sns.lineplot(data=df2, x='year', y='suicides_no', markers=True, dashes=False, hue='sex', palette='Reds_r',
                 style='sex')
g.set_xlabel('Year')
g.set_ylabel('Deaths')
g.set_title('Suicide Trend')
#g.annotate('trying to annotate',
 #          xy=(1987, 550), xytext=(70, -190),
  #         xycoords='data',
   #        bbox=dict(boxstyle='round', fc='0.8'),  # New param
    #       ha='center',
     #      va='center',
       #    arrowprops={},
      #     textcoords='offset points'
        #   )
plt.show()
