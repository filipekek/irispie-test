
import sys
sys.path.append("..")

from modiphy import *

import random

class A:
    pass

class B:
    def __init__(self, start_date):
        self.start_date = start_date

class C:
    def __init__(self, end_date):
        self.end_date = end_date

class D:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

ddd = lambda year, day: dd(year, ..., day)

def _random_year():
    x = random.randint(0, 3000)
    y = random.randint(0, 3000)
    return x,y

def _random_pick(max):
    x = random.randint(1, max)
    y = random.randint(1, max)
    return x,y

def _test_errors(test, function):
    error = False
    try:
        res = function.resolve(test)
    except:
        error = True

    assert error

def _assertion(start_date, end_date, b_res, c_res, d_res_s, d_res_e, k):
    assert b_res == start_date+k
    assert c_res == end_date+k
    assert d_res_s == start_date+k
    assert d_res_e == end_date+k


def test_basic_context(function, max, max2=None):
    for k in range(-5, 5):
        x, y = _random_year()
        x1, y1 = _random_pick(max)
        if max2:
            x2, y2 = _random_pick(max2)
            start_date = function(x, x1, x2)
            end_date = function(y, y1, y2)
        elif not max2 and function != dd:
            start_date = function(x, x1)
            end_date = function(y, y1)
        elif not max2 and function == dd:
            start_date = ddd(x, x1)
            end_date = ddd(y, y1)

        s = start+k
        e = end+k
        a = A()
        b = B(start_date)
        c = C(end_date)
        d = D(start_date, end_date)

        _test_errors(a, s)
        _test_errors(a, e)

        b_res = s.resolve(b)
        _test_errors(b, e)

        c_res = e.resolve(c)
        _test_errors(c, s)

        d_res_s = s.resolve(d)
        d_res_e = e.resolve(d)

        _assertion(start_date, end_date, b_res, c_res, d_res_s, d_res_e, k)

if __name__ == '__main__':
    test_basic_context(yy, 1)
    test_basic_context(hh, 2)
    test_basic_context(qq, 4)
    test_basic_context(mm, 12)
    test_basic_context(dd, 12, 28)
    test_basic_context(dd, 365)
