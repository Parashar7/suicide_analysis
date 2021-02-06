import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv('master.csv')
df2 = df1.fillna(0)
plt.figure(figsize=(12, 6))
heat = pd.pivot_table(df2, values='suicides_no', index=['age'], columns=['year'],
                      fill_value=0,
                      margins=True)

# named_index = [[calendar.month_abbr[i] if isinstance(i, int) else i for i in list(heat.index)]]
# all_month_year_df = heat.set_index(named_index)
ax = sns.heatmap(heat, cmap='RdYlGn_r')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=10)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, fontsize=10)
plt.title('Average Opening', fontsize=20, pad=20)
# print(heat)
plt.show()
