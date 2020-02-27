import pandas as pd
# read csv file
df = pd.read_csv('usa_000002.csv.gz')
codes = pd.read_csv('occupation_code - Sheet1 (1).csv')
# rename columns for code csv file
codes.rename(columns={'2010 Census Occupation Code': 'code', 'Unnamed: 1':'occ'}, inplace=True)
# there are 552 different occupations.

# only include necessary columns
df = df[['sec', 'occ', 'sex_sp', 'occ_sp']]
# drop NaN values
df.dropna(inplace=True)
# drop 0 values
df = df[(df != 0).all(1)]
# drop mirror duplicates
df = df.iloc[::2]
df['occ'] = df['occ'].astype('int')
df['occ_sp'] = df['occ_sp'].astype('int')

value_counts2 = pd.DataFrame(df['occ_sp'].value_counts())
value_counts2.reset_index(inplace=True)
value_counts = pd.DataFrame(df['occ'].value_counts())



value_counts.reset_index(inplace=True)

df = pd.merge(left=value_counts2,right=codes, left_on='index', right_on='code')
first_occ_count = df
second_occ_count = df

second_occ_count = second_occ_count[['occ', 'occ_sp']]
second_occ_count
first_occ_count = first_occ_count[['occ_y', 'occ_x']]

first_occ_count

merged_occ_count = pd.merge(left=first_occ_count,right=second_occ_count, left_on='occ_y', right_on='occ')
merged_occ_count = merged_occ_count[['occ', 'occ_sp', 'occ_x']]
sum_col = merged_occ_count['occ_sp'] + merged_occ_count['occ_x']

merged_occ_count['sum'] = sum_col
merged_occ_count = merged_occ_count.sort_values(by=['sum'], ascending=False)
merged_occ_count = merged_occ_count[['occ', 'sum']]
merged_occ_count.head(50)



# merge code dataframe with occupation dataframe
#df1 = pd.merge(df,codes,how = 'inner', left_on='occ', right_on='code')
pd.set_option('display.max_rows', 479)

both = pd.concat([df_count, merged_count], axis=1)

df.rename(columns={'sec':'sex', 'occ':'occupation', 'sex_sp':'sex_of_spouse', 'occ_sp':'occupation_of_spouse'}, inplace=True)


df = pd.merge(left=df,right=codes, left_on='occ_sp', right_on='code')
df

# count how many people in each profession for both cols
occ_x_count = data1['occ'].value_counts()

occ_y_count = data['occ_y'].value_counts()
# convert count to DataFrame
occ_x_count = pd.DataFrame(occ_x_count)

occ_y_count=  pd.DataFrame(occ_y_count)

# sort
