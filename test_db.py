import sys
sys.path.append('..')

from irispie import *

# Create a new empty "databank"
d = Databank()
d1 = Databank()

# Fill in a couple of entries
d.a = 1
d.b = "xxxx"
d.c = True
d.ddd = [1,2,3]

d1.copy = 12

def _test(x, y):
    assert x == y

def _loop_test(x, y, names):
    for n in names:
        _test(x[n], y[n])

def test_names(d):
    e = d._copy()
    _test(e.get_names(), ['a', 'b', 'c', 'ddd'])

    e1 = d.copy()
    _test(e1.get_names(), ['a', 'b', 'c', 'ddd'])

    a = d.copy()
    a._rename(["a", "c"], ["A", "C"])
    _test(a.get_names(), ['A', 'C', 'b', 'ddd'])

    b = d.copy()
    b._keep(["b", "ddd"])
    _test(b.get_names(), ['b', 'ddd'])

    e._remove(["a", "ddd"])
    _test(e.get_names(), ['b', 'c'])

    f = d1._copy()
    _test(f.get_names(), ['copy'])

def test_data(d):
    a = d.copy()
    names_a = a.get_names()
    _loop_test(a, d, names_a)

    b = d._copy()
    names_b = b.get_names()
    _loop_test(b, d, names_b)

    c = d.copy()
    c._rename(target_names=lambda n: n.upper())
    for i in d.get_names():
        _test(d[i], c[i.upper()])

    e = d.copy()
    e._keep(['b', 'ddd'])
    names_e = e.get_names()
    _loop_test(e, d, names_e)

    f = d.copy()
    f._remove(["a", "ddd"])
    names_f = f.get_names()
    _loop_test(f, d, names_f)

    g = d1._copy()
    names_g = g.get_names()
    _loop_test(g, d1, names_g)
