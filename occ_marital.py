import pandas as pd

og = og.dropna()

og














# Import and clean two datasets
og = pd.read_csv('usa_000002.csv.gz')
code = pd.read_csv('occupation_code - Sheet1 (1).csv')
code.columns = ['occ', 'occupation']
og = og[['hhwt', 'sec', 'occ', 'sex_sp', 'occ_sp']]
code.rename(columns={'occ':'occupation_code', 'occupation': 'occupation_name'}, inplace=True)
og.rename(columns={'hhwt':'households', 'sec':'sex', 'occ':'occupation', 'sex_sp':'sex_of_spouse', 'occ_sp':'occupation_of_spouse'}, inplace=True)
og = og[['households']]

df = pd.merge(left=df,right=code, left_on='occupation_of_spouse', right_on='occupation_code')
import numpy as np

df = df[['sex', 'occupation_name_x', 'sex_of_spouse', 'occupation_name_y', 'count']]
df = df.join(og)
df = df[['households', 'sex', 'occupation_name_x', 'sex_of_spouse', 'occupation_name_y', 'count']]

df.to_csv('master_dataframe.csv')


df = df[['households', 'sex', 'occupation', 'occupation_name_x', 'sex_of_spouse', 'occupation_of_spouse', 'occupation_name_y']]
df.rename(columns={'occupation_name_x':'occupation1', 'occupation_name_y':'occupation2'}, inplace=True)
df = df.groupby(['occupation','occupation_of_spouse', 'sex', 'sex_of_spouse']).size().reset_index().rename(columns={0:'count'})
df = df.sort_values(by='count', ascending=False)
df = df[~df[['occupation', 'occupation_of_spouse']].apply(frozenset, axis=1).duplicated()]


df_occ = list(df2['occupation1'])
df2 = df2[df2['occupation']!=9920]

df = df[['sex', 'occupation', 'occupation1', 'sex_of_spouse', 'occupation_of_spouse']]

df = df.groupby(['occupation','occupation_of_spouse']).size().reset_index().rename(columns={0:'count'})



prof = pd.read_csv('profession-profiles.csv')


prof_list = list(prof['Profession'])



from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import utils
from . import fuzz
from . import utils
from utils import *
import heapq
import logging
from functools import partial
default_scorer = fuzz.WRatio
default_processor = fuzz.utils.full_process
myset = set(df_occ)
myset = list(myset)

myset


import pyperclip

 ESTJ = pyperclip.paste()
 ISTJ = pyperclip.paste()
 ESFJ = pyperclip.paste()
 ISFJ = pyperclip.paste()
 ESTP = pyperclip.paste()
 ISTP = pyperclip.paste()
 ESFP = pyperclip.paste()
 ISFP = pyperclip.paste()
 ENFJ = pyperclip.paste()
 INFJ = pyperclip.paste()
 ENFP = pyperclip.paste()
 INFP = pyperclip.paste()
 ENTJ = pyperclip.paste()
 INTJ = pyperclip.paste()
 ENTP = pyperclip.paste()
 INTP = pyperclip.paste()

ESTJ = ESTJ.replace('\n', ' ')
ESTJ = ESTJ.replace('/n', ' ')
ESTJ = ESTJ.split(', ')

personality_types = [ESTJ, ISTJ, ESFJ, ISFJ, ESTP, ISTP, ESFP, ISFP, ENFJ, INFJ, ENFP, INFP, ENTJ, INTJ, ENTP, INTP]

personalities = pd.DataFrame(ESTJ)
personalities1 = pd.DataFrame(ISTJ)
personalities2 = pd.DataFrame(ESFJ)
personalities3 = pd.DataFrame(ISFJ)
personalities4 = pd.DataFrame(ESTP)
personalities5 = pd.DataFrame(ISTP)
personalities6 = pd.DataFrame(ISFP)
personalities7 = pd.DataFrame(ENFJ)
personalities8 = pd.DataFrame(INFJ)
personalities9 = pd.DataFrame(ENFP)
personalities10 = pd.DataFrame(INFP)
personalities11 = pd.DataFrame(ENTJ)
personalities12 = pd.DataFrame(INTJ)
personalities13 = pd.DataFrame(ENTP)
personalities14 = pd.DataFrame(INTP)

personalities14['type'] = 'INTP'

frames = [personalities, personalities1, personalities2, personalities3, personalities4, personalities5, personalities6, personalities7, personalities8, personalities9, personalities10, personalities11, personalities12, personalities13, personalities14]
result = pd.concat(frames)



result['occupation'] = result[0]

result = result[['occupation', 'type']]


occupation1 = result['occupation']

occupation1 = occupation1.str.lower()
occupation_series = set(occupation1)


new_result1 = pd.DataFrame(occupation_series)


new_result1.to_csv('personalities_occupation_condensed.csv')
result_list = list(result['occupation'])
extraction = process.extractOne(myset[3], result_list)

(occupation, score) = extraction

result_list

big_list = []
for i in myset:
    match = process.extractOne(i, result_list)
    (occupation, score) = match
    stuff = [i, occupation]
    big_list.append(stuff)


big_df_list = pd.DataFrame(big_list)
big_df_list.to_csv('matched_occupations.csv')
