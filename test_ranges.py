
import sys
sys.path.append("..")

from modiphy import *

import random


def create_dates():
    first_date = random.randint(1000, 1000)
    last_date = random.randint(first_date+1, first_date+1000)
    return first_date, last_date


def random_pick(number):
    r = random.randint(1,number)
    s = random.randint(1,number)
    return r, s


def create_diff_lists(r2, r3, r2_bw, r3_bw, pc_first_date, pc_last_date):
    l_2 = list(r2)
    l_3 = list(r3)
    l_bw_2 = list(r2_bw)
    l_bw_3 = list(r3_bw)
    l_length_2 = int(((pc_last_date-pc_first_date)/2)+1)
    l_length_3 = int(((pc_last_date-pc_first_date)/3)+1)
    return l_2, l_3, l_bw_2, l_bw_3, l_length_2, l_length_3


def create_lists(r, r_bw, pc_first_date, pc_last_date):
    l = list(r)
    l_bw = list(r_bw)
    l_length = (pc_last_date-pc_first_date)+1
    return l, l_bw, l_length


def assertion(r, r_bw, l, l_bw, l_length, r_other, r_bw_other, pc_first_date, pc_last_date):
    assert r == r_other
    assert r_bw == r_bw_other
    assert l_length == len(l)
    assert l_length == len(l_bw)
    for j in range(l_length):
        assert l[j]==pc_first_date+j
        assert l_bw[j]==pc_last_date-j


def assertion_diff(r, r_bw, l, l_bw, l_length, pc_first_date, pc_last_date, mult):
    assert l_length == len(l)
    assert l_length == len(l_bw)
    for j in range(l_length):
        assert l[j]==pc_first_date+j*mult
        assert l_bw[j]==pc_last_date-j*mult


def test_yy_range(num_tests):
    for i in range(num_tests):
        first_date, last_date = create_dates()

        pc_first_date = yy(first_date)
        pc_last_date = yy(last_date)
        r = Ranger(pc_first_date, pc_last_date, 1)
        r_bw = Ranger(pc_last_date, pc_first_date, -1)
        r_other = pc_first_date >> pc_last_date
        r_bw_other = pc_first_date << pc_last_date

        l, l_bw, l_length = create_lists(r, r_bw, pc_first_date, pc_last_date)

        assertion(r, r_bw, l, l_bw, l_length, r_other, r_bw_other, pc_first_date, pc_last_date)


def test_hh_range(num_tests):
    for i in range(num_tests):
        first_date, last_date = create_dates()
        first_half, last_half = random_pick(2)

        pc_first_date = hh(first_date, first_half)
        pc_last_date = hh(last_date, last_half)
        r = Ranger(pc_first_date, pc_last_date, 1)
        r_bw = Ranger(pc_last_date, pc_first_date, -1)
        r_other = pc_first_date >> pc_last_date
        r_bw_other = pc_first_date << pc_last_date

        l, l_bw, l_length = create_lists(r, r_bw, pc_first_date, pc_last_date)

        assertion(r, r_bw, l, l_bw, l_length, r_other, r_bw_other, pc_first_date, pc_last_date)


def test_qq_range(num_tests):
    for i in range(num_tests):
        first_date, last_date = create_dates()
        first_quarter, last_quarter = random_pick(4)

        pc_first_date = qq(first_date, first_quarter)
        pc_last_date = qq(last_date, last_quarter)
        r = Ranger(pc_first_date, pc_last_date, 1)
        r_bw = Ranger(pc_last_date, pc_first_date, -1)
        r_other = pc_first_date >> pc_last_date
        r_bw_other = pc_first_date << pc_last_date

        l, l_bw, l_length = create_lists(r, r_bw, pc_first_date, pc_last_date)

        assertion(r, r_bw, l, l_bw, l_length, r_other, r_bw_other, pc_first_date, pc_last_date)


def test_mm_range(num_tests):
    for i in range(num_tests):
        first_date, last_date = create_dates()
        first_month, last_month = random_pick(4)

        pc_first_date = mm(first_date, first_month)
        pc_last_date = mm(last_date, last_month)
        r = Ranger(pc_first_date, pc_last_date, 1)
        r_bw = Ranger(pc_last_date, pc_first_date, -1)
        r_other = pc_first_date >> pc_last_date
        r_bw_other = pc_first_date << pc_last_date

        l, l_bw, l_length = create_lists(r, r_bw, pc_first_date, pc_last_date)

        assertion(r, r_bw, l, l_bw, l_length, r_other, r_bw_other, pc_first_date, pc_last_date)


def test_dd_range(num_tests, year_1, month_1, day_1, year_2, month_2, day_2):
    """
    Input: first year, first_month, first day, second year, second_month, second day
    Recommended input (to check most):
    1) same year, different days
    2) different days and years (non leap)
    3) same year (leap), different days
    4) different days, different years)
    """
    first_date = dd(year_1, month_1, day_1)
    last_date = dd(year_2, month_2, day_2)
    r = Ranger(first_date, last_date, 1)
    r_bw = Ranger(last_date, first_date, -1)
    r_other = first_date >> last_date
    r_bw_other = first_date << last_date
    l = list(r)
    l_bw = list(r_bw)
    l_length = (last_date-first_date)+1

    assertion(r, r_bw, l, l_bw, l_length, r_other, r_bw_other, first_date, last_date)
    # print(l)


def test_by_more_yy(num_tests):
    for i in range(num_tests):
        first_date, last_date = create_dates()

        pc_first_date = yy(first_date)
        pc_last_date = yy(last_date)
        r_by2 = Ranger(pc_first_date, pc_last_date, 2)
        r_bw_by2 = Ranger(pc_last_date, pc_first_date, -2)
        r_by3 = Ranger(pc_first_date, pc_last_date, 3)
        r_bw_by3 = Ranger(pc_last_date, pc_first_date, -3)


        l_2, l_3, l_bw_2, l_bw_3, l_length_2, l_length_3 = create_diff_lists(r_by2, r_by3, r_bw_by2, r_bw_by3, pc_first_date, pc_last_date)

        assertion_diff(r_by2, r_bw_by2, l_2, l_bw_2, l_length_2, pc_first_date, pc_last_date, 2)
        assertion_diff(r_by3, r_bw_by3, l_3, l_bw_3, l_length_3, pc_first_date, pc_last_date, 3)


def test_by_more(num_tests, function, max):
    """
    inputs - function (function you want to test dd, mm...), max (number of the functions thingamagig)
    """
    for i in range(num_tests):
        first_year, last_year = create_dates()
        first_date, last_date = random_pick(max)

        pc_first_date = function(first_year, first_date)
        pc_last_date = function(last_year, last_date)
        r_by2 = Ranger(pc_first_date, pc_last_date, 2)
        r_by3 = Ranger(pc_first_date, pc_last_date, 3)
        r_bw_by2 = Ranger(pc_last_date, pc_first_date, -2)
        r_bw_by3 = Ranger(pc_last_date, pc_first_date, -3)

        l_2, l_3, l_bw_2, l_bw_3, l_length_2, l_length_3 = create_diff_lists(r_by2, r_by3, r_bw_by2, r_bw_by3, pc_first_date, pc_last_date)

        assertion_diff(r_by2, r_bw_by2, l_2, l_bw_2, l_length_2, pc_first_date, pc_last_date, 2)
        assertion_diff(r_by3, r_bw_by3, l_3, l_bw_3, l_length_3, pc_first_date, pc_last_date, 3)


def test_by_more_dd(num_tests):
    for i in range(num_tests):
        first_year, last_year = create_dates()
        first_month, last_month = random_pick(12)
        first_day, last_day = random_pick(28)

        pc_first_date = dd(first_year, first_month, first_day)
        pc_last_date = dd(last_year, last_month, last_day)
        r_by2 = Ranger(pc_first_date, pc_last_date, 2)
        r_bw_by2 = Ranger(pc_last_date, pc_first_date, -2)
        r_by3 = Ranger(pc_first_date, pc_last_date, 3)
        r_bw_by3 = Ranger(pc_last_date, pc_first_date, -3)

        l_2, l_3, l_bw_2, l_bw_3, l_length_2, l_length_3 = create_diff_lists(r_by2, r_by3, r_bw_by2, r_bw_by3, pc_first_date, pc_last_date)

        assertion_diff(r_by2, r_bw_by2, l_2, l_bw_2, l_length_2, pc_first_date, pc_last_date, 2)
        assertion_diff(r_by3, r_bw_by3, l_3, l_bw_3, l_length_3, pc_first_date, pc_last_date, 3)


def test_first_over_last(num_tests, function, max):
    """
    inputs - the same as test_by_more()
    """
    for i in range(num_tests):
        last_year, first_year = create_dates()
        if max == 0:
            first_date = 0
            last_date = 0
        elif max > 0:
            first_date, last_date = random_pick(max)

        pc_first_date = function(first_year, first_date)
        pc_last_date = function(last_year, last_date)
        r = Ranger(pc_first_date, pc_last_date, 1)
        r_bw = Ranger(pc_last_date, pc_first_date, -1)
        r_other = pc_first_date >> pc_last_date
        r_bw_other = pc_first_date << pc_last_date
        r_by2 = Ranger(pc_first_date, pc_last_date, 2)
        r_bw_by2 = Ranger(pc_last_date, pc_first_date, -2)
        r_by3 = Ranger(pc_first_date, pc_last_date, 3)
        r_bw_by3 = Ranger(pc_last_date, pc_first_date, -3)

        l, l_bw, l_length = create_lists(r, r_bw, pc_first_date, pc_last_date)
        l_2, l_3, l_bw_2, l_bw_3, l_length_2, l_length_3 = create_diff_lists(r_by2, r_by3, r_bw_by2, r_bw_by3, pc_first_date, pc_last_date)

        assert l == []
        assert l_bw == []
        assert l_2 == []
        assert l_bw_2 == []
        assert l_3 == []
        assert l_bw_3 == []
        assert r == r_other
        assert r_bw == r_bw_other


def test_same_dates(num_tests, function):
    year = random.randint(1000,1000)
    date = 1

    pc_date = function(year, date)
    r = Ranger(pc_date, pc_date, 1)
    r_bw = Ranger(pc_date, pc_date, -1)
    r_other = pc_date >> pc_date
    r_bw_other = pc_date << pc_date
    r_by2 = Ranger(pc_date, pc_date, 2)
    r_bw_by2 = Ranger(pc_date, pc_date, -2)
    r_by3 = Ranger(pc_date, pc_date, 3)
    r_bw_by3 = Ranger(pc_date, pc_date, -3)

    l, l_bw, l_length = create_lists(r, r_bw, pc_date, pc_date)
    l_2, l_3, l_bw_2, l_bw_3, l_length_2, l_length_3 = create_diff_lists(r_by2, r_by3, r_bw_by2, r_bw_by3, pc_date, pc_date)

    assert l == [pc_date]
    assert l_bw == [pc_date]
    assert l_2 == [pc_date]
    assert l_bw_2 == [pc_date]
    assert l_3 == [pc_date]
    assert l_bw_3 == [pc_date]
    assert r == r_other
    assert r_bw == r_bw_other


if __name__=="__main__":
    num_tests = 100
    test_yy_range(num_tests)
    test_hh_range(num_tests)
    test_qq_range(num_tests)
    test_mm_range(num_tests)
    test_dd_range(num_tests, 1998, 3, 16, 2004, 6, 12)
    test_by_more_yy(num_tests)
    test_by_more(num_tests, hh, 2)
    test_by_more(num_tests, mm, 12)
    test_by_more(num_tests, qq, 4)
    test_by_more_dd(num_tests)
    test_first_over_last(num_tests, yy, 0)
    test_first_over_last(num_tests, hh, 2)
    test_first_over_last(num_tests, qq, 4)
    test_first_over_last(num_tests, mm, 12)
    for i in [yy, hh, qq, mm]:
            test_same_dates(num_tests, i)


