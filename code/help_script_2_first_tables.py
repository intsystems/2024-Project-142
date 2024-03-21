import pandas as pd
import pickle

df = pd.read_pickle('C:\goszakupki_okpd_data.pickle')

# Сначала подсчитаем, сколько раз каждое значение OKPD2 встречается в таблице
counts = df['OKPD2'].value_counts()
# Теперь отфильтруем counts, чтобы оставить только значения с более чем 10 вхождениями
filtered_counts = counts[counts > 10]

# Фильтруем исходный df, оставляя только строки с OKPD2, которые есть в filtered_counts
filtered_df = df[df['OKPD2'].isin(filtered_counts.index)]

# В результате filtered_df содержит только те записи, где значение OKPD2 встречается более 10 раз.
# filtered_df

'''
Подготовим два файла:  
1. Просто 200к записей +- равномерно по первому коду классификатора
2. 200к записей == 100 наиболей встречаемых классов, из них по 1к записей в каждом 
'''

filtered_df['new_code'] = filtered_df['OKPD2'].apply(lambda x: x.split('.')[0])
filtered_df_only_1_step = filtered_df.drop('OKPD2', axis=1).copy()
random_sample = filtered_df_only_1_step.sample(n=200000, random_state=1019)
#print(random_sample.groupby('new_code')['text'].count().sort_values())
random_sample.to_pickle("random_sample_200k.pickle")

filtered_df = filtered_df.drop('new_code', axis=1)
top_100_classes = filtered_df['OKPD2'].value_counts().nlargest(100).index
samples_per_class = 2000
final_sample = pd.DataFrame()

for class_value in top_100_classes:
    class_sample = filtered_df[filtered_df['OKPD2'] == class_value].sample(n=samples_per_class, random_state=1)
    final_sample = pd.concat([final_sample, class_sample], ignore_index=True)
final_sample.to_pickle("top_100_class_200k.pickle")
