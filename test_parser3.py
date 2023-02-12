import sys
sys.path.append('..')

import modiphy.parsers.model as pm
from modiphy.models.core import Model
from modiphy.quantities import QuantityKind
from modiphy.equations import EquationKind


source1 = r"""


    !transition-shocks
        "Shock x1" shk_x1
        "Shock x2" shk_x2,
        shk_x3; shk_x4

    !transition-variables
        "Variable x1" x1 "Variable x3" x3

    !parameters
        rho_x1 ss_x1

    !transition-equations
        "Equation x1" x1 = rho_x1 * x1{-1} + (1 - rho_x1) * ss_x1 + shk_x1 !! x1 = 0;

    !transition-equations
        "Equation x2" x2 = shk_x1 * x2 + (3 + ss_x1);

    !transition-variables
        "Variable x2" x2

    !measurement-variables
        "M Variable mx1" mx1

    !measurement-shocks
        m_shk_x1

    !log-variables
        x1 rho_x1 shk_x3
"""

s1 = pm.parse_from_string(source1)
s1.seal()

m1 = Model.from_source(s1)


source2 = r"""


    !transition-shocks
        "Shock x1" shk_x1
        "Shock x2" shk_x2,
        shk_x3; shk_x4

    !transition-variables
        "Variable x1" x1 "Variable x3" x3

    !parameters
        rho_x1 ss_x1

    !transition-equations
        "Equation x1" x1 = rho_x1 * x1{-1} + (1 - rho_x1) * ss_x1 + shk_x1 !! x1 = 0;

    !transition-equations
        "Equation x2" x2 = shk_x1 * x2 + (3 + ss_x1);

    !transition-variables
        "Variable x2" x2

    !measurement-variables
        "M Variable mx1" mx1

    !measurement-shocks
        m_shk_x1

    !log-variables !all-but
        x3, x2
"""

s2 = pm.parse_from_string(source2)
s2.seal()

m2 = Model.from_source(s2)


#m._quantities

#
# Ordering:
#
# * transition variables (within transition variables, ordered as entered by the user)
# * transition shocks
# * measurement variables
# * measurement shocks
# * parameters
#
# Human names
# Descriptions
# Quantity kinds
# Entry
#

#m._dynamic_equations


#m._steady_equations

def _create_list(m, name):
    y = [ getattr(i, name) for i in m ]
    return y

def _assertion(x, manual_x):
    for i in range(len(manual_x)):
        assert manual_x[i] == x[i]

def test_quantities_logly(m):
    x = _create_list(m, "logly")
    manual_x = [True, False, False, None, None, None, None, False, None, None, None]
    _assertion(x, manual_x)

def test_quantities_logly_allbut(m):
    x = _create_list(m, "logly")
    manual_x = [True, False, False, None, None, None, None, True, None, None, None]
    _assertion(x, manual_x)

