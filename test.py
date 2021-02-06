import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

education=["Bachelor's", "Less than Bachelor's","Master's","PhD","Professional"]
salary = [110000,105000,126000,144200,95967]
df = pd.DataFrame({"Education":education,
                  "Salary":salary})

print(df)

plt.figure(figsize=(10,6))
# make barplot
sns.barplot(x='Education', y="Salary", data=df, order=df.sort_values('Salary').Education)
# set labels
plt.xlabel("Education", size=15)
plt.ylabel("Salary in US Dollars", size=15)
plt.title("Bar plot with Seaborn", size=18)
plt.tight_layout()
plt.savefig("barplot_Seaborn_Python.png", dpi=100)
plt.show()