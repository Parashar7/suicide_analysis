import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('master.csv')
new_df = df.fillna(0)
# print(new_df.generation.unique())
# fig, axes = plt.subplots(figsize=(14, 10))
# df3 = new_df.sort_values(by='suicides_no', ascending=False)
# sns.barplot(data=df3, y='country', x='suicides_no', ci=None, palette='YlOrRd_r')
# axes.set_xlabel('Country')
# axes.set_ylabel('Suicide Cases')
# axes.set_title('Top 15 Countries with highest Suicide Cases', fontsize=15)
# axes.set_ylim([14, 0])
# Matplotlib
# plt.figure(figsize=(12,6))
# df_sorted = df.sort_values('suicides_no', ascending=False)
# g=plt.bar('country', 'suicides_no', data=df_sorted)
# plt.xticks(rotation=45)
# g.invert_xaxis()
# plt.xlim((9, 0))


# Seaborn
# fig, axes = plt.subplots(figsize=(14, 10))
# df3 = new_df.sort_values(by='suicides_no', ascending=False)
# axes = sns.barplot(data=df3, y='suicides_no', x='country', ci=None, palette='YlOrRd_r')
# for p in axes.patches:
#    axes.annotate(format(p.get_height(), '.1f'),
#                  (p.get_x() + p.get_width() / 2., p.get_height()),
#                  ha='center', va='top',
#                  xytext=(0, 12), size=15,
#                  textcoords='offset points')
# axes.set_xlabel('Country')
# axes.set_ylabel('Suicide Cases')
# axes.set_title('Top 15 Countries with highest Suicide Cases', fontsize=15)
# axes.set_xlim([9, 0])
# plt.setp(axes.get_xticklabels(), rotation=45)

plt.figure(figsize=(12, 6))
# df_sorted = new_df.sort_values('gdp_per_capita', ascending=False)
# g = plt.bar('country', 'gdp_per_capita', data=df_sorted, color='green')
# plt.xticks(rotation=45)
# plt.xlim((0, 9))
# plt.show()

# seaborn
order = new_df.sort_values(by='gdp_per_capita', ascending=False)
s = sns.barplot(data=order, x='country', y='gdp_per_capita',
                ci=None)
for p in s.patches:
    s.annotate(format(p.get_height(), '.1f'),
               (p.get_x() + p.get_width() / 2., p.get_height()),
               ha='center', va='top',
               xytext=(0, 10), size=9,
               textcoords='offset points')
s.set_xlim([9, 0])
plt.show()
