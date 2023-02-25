import sys
sys.path.append('..')

from modiphy.models.core import Model
from modiphy.quantities import QuantityKind
from modiphy.equations import EquationKind


source = r"""
    !for ? = a, b, c !do

    !transition-shocks
        "Shock ?1" shk_?1
        shk_?2,

    !transition-variables
        ?

    !parameters
        rho_?

    !transition-equations
        ? = rho_? * ?{-1} + shk_?2 - shk_?1;

!end
"""

m = Model.from_string(source)


m._quantities

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

m._dynamic_equations


m._steady_equations

def _create_list(m, name):
    y = [ getattr(i, name) for i in m ]
    return y

def _assertion(x, manual_x):
    for i in range(len(manual_x)):
        assert manual_x[i] == x[i]

def test_quantities_human(m):
    x = _create_list(m, "human")
    manual_x = ['a', 'b', 'c', 'shk_a1', 'shk_a2', 'shk_b1', 'shk_b2', 'shk_c1', 'shk_c2', 'rho_a', 'rho_b', 'rho_c']
    _assertion(x, manual_x)

def test_quantities_descriptions(m):
    x = _create_list(m, "descript")
    manual_x = ['', '', '', 'Shock a1', '', 'Shock b1', '', 'Shock c1', '', '', '', '',]
    _assertion(x, manual_x)

def test_quantities_kinds(m, q):
    x = _create_list(m, "kind")
    manual_x = [
    q.TRANSITION_VARIABLE,
    q.TRANSITION_VARIABLE,
    q.TRANSITION_VARIABLE,
    q.TRANSITION_SHOCK,
    q.TRANSITION_SHOCK,
    q.TRANSITION_SHOCK,
    q.TRANSITION_SHOCK,
    q.TRANSITION_SHOCK,
    q.TRANSITION_SHOCK,
]
    _assertion(x, manual_x)

def test_quantities_entry(m):
    x = _create_list(m, "entry")
    manual_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    _assertion(x, manual_x)

def test_dynamic_equations_human(m):
    x = _create_list(m, "human")
    manual_x = ['a = rho_a * a{-1} + shk_a2 - shk_a1', 'b = rho_b * b{-1} + shk_b2 - shk_b1', 'c = rho_c * c{-1} + shk_c2 - shk_c1']
    _assertion(x, manual_x)

def test_dynamic_equations_descriptions(m):
    x = _create_list(m, "descript")
    manual_x = ['', '', '']
    _assertion(x, manual_x)

def test_dynamic_equations_kinds(m, q):
    x = _create_list(m, "kind")
    manual_x = [q.TRANSITION_EQUATION, q.TRANSITION_EQUATION, q.TRANSITION_EQUATION]
    _assertion(x, manual_x)

def test_dynamic_equations_entry(m):
    x = _create_list(m, "entry")
    manual_x = [0, 1, 2]
    _assertion(x, manual_x)
