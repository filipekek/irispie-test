import sys
sys.path.append('..')

from modiphy.models.core import Model
import numpy as np

source_string = r"""
        !transition-variables
            a, b

        !parameters
            rho_a, ss_a

        !transition-equations
            a = rho_a * a{-1} + (1 - rho_a) * ss_a;
            b = b{-1} + a;

"""

m = Model.from_string(source_string, linear=True, flat=False)

m.assign(
    rho_a = 0.5,
    ss_a = 1,

);

m.steady()

xx = m._variants[0].levels
xx[1] = 0
yy = m._variants[0].changes

aa = m.create_qid_to_name()
bb = m.create_name_to_qid()

def testx(xx):
    data_array = np.array([1, 0, 0.5, 1])
    if not np.all(data_array==np.around(xx, 3)):
        raise Exception('Something is wrong')

def testy(yy):
    data_array = np.array([0, 1])
    pc = np.array([yy[0], yy[1]])
    if not np.all(data_array==np.around(pc, 3)):
        raise Exception('Something is wrong')

