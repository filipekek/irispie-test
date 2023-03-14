import sys
sys.path.append('..')

from modiphy.models.core import Model
import numpy as np

source_string = r"""
        !transition-variables
            a

        !parameters
            rho_a, ss_a, rho_x, ss_x, shock_c

        !transition-equations
            a = rho_a * a{-1} + (1 - rho_a) * ss_a;

        !measurement-variables
            b, c

        !measurement-equations
            b = a + 5;

        !transition-variables
            x

        !transition-equations
            x = ss_x + rho_x * (x{-1} - ss_x);

        !measurement-equations
            c = shock_c * a + 1;

"""

m = Model.from_string(source_string, linear=True, flat=True)

m.assign(
    rho_a = 0.5,
    ss_a = 1,
    rho_x = 0.7,
    ss_x = 4,
    shock_c = 3
);

m.steady()

xx = m._variants[0].levels

aa = m.create_qid_to_name()
bb = m.create_name_to_qid()

def test(xx):
    data_array = np.array([1, 4, 6, 4, 0.5, 1, 0.7, 4, 3])
    if not np.all(data_array==xx):
        raise Exception('Something is wrong')

