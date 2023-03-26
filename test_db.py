import sys
sys.path.append('..')

from irispie import *

# Create a new empty "databank"
d = db_.Databank()

# Fill in a couple of entries
d.a = 1
d.b = "xxxx"
d.c = True
d.ddd = [1,2,3]

print(d)
print("-"*30)

e = d._copy()
print(e)
print("-"*30)

d._rename(["a", "c"], ["A", "C"])
print(d)
print("-"*30)

d._keep(["b", "ddd"])
print(d)
print("-"*30)

e._remove(["a", "ddd"])
print(e)
print("-"*30)
