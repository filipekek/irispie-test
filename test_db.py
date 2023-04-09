import sys
sys.path.append('..')

from irispie import *

# Create a new empty "databank"
d = Databank()

# Fill in a couple of entries
d.a = 1
d.b = "xxxx"
d.c = True
d.ddd = [1,2,3]

def _test(x, y):
    assert x == y

def test_names(d):
    e = d._copy()
    _test(e.get_names(), ['a', 'b', 'c', 'ddd'])

    e1 = d.copy()
    _test(e1.get_names(), ['a', 'b', 'c', 'ddd'])

    d._rename(["a", "c"], ["A", "C"])
    _test(d.get_names(), ['A', 'C', 'b', 'ddd'])

    d._keep(["b", "ddd"])
    _test(d.get_names(), ['b', 'ddd'])

    e._remove(["a", "ddd"])
    _test(e.get_names(), ['b', 'c'])
