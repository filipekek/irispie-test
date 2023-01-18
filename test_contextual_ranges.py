
import sys
sys.path.append('..')

from modiphy import *

import random

class Dates():
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

def _random_pick(max):
    x = random.randint(1, max)
    return x

ddd = lambda x,y: dd(x, ..., y)

def _create_date(function, max, max2):
    year = _random_pick(3000)
    sub = _random_pick(max)
    if max2 and function == dd:
        sub2 = _random_pick(max2)
        date = function(year, sub, sub2)
    elif not max2 and function != dd:
        date = function(year, sub)
    elif not max2 and function == dd:
        date = ddd(year, sub)
    else:
        raise Exception('questionable, error in input probably')
    return date

def _create_start_end(function, max, max2):
    start_date = _create_date(function, max, max2)
    end_date = _create_date(function, max, max2)
    dates = Dates(start_date, end_date)
    return dates

def _create_range1(dates, function, max, max2):
    other_date = _create_date(function, max, max2)
    if dates.start_date > other_date:
        r = Ranger(start, other_date, -1)
        r_manual = Ranger(dates.start_date, other_date, -1)
    elif dates.start_date < other_date:
        r = Ranger(start, other_date, 1)
        r_manual = Ranger(dates.start_date, other_date, 1)
    else:
        raise Exception('something is wrong 1')
    return r, r_manual

def _create_range2(dates, function, max, max2):
    other_date = _create_date(function, max, max2)
    if dates.end_date > other_date:
        r = Ranger(other_date, end, 1)
        r_manual = Ranger(other_date, dates.end_date, 1)
    elif dates.end_date < other_date:
        r = Ranger(other_date, end, -1)
        r_manual = Ranger(other_date, dates.end_date, -1)
    else:
        raise Exception('something is wrong 2')
    return r, r_manual

def _create_range3(dates):
    if dates.start_date > dates.end_date:
        r = Ranger(start, end, -1)
        r_manual = Ranger(dates.start_date, dates.end_date, -1)
    elif dates.start_date < dates.end_date:
        r = Ranger(start, end, 1)
        r_manual = Ranger(dates.start_date, dates.end_date, 1)
    else:
        raise Exception('something is wrong 3')
    return r, r_manual

def _create_range4(dates, k):
    if dates.start_date > dates.end_date:
        r = Ranger(start+k, end+k, -1)
        r_manual = Ranger(dates.start_date+k, dates.end_date+k, -1)
    elif dates.start_date < dates.end_date:
        r = Ranger(start+k, end+k, 1)
        r_manual = Ranger(dates.start_date+k, dates.end_date+k, 1)
    else:
        raise Exception('something is wrong 4')
    return r, r_manual

def _create_range5(dates, k, m):
    if dates.start_date+k > dates.start_date+m:
        r = Ranger(start+k, start+m, -1)
        r_manual = Ranger(dates.start_date+k, dates.start_date+m, -1)
    elif dates.start_date+k < dates.start_date+m:
        r = Ranger(start+k, start+m, 1)
        r_manual = Ranger(dates.start_date+k, dates.start_date+m, 1)
    else:
        raise Exception('something is wrong 5')
    return r, r_manual

def _create_range6(dates, k, m):
    if dates.end_date+k > dates.end_date+m:
        r = Ranger(end+k, end+m, -1)
        r_manual = Ranger(dates.end_date+k, dates.end_date+m, -1)
    elif dates.end_date+k < dates.end_date+m:
        r = Ranger(end+k, end+m, 1)
        r_manual = Ranger(dates.end_date+k, dates.end_date+m, 1)
    else:
        raise Exception('something is wrong 6')
    return r, r_manual

def _resolve_assert(dates, r, r_manual):
    r_resolved = r.resolve(dates)
    assert r_resolved == r_manual

def test_ranges(test, k, m, function, max, max2=None):
    """
    inputs: test, k, m, function, max, max2(optional)

    test input help:
    1 - start, fixed
    2 - fixed, end
    3 - start, end
    4 - start + k, end + k
    5 - start + k, start + m
    6 - end + k, end + m

    k, m: list (can be empty for 1-3, must be same length)
    """
    if len(k) != len(m):
        raise Exception("lists aren't the same length")
    dates = _create_start_end(function, max, max2)

    if test == 1:
        r, r_manual = _create_range1(dates, function, max, max2)
        _resolve_assert(dates, r, r_manual)

    if test == 2:
        r, r_manual = _create_range2(dates, function, max, max2)
        _resolve_assert(dates, r, r_manual)

    if test == 3:
        r, r_manual = _create_range3(dates)
        _resolve_assert(dates, r, r_manual)

    if test == 4:
        for i in k:
            r, r_manual = _create_range4(dates, i)
            _resolve_assert(dates, r, r_manual)

    if test == 5:
        for i in range(len(k)):
            r, r_manual = _create_range5(dates, k[i], m[i])
            _resolve_assert(dates, r, r_manual)

    if test == 6:
        for i in range(len(k)):
            r, r_manual = _create_range6(dates, k[i], m[i])
            _resolve_assert(dates, r, r_manual)

def test_freq_mismatch(function1, function2, max1, max2):
    start_date = function1(2000, max1)
    end_date = function2(2003, max2)
    dates = Dates(start_date, end_date)
    r = (start, end)

    error = False
    try:
        r_res = r.resolve(dates)
    except:
        error = True
    assert error

if __name__ == '__main__':
    test_ranges(1, [], [], yy, 1)
    test_ranges(1, [], [], hh, 2)
    test_ranges(1, [], [], qq, 4)
    test_ranges(1, [], [], mm, 12)
    test_ranges(1, [], [], dd, 365)
    test_ranges(1, [], [], dd, 12, 28)

    test_ranges(2, [], [], yy, 1)
    test_ranges(2, [], [], hh, 2)
    test_ranges(2, [], [], qq, 4)
    test_ranges(2, [], [], mm, 12)
    test_ranges(2, [], [], dd, 365)
    test_ranges(2, [], [], dd, 12, 28)

    test_ranges(3, [], [], yy, 1)
    test_ranges(3, [], [], hh, 2)
    test_ranges(3, [], [], qq, 4)
    test_ranges(3, [], [], mm, 12)
    test_ranges(3, [], [], dd, 365)
    test_ranges(3, [], [], dd, 12, 28)

    k = [-3, -2, -1, 0, 1, 2, 3]
    m = [-4, -3, -2, -1, 0, 1, 2]

    test_ranges(4, k, k, yy, 1)
    test_ranges(4, k, k, hh, 2)
    test_ranges(4, k, k, qq, 4)
    test_ranges(4, k, k, mm, 12)
    test_ranges(4, k, k, dd, 365)
    test_ranges(4, k, k, dd, 12, 28)

    test_ranges(5, k, m, yy, 1)
    test_ranges(5, k, m, hh, 2)
    test_ranges(5, k, m, qq, 4)
    test_ranges(5, k, m, mm, 12)
    test_ranges(5, k, m, dd, 365)
    test_ranges(5, k, m, dd, 12, 28)


    test_ranges(6, k, m, yy, 1)
    test_ranges(6, k, m, hh, 2)
    test_ranges(6, k, m, qq, 4)
    test_ranges(6, k, m, mm, 12)
    test_ranges(6, k, m, dd, 365)
    test_ranges(6, k, m, dd, 12, 28)

    test_freq_mismatch(yy, qq, 1, 4)
    test_freq_mismatch(hh, mm, 2, 12)
