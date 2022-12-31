
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

def test_yy_range():
    for i in range(1000):
        first_date, last_date = create_dates()

        pc_first_date = yy(first_date)
        pc_last_date = yy(last_date)
        r = Ranger(pc_first_date, pc_last_date, 1)
        r_backwards = Ranger(pc_last_date, pc_first_date, -1)
        r_other = pc_first_date >> pc_last_date
        r_bw_other = pc_first_date << pc_last_date


        l = list(r)
        l_length = (last_date-first_date)+1
        l_backwards = list(r_backwards)

        assert r == r_other
        assert r_backwards == r_bw_other
        assert l_length == len(l)
        assert l_length == len(l_backwards)
        for j in range(l_length):
            assert l[j]==pc_first_date+j
        for k in range(l_length):
            assert l_backwards[k]==pc_last_date-k

def test_hh_range():
    for i in range(1000):
        first_date, last_date = create_dates()
        first_half, last_half = random_pick(2)

        pc_first_date = hh(first_date, first_half)
