#!/usr/bin/env
"""
    Test memory pandas

    (C) Jose Angel Velasco (joseangel.velasco@yahoo.es
    Nov. 2020
"""
import pandas as pd
import numpy as np
import time
import psutil

# gives a single float value
# gives an object with many fields
psutil.virtual_memory()
# you can convert that object to a dictionary
dict(psutil.virtual_memory()._asdict())
# gives an object with many fields
psutil.virtual_memory()
# you can convert that object to a dictionary
dict(psutil.virtual_memory()._asdict())

memory_available_GB = psutil.virtual_memory().available / 1000000000
print('\n')
print('======= Memory available BEFORE test ======:', round(memory_available_GB, 2), 'GB')


# Requires at least 12GB RAM free
def test_data_set_int():
    df = pd.DataFrame(data=np.random.random((100000000, 10)), columns=['column_{}'.format(i) for i in range(10)])
    return df


print('\n')
print('      .')
print('      .')
print('      .')
print('  Test in progres ')
print('      .')
print('      .')
print('      .')

df = test_data_set_int()
# print(x)


memory_available_GB2 = psutil.virtual_memory().available / 1000000000
print('\n')
print('======= Memory available AFTER test ======:', round(memory_available_GB2, 2), 'GB')

print('\n')
print('======= Memory occupation =========:', round(memory_available_GB - memory_available_GB2, 2), 'GB')

if 0 == 0:
    print('\n')
    print('======= Describe data frame operation ===== ')

    start_time = time.time()
    try:
        df.describe()
    except NameError:
        print('Fail in operate with dataframe')
    print("--- %s seconds ---" % (time.time() - start_time))

if 1 == 0:
    print('\n')
    print('======= Writing test data ======')
    df.to_csv("test_memory_pandas_data.csv")
