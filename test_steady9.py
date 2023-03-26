import sys
sys.path.append('..')
import random


from modiphy.dataman.databanks import Databank
from modiphy.models.core import Model
import numpy as np

source_string = r"""
    !for ? = <range(300)> !do

    !transition-variables
        a?

    !parameters
        ss_a?, rho_a?

    !transition-equations
        a? = rho_a? * a?{-1} + (1 - rho_a?) * ss_a?;
!end
"""

m = Model.from_string(source_string, linear=True, flat=False)

p = Databank()
for i in range(300):
    p["rho_a"+str(i)] = random.random()/2
    p["ss_a"+str(i)] = random.randint(-1000, 1000)
m.assign_from_databank(p)

m.steady()

xx = m.get_steady_levels()

aa = m.create_qid_to_name()

def testx(xx):
    z = 0
    for i in range(300):
        f = abs(xx['a' + str(i)]-xx['ss_a' + str(i)])<10e-12
        if not f:
            raise Exception('System Overload')

