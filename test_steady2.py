import sys
sys.path.append('..')

from modiphy.models.core import Model
import numpy as np

source_string = r"""
        !transition-variables
            a

        !parameters
            rho_a, ss_a

        !transition-equations
            a = ss_a + rho_a * (a{-1} - ss_a);

        !measurement-variables
            b

        !measurement-equations
            b = 5*a + 3/rho_a;

"""

m = Model.from_string(source_string, linear=True, flat=True)

m.assign(
    rho_a = 0.8,
    ss_a = 1,
);

m.steady()

xx = m._variants[0].levels

aa = m.create_qid_to_name()
bb = m.create_name_to_qid()

def test(xx):
    data_array = np.array([1, 8.75, 0.8, 1])
    if not np.all(data_array==xx):
        raise Exception('Something is wrong')
