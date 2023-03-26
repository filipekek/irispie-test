import sys
sys.path.append('..')

from modiphy.models.core import Model
import numpy as np

source_string = r"""
    !for ? = <range(300)> !do

    !transition-variables
        a?

    !transition-equations
        a? = 0.8*a?{-1} + (1 - 0.8) * 0.5;
!end
"""

m = Model.from_string(source_string, linear=True, flat=False)
m.steady()

#m.assign(
#    ss_a = 0.5
#);

xx = m._variants[0].levels
yy = m._variants[0].changes

aa = m.create_qid_to_name()

def testx(xx):
    z = 0
    for i in range(300):
        f = abs(xx[i]-0.5)
        if f > z:
            z = f
    print(z)

