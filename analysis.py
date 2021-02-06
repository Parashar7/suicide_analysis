import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# feature engineering

df = pd.read_csv('master.csv')
new_df = df.fillna(0)
# print('Age group wise death:\n', new_df.age.value_counts())
# print('Year wise total deaths(Top 5):\n', new_df.year.value_counts().head(5))
# print('Year wise total deaths(Least 5):\n', new_df.year.value_counts().tail(5))

# print(new_df.sex.value_counts())
# fig, axes = plt.subplots(1,2, figsize=(15, 6))
# sns.countplot(data=new_df, y='year', order=new_df['year'].value_counts().index, palette='gist_rainbow', ax=axes[0])


# fig, ax = plt.subplots(figsize=(15, 8))
# dff = (new_df.sort_values(by='suicides_no', ascending=False))
# sns.barplot(data=dff, x='year', y='suicides_no')
# ax.barh(dff['suicides_no'], dff['year'])


# axes.set_ylabel('Year')
# axes.set_xlabel('Death Counts')
# axes.set_ylim([9, 0])
# axes.set_title('Years with top 5 Deaths', fontsize=15)


# fig, axes = plt.subplots(figsize=(15, 6))
# new_df.query("sex=='male'").groupby('year').count()['generation'].sort_values(ascending=True).tail(5).plot(kind='barh')
# sns.lineplot(data=new_df, x='year', y='suicides_no', hue='age', palette='magma_r')
# plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
# axes.set_xlabel('Year')
# axes.set_ylabel('Suicide Number')
# axes.set_title('Year Vs Age Death', fontsize=15)

# sns.countplot(data=new_df, y='generation', order=new_df['generation'].value_counts().index, palette='twilight_shifted_r')
# axes.set_xlabel('Death Count')
# axes.set_ylabel('Generation')
# axes.set_title('Generation Wise Death', fontsize=15)

# print(new_df.country_year.value_counts())
# g = sns.relplot(data=new_df, x='year', y='suicides/100k pop', palette='rocket_r', col='sex', kind='line', hue='generation')
# g.set_axis_labels('Year', 'Suicide Rate')
# g.set_titles('Sex:{col_name}')
# plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)

# sns.barplot(data=new_df, x='generation', y='gdp_per_capita', ax=axes[0], palette='viridis')
# axes[0].set_xlabel('Generation')
# axes[0].set_ylabel('GDP Per Capita')
# axes[0].set_title('Income of Generation')
# sns.barplot(data=new_df, x='generation', y='suicides/100k pop', ax=axes[1], palette='inferno_r')
# axes[1].set_xlabel('Generation')
# axes[1].set_ylabel('Suicide Rate')
# axes[1].set_title('Suicide Rate of Generation')

# s=sns.countplot(data=new_df, y='country', order=new_df['country'].value_counts().index, palette='RdBu')
# s.set_ylabel('Country')
# s.set_xlabel('Death Counts')
# axes.set_ylim([15, 0])
# s.set_title('Country with top 10 Deaths', fontsize=15)

# g = sns.barplot(data=new_df, x='country', y='HDI_for_year', order=df.sort_values('HDI_for_year', ascending=True).country)
# g.set_xlim([9, 0])
# plt.savefig("relpolt.png", dpi=100)

# g = sns.barplot(data=new_df, y='country', x='HDI_for_year' )
# sort_df = new_df.HDI_for_year.sort_values(ascending=True)

# sorted_df = new_df.sort_values(by='population', ascending=False).head(10)

# g = sns.barplot(data=new_df, x='suicides/100k pop', y='country')
# g.set_ylim([14, 0])
# print(new_df.gdp_per_capita)

# sns.barplot(data=new_df, x='suicides_no', y='country', ax=axes[0])
# axes[0].set_ylim([9, 0])
# sns.countplot(data=new_df, y='country', ax=axes[1], order=new_df.country.value_counts().index)
# axes[1].set_ylim([9, 0])

# dff = (new_df.sort_values(by='suicides/100k_pop', ascending=False).head(20))

# print(dff['suicides/100k_pop'])
# fig, ax = plt.subplots(figsize=(15, 8))
# ax.barh(dff['suicides/100k_pop'], dff['country'])
# sns.barplot(data=dff, x='suicides/100k_pop', y='country')

# print(new_df.sort_values(by='suicides/100k_pop', ascending=False).head(10))
# print(new_df.query("country=='Aruba'"))

# sns.barplot(data=new_df, x='suicides_no', y='year', ax=axes[1])

# sns.set_style('darkgrid')
# fig, g = plt.subplots(figsize=(12, 6))

# g = sns.countplot(data=new_df.query("generation=='Generation X'"), y='country',
#  order=new_df['country'].value_counts().index)
# g.set_ylim([21, 0])
# g.set_ylabel('Country')
# g.set_xlabel('Generation X')
# g.set_title('Countries with most number of Generation X people', fontsize=15)


# df2 = new_df.value_counts().sort_values(ascending=True)
# print(new_df.value_counts().head(5))

# df_zip = pd.DataFrame(df['country'].value_counts().sort_values(by='population', ascending=True).head(5))
# df_zip.rename(columns={'country': 'Top 5'}, inplace=True)
# df2 = new_df.sort_values(by='population', ascending=True)
# print(df2.country.value_counts())

comp_df = new_df[['country', 'population']].value_counts().sort_values(ascending=False)
group = new_df.groupby('country')
group_data = group[['population']]
print(comp_df)

plt.show()
