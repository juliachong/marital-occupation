import pandas as pd

df = pd.read_csv("master_dataframe.csv").drop(columns=["Unnamed: 0"], errors="ignore")
df = df.rename(columns={"occupation_name_x": "name1", "occupation_name_y": "name2"})

# --- combined occupation counts 
most_occs = (
    pd.concat([df["name1"], df["name2"]], ignore_index=True)
      .value_counts(dropna=False)
      .rename_axis("occupation")
      .reset_index(name="count")
      .sort_values("count", ascending=False)
)

# teachers by gender

# MALE (sex == 1): teacher -> NOT teacher in name2
male_teachers = teachers[teachers["sex"] == 1]
not_male_teach = (
    male_teachers[~male_teachers["name2"].str.contains("teacher", case=False, na=False)]
      .groupby("name2", dropna=False)["count"]
      .sum()
      .reset_index()
      .sort_values("count", ascending=False)
)

# FEMALE (sex == 2): teacher -> NOT teacher in name2
female_teachers = teachers[teachers["sex"] == 2]
not_female_teach = (
    female_teachers[~female_teachers["name2"].str.contains("teacher", case=False, na=False)]
      .groupby("name2", dropna=False)["count"]
      .sum()
      .reset_index()
      .sort_values("count", ascending=False)
)

top50_occs = most_occs.head(50)
top20_not_male = not_male_teach.head(20)
top20_not_female = not_female_teach.head(20)
