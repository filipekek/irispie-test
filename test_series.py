
import sys
sys.path.append('..')

import numpy as np
from modiphy.dataman import *
from IPython import embed

x = Series(num_columns=2)

y = Series(num_columns=2)

t = qq(2023,1)

class Dates:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

def _test(x, y):
    if not np.all(np.logical_or(x==y, np.logical_and(np.isnan(x), np.isnan(y)))):
        raise Exception('somethings is wrong')

def variation1(t):
    data = np.array([
        [1, 10],
        [2, 20],
        [3, 30],
])

    x[t>>t+2] = data

    _test(x[t], np.array([1, 10]))
    _test(x[t+1], np.array([2, 20]))
    _test(x[t+2], np.array([3, 30]))
    _test(x[t+3], np.array([np.nan, np.nan]))
    _test(x[t-1], np.array([np.nan, np.nan]))

def variation2(t):
    data1 = np.array([
        [11],
        [12],
        [13],
    ])

    x[t>>t+2] = data1

    _test(x[t>>t+1], np.array([[11,11], [12,12]]))
    _test(x[t+2>>t+3], np.array([[13, 13], [np.nan, np.nan]]))
    _test(x[t+3>>t+4], np.array([[np.nan, np.nan], [np.nan, np.nan]]))

def variation3(t):
    y[t>>t+2] = ([1,2,3], [10,20,30])

    _test(y[t], np.array([1, 10]))
    _test(y[t+1>>t+2], np.array([[2, 20], [3, 30]]))
    _test(y[t-1], np.array([np.nan, np.nan]))

def variation4(t):
    y[t>>t+2] = [1, 2, 3]

    _test(y[t], np.array([1,1]))
    _test(y[t+2], np.array([3, 3]))
    _test(y[t-1>>t+1], np.array([[np.nan, np.nan], [1, 1], [2, 2]]))

def variation5(t):
    y[t] = (100, 200)

    _test(y[t], np.array([100, 200]))

def variation6(t):
    y[t>>t+2] = (100, 200)

    _test(y[t>>t+2], np.array([[100, 200], [100, 200], [100, 200]]))

def variation7(t):
    y = Series(num_columns=2)
    y[ [t, t-10, t+10] ] = ( [123, 456, 789], -1000 )
    j = np.array([
    [456, -1000],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [123, -1000],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [np.nan, np.nan],
    [789, -1000]
])

    _test(y[t-10>>t+10], j)

def variation8(t):
    y[t>>t+2, 0] = [1000, 2000, 3000]

    _test(y[t>>t+2], np.array([[1000, np.nan], [2000, np.nan], [3000, np.nan]]))

def variation9(t):
    y[t>>t+2, 1] = [-1000, 2000, 3000]

    _test(y[t>>t+2], np.array([[np.nan, -1000], [np.nan, 2000], [np.nan, 3000]]))

def variation10():
    z = Series(num_columns=2)
    data = np.array([
    [1, 100],
    [2, 200],
    [3, 300],
])
    z[qq(2020, 2) >> qq(2020, 4)] = data


    _test(z[start>>qq(2020,4)], np.array([[1, 100], [2, 200], [3, 300]]))
    _test(z[qq(2020, 2)>>end], np.array([[1, 100], [2, 200], [3, 300]]))
    _test(z[start>>end], np.array([[1, 100], [2, 200], [3, 300]]))
    _test(z[start-1>>end], np.array([[np.nan, np.nan], [1, 100], [2, 200], [3, 300]]))
    _test(z[start>>end-1], np.array([[1, 100], [2, 200]]))
