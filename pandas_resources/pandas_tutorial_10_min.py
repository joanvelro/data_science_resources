import numpy as np
import pandas as pd
"""
source : http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
"""

"""Object Creation"""
"""Creating a Series by passing a list of values, letting pandas create a default integer index:"""
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print('\n',s)

dates = pd.date_range('20130101', periods=6)
print('\n',dates)

"""Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:"""
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print('\n',df)

"""Creating a DataFrame by passing a dict of objects that can be converted to series-like"""
df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})
print('\n',df2)

print('\n',df2.dtypes)

"""
Viewing Data
"""
print('\n',df.head(10))

print('\n',df.tail(10))

print('\n',df.columns)

print('\n',df.columns.values)

print('\n',df.index)

print('\n','df.values:','\n',df.values)

print('\n','df.describe():','\n',df.describe())

print('\n','df.T:','\n',df.T)

print('\n',df.head(10))

print('\n','df.sort_index(axis=1, ascending=False):','\n',df.sort_index(axis=1, ascending=False))

print('\n','df.sort_index(axis=0, ascending=False):','\n',df.sort_index(axis=0, ascending=False))

print('\n','df.sort_values(by=B):','\n',df.sort_values(by='B'))

"""
Selection
"""

"""Slice columns"""
print('\n',df.head())

print('\n',df['A'])

print('\n',df.iloc[:,0])

print('\n',df.loc[:,'A'])

print('\n',df.A)


"""Slice rows"""
print('\n',df[0:3])

print('\n',df['20130102':'20130104'])


"""Selection by Label"""
print('\n',df.loc[dates[0]])


"""Selecting on a multi-axis by label:"""
print('\n',df.loc[:, ['A', 'B']])

print('\n',df.loc['20130102':'20130104', ['A', 'B']])

print('\n',df.loc['20130104', ['A', 'B']])


print('\n',df.loc[dates[0], 'A'])

"""Select via the position of the passed integers"""
print('\n',df.iloc[3])

print(type(df.iloc[3]))

print('\n',df.iloc[3:5, 0:2])

print('\n',df.iloc[[1, 2, 4], [0, 2]])

print('\n',df.iloc[1:3, :])

print('\n',df.iloc[:, 1:3])

print('\n',df.iloc[1, 1])

"""Boolean Indexing"""
print('\n',df[df.A > 0])

print('\n',df[df > 0])


""" Adding"""
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']

""" filtering"""
print('\n',df2[df2['E'].isin(['two', 'four'])])

"""Setting"""
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
print('\n',s1)

df['F'] = s1

df.at[dates[0], 'A'] = 0 # faster

df[dates[0], 'A'] = 0

df.iat[0, 1] = 0

df.loc[:, 'D'] = np.array([5] * len(df))

df2 = df.copy()

df2[df2 > 0] = -df2

print('\n',df2.head())


