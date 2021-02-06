import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv('master.csv')
df2 = df1.fillna(0)
# print(df2.columns)

sns.set_style('darkgrid')
fig, axes = plt.subplots(figsize=(12, 6))
# 1.Country with highest population
df3 = df2.sort_values(by='suicides_no', ascending=False)
# sns.barplot(data=df3, x='population', y='country', palette='CMRmap', ci=None)
# axes.set_xlabel('Country')
# axes.set_ylabel('Population')
# axes.set_title('Top 15 Countries with highest Population', fontsize=15)
# axes.set_ylim([14, 0])

# 2.Country with highest suicide cases
# sns.barplot(data=df3, y='country', x='suicides_no', ci=None, palette='YlOrRd_r')
# axes.set_xlabel('Country')
# axes.set_ylabel('Suicide Cases')
# axes.set_title('Top 15 Countries with highest Suicide Cases', fontsize=15)
# axes.set_ylim([14, 0])

# 3.Country with highest suicide rate
# sns.barplot(data=df3, y='country', x='suicides/100k_pop', ci=None, palette='YlOrRd_r')
# axes.set_xlabel('Country')
# axes.set_title('Top 15 Countries with highest Suicide Rate', fontsize=15)
# axes.set_ylim([14, 0])

# 4.Country with highest HDI
# sns.barplot(data=df3, y='country', x='HDI_for_year', ci=None, palette='nipy_spectral')
# axes.set_xlabel('HDI')
# axes.set_ylabel('Country')
# axes.set_title('Top 15 Countries with highest HDI', fontsize=15)
# axes.set_ylim([14, 0])

# 6.Country with highest gdp for year
# fig1, a = plt.subplots(1, 2, figsize=(12, 6))
# sns.barplot(data=df3, y='country', x='gdp_per_capita', ci=None, palette='tab10')
# axes.set_xlabel('GDP Per Capita')
# axes.set_ylabel('Country')
# axes.set_title('Top 15 Countries with GDP per Capita', fontsize=15)
# axes.set_ylim([14, 0])

# 7.Generation Count
# sns.countplot(data=df3, x='generation', order=df3['generation'].value_counts().index, palette='Purples_r')
# axes.set_xlabel('Generation')
# axes.set_ylabel('Count')
# axes.set_title('Generation Count', fontsize=15)

# 8.Generation with highest gdp per capita
# sns.barplot(data=df3, x='generation', y='gdp_per_capita', palette='coolwarm', ci=None)
# axes.set_xlabel('Generation')
# axes.set_ylabel('GDP Per Capita')
# axes.set_title('Per Capita Income of Every Generation', fontsize=15)

# 9.Generation with highest suicide rate
# sns.barplot(data=df3, x='generation', y='suicides/100k_pop', ci=None, palette='YlOrRd_r')
# axes.set_xlabel('Generation')
# axes.set_ylabel('Suicide Rate')
# axes.set_title('Suicide Rate in every Generation', fontsize=15)

# 10.Year with highest death
# sns.barplot(data=df3, y='suicides_no', x='year', ci=None)
# axes.set_xlabel('Deaths')
# axes.set_ylabel('Year')
# axes.set_title('Year With Highest Deaths', fontsize=15)
# axes.set_ylim()

# 11.Number of deaths in males vs females
# sns.barplot(data=df3, x='sex', y='suicides_no', ci=None, palette='OrRd_r')
# axes.set_xlabel('Sex')
# axes.set_ylabel('Suicide Cases')
# axes.set_title('Number of Deaths in Male Vs Female', fontsize=15)

# 12.Age Vs suicide number
df4 = df2.sort_values('suicides_no', ascending=False).reset_index(drop=True)
axes = sns.barplot(data=df4, x='country', y='suicides_no', ci=None, palette='RdYlGn')
axes.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
# axes.set_xticklabels(df4.country)
for item in axes.get_xticklabels(): item.set_rotation(90)
for i, v in enumerate(df4["suicides_no"].iteritems()):
    axes.text(i, v[1], "{:,}".format(v[1]), color='m', va='bottom', rotation=45)
# plt.tight_layout()
axes.set_xlabel('Age')
axes.set_ylabel('Suicide Cases')
axes.set_title('Number of Deaths in Different Age Groups', fontsize=15)
plt.setp(axes.get_xticklabels(), rotation=45)
axes.set_xlim([0, 9])

# 13.	Age wise death of females
# 14.	Age wise death of males
# g = sns.catplot(data=df3, col='sex', x='age', y='suicides_no', kind='bar', ci=None, height=6, aspect=1, palette='OrRd_r')
# g.set_axis_labels('Age', 'Suicide Number')
# g.set_titles("Gender: {col_name}")
plt.show()
