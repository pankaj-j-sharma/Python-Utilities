import pandas as pd

import pandas as pd

df = pd.read_csv('C:\\Interviews\\30-Days-Of-Python\\data\\F500.csv',
                 sep=";", encoding='unicode_escape')
df1 = pd.read_csv('C:\\Interviews\\30-Days-Of-Python\\data\\F500.csv',
                  sep=";", encoding='unicode_escape')

df.head()
df.describe()
df.memory_usage(deep=True)

df.columns
df.dtypes

df['name'] = df.name.astype('category')

df['name'].value_counts()  # count the values similar to group by
df.drop_duplicates(inplace=True)

df.employees = df.employees.astype('int')
df.groupby(by='name').employees.mean()

df_merged = df.merge(df1, on='id', how='left')
df.sort_values(by='name', inplace=True)

# df.columns
df['profits'].fillna(0, inplace=True)

# Pandas dtype 	Python type		NumPy type
# object		str or mixed	string_, unicode_, mixed types
# int64			int				int_, int8, int16, int32, int64, uint8, uint16, uint32, uint64
# float64		float			float_, float16, float32, float64
# bool			bool			bool_
