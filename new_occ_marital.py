import pandas as pd
df = pd.read_csv('master_dataframe.csv')
df = df.drop(columns=['Unnamed: 0'])
df.rename(columns={'occupation_name_x':'name1', 'occupation_name_y':'name2'}, inplace=True)

most_occs = df['name1'].value_counts()
most_occs1 = df['name2'].value_counts()

most_occs = pd.DataFrame(most_occs)
most_occs1 = pd.DataFrame(most_occs1)
most_occs1.reset_index()
most_occs1.rename(columns={'index':'name', 'name2':'count'}, inplace=True)
most_occs = most_occs.append(most_occs1)


most_occs = most_occs.rename(columns={"occupation_name_x": "count"})
most_occs1 = most_occs1.rename(columns={'occupation_name_y':'count'})
df.sort_values(by='count', ascending=False)
most_occs =most_occs.append(most_occs1)
len(most_occs)
most_occs = most_occs.sort_values(by='count', ascending=False)
most_occs = most_occs.reset_index()
most_occs.columns = ['occupation', 'count']
df
teachers = df[df["name1"].str.contains("teacher")]

teachers = teachers[teachers['sex'] == 1]
teach = teachers[teachers['name2'].str.contains("teacher")]
not_teach = teachers[~teachers["name2"].str.contains("teacher", na=False)]
not_teach
not_male_teach = not_teach.groupby('name2')['count'].sum()


not_male_teach = pd.DataFrame(not_male_teach)
not_male_teach = not_male_teach.sort_values(by='count', ascending=False)
most_occs.head(50)

teachers = df[df["name1"].str.contains("teacher")]
teachers = teachers[teachers['sex'] == 2]



not_teach = teachers[~teachers["name2"].str.contains("teacher", na=False)]

not_female_teach = not_teach.groupby('name2')['count'].sum()

not_female_teach = pd.DataFrame(not_female_teach)
not_female_teach = not_female_teach.sort_values(by='count', ascending=False)

not_female_teach[0:20]
# ax.plot(colormap='PRGn')

not_male_teach = not_male_teach.reset_index()
not_female_teach = not_female_teach.reset_index()
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
new_figure = plt.figure(figsize=(16,4))

ax = new_figure.add_subplot(121)
ax.title.set_text('Male Teachers')

# Generate a line plot on first axes
color = cm.viridis_r(np.linspace(.4,.8, 30))
ax.bar(not_male_teach['name2'][0:20], not_male_teach['count'][0:20], color='blue')
for ax in new_figure.axes:
    plt.sca(ax)
    plt.xticks(rotation=60)
