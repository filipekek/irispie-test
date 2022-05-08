
import sys
sys.path.append("/home/filip")

from modiphy import yy, qq, hh, mm, ii, dd

import random

def test_yy():
    for i in range(1000):
        year = random.randint(-1000, 2000)
        plus = random.randint(1, 100)
        minus = random.randint(1, 100)
        pc_yy = int(yy(year))
        assert year+plus == pc_yy+plus, year-minus == pc_yy-minus

def test_hh():
    for i in range(1000):
        year = random.randint(-1000, 2000)
        half = random.randint(1, 2)
        hh_dc = year*2+(half-1)
        pc_hh = int(hh(year, half))
        plus = random.randint(1, 100)
        minus = random.randint(1, 100)
        assert hh_dc+plus == pc_hh+plus, hh_dc-minus == pc_hh-minus

def test_qq():
    for i in range(1000):
        year = random.randint(-1000, 2000)
        quarter = random.randint(1, 4)
        qq_dc = year*4+(quarter-1)
        pc_qq = int(qq(year, quarter))
        plus = random.randint(1, 100)
        minus = random.randint(1, 100)
        assert qq_dc+plus == pc_qq+plus, qq_dc-minus == pc_qq-minus

def test_mm():
    for i in range(1000):
        year = random.randint(-1000, 2000)
        month = random.randint(1, 12)
        mm_dc = year*12+(month-1)
        pc_mm = int(mm(year, month))
        plus = random.randint(1, 100)
        minus = random.randint(1, 100)
        assert mm_dc+plus == pc_mm+plus, mm_dc-minus == pc_mm-minus

def test_ii():
    for i in range(1000):
        ii_dc = random.randint(-1000, 2000)
        pc_ii = int(ii(ii_dc))
        plus = random.randint(1, 100)
        minus = random.randint(1, 100)
        assert ii_dc+plus == pc_ii+plus, ii_dc-minus == pc_ii-minus

#def test_all(max):
#    if max == None:
#        for i in range(1000):
#            year = random.randint(-1000, 2000)
#            plus = random.randint(1, 100)
#            minus = random.randint(1, 100)
#            pc_yy = int(yy(year))
#            assert year+plus == pc_yy+plus, year-minus == pc_yy-minus
#
##    elif max
#    else:
#        for i in range(1000):
#            year = random.randint(-1000, 2000)
#            quarter = random.randint(1, 4)
#            qq_dc = year*4+(quarter-1)
#            pc_qq = int(qq(year, quarter))
#            plus = random.randint(1, 100)
#            minus = random.randint(1, 100)
#            assert qq_dc+plus == pc_qq+plus, qq_dc-minus == pc_qq-minus

