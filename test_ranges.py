
import sys
sys.path.append("/home/filip")

from modiphy import *

import random

def create_dates():
    first_date = random.randint(-1000, 1000)
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

def test_yy_range():
    for i in range(1000):
        first_date, last_date = create_dates()

        pc_first_date = yy(first_date)
        pc_last_date = yy(last_date)
        r = Ranger(pc_first_date, pc_last_date, 1)
        r_bw = Ranger(pc_last_date, pc_first_date, -1)
        r_other = pc_first_date >> pc_last_date
        r_bw_other = pc_first_date << pc_last_date

        l, l_bw, l_length = create_lists(r, r_bw, pc_first_date, pc_last_date)

        assertion(r, r_bw, l, l_bw, l_length, r_other, r_bw_other, pc_first_date, pc_last_date)

def test_hh_range():
    for i in range(1000):
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


def test_qq_range():
    for i in range(1000):
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

def test_mm_range():
    for i in range(1000):
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

def test_dd_range(year_1, month_1, day_1, year_2, month_2, day_2):
    """
    Input: first year, first_month, first day, second year, second_month, second day
    Reccomended input (to check most):
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
    print(l)

def test_by_more_yy():
    for i in range(1000):
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

def test_by_more(function, max):
    for i in range(1000):
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

