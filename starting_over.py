import pandas as pd
df = pd.read_csv('cat1.csv')

tuples = df['CODE'][0].split('-')
int(tuples[0])
list_1 = []
list_2 = []
for i in range(len(df['CODE'])):
    tuples = df['CODE'][i].split('-')
    list_1.append(int(tuples[0]))
    list_2.append(int(tuples[1]))


df1 = pd.DataFrame(list_1, list_2)
df1 = df1.reset_index()
df1.columns = ['code1', 'code2']
df1 = df1[['code2', 'code1']]
ranges = df1
ranges['category'] = list(range(1,25))
ranges['code2'][1]
df = pd.read_csv('usa_000002.csv.gz')
df = df[['sec', 'occ', 'sex_sp', 'occ_sp']]

df.rename(columns={'sec':'sex', 'occ':'occupation', 'sex_sp':'sex_of_spouse', 'occ_sp':'occupation_of_spouse'}, inplace=True)
df.dropna(inplace=True)



df = df.iloc[::2]


list_ranges = []
for i in range(len(ranges)):
    range_tuple = (ranges['code2'][i], ranges['code1'][i])
    list_ranges.append(range_tuple)


bins = pd.IntervalIndex.from_tuples(list_ranges, closed='both')

x = pd.cut(list(df['occupation']), bins, include_lowest=True)
x.categories = list(range(1,25))
df['bins_spouse'] = x

y = pd.cut(list(df['occupation_of_spouse']), bins, include_lowest=True)
y.categories = list(range(1,25))
df['bins_spouse'] = y


df


df.dropna(inplace=True)
