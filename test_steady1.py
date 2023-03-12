import sys
sys.path.append('..')

from modiphy.models.core import Model
import numpy as np

source_string = r"""
        !transition-variables
            a

        !transition-parameters
            rho_a, ss_a

        !transition-equations
            a = rho_a * a{-1} + (1 - rho_a) * ss_a;

        !measurement-variables
            b

        !measurement-equations
            b = a + 5;

"""

m = Model.from_string(source_string, linear=True, flat=True)

m.assign(
    rho_a = 0.5,
    ss_a = 1,
);

m.steady()

xx = m._variants[0].levels

aa = m.create_qid_to_name()
bb = m.create_name_to_qid()

#def test(xx):
#    data_array = np.array([
