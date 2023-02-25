import sys
sys.path.append('..')

from modiphy.models.core import Model
from modiphy.quantities import QuantityKind
from modiphy.equations import EquationKind


source = r"""


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

    !measurement-equations
        m_shk_x1 = mx1+3;
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
    manual_x = ['x1', 'x3', 'x2', 'shk_x1', 'shk_x2', 'shk_x3', 'shk_x4','mx1', 'm_shk_x1', 'rho_x1', 'ss_x1']
    _assertion(x, manual_x)

def test_quantities_descriptions(m):
    x = _create_list(m, "descript")
    manual_x = ['Variable x1', 'Variable x3','Variable x2','Shock x1', 'Shock x2', '', '','M Variable mx1', '', '', '']
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
    q.MEASUREMENT_VARIABLE,
    q.MEASUREMENT_SHOCK,
    q.PARAMETER,
    q.PARAMETER]
    _assertion(x, manual_x)

def test_quantities_entry(m):
    x = _create_list(m, "entry")
    manual_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    _assertion(x, manual_x)

def test_dynamic_equations_human(m):
    x = _create_list(m, "human")
    manual_x = ['x1 = rho_x1 * x1{-1} + (1 - rho_x1) * ss_x1 + shk_x1', 'x2 = shk_x1 * x2 + (3 + ss_x1)']
    _assertion(x, manual_x)

def test_dynamic_equations_descriptions(m):
    x = _create_list(m, "descript")
    manual_x = ['Equation x1', 'Equation x2']
    _assertion(x, manual_x)

def test_dynamic_equations_kinds(m, q):
    x = _create_list(m, "kind")
    manual_x = [q.TRANSITION_EQUATION, q.TRANSITION_EQUATION]
    _assertion(x, manual_x)

def test_dynamic_equations_entry(m):
    x = _create_list(m, "entry")
    manual_x = [0, 1]
    _assertion(x, manual_x)

def test_steady_equations_human(m):
    x = _create_list(m, "human")
    manual_x = ['x1 = 0', 'x2 = shk_x1 * x2 + (3 + ss_x1)']
    _assertion(x, manual_x)

def test_steady_equations_descriptions(m):
    x = _create_list(m, "descript")
    manual_x = ['Equation x1', 'Equation x2']
    _assertion(x, manual_x)

def test_steady_equations_kinds(m, q):
    x = _create_list(m, "kind")
    manual_x = [q.TRANSITION_EQUATION, q.TRANSITION_EQUATION]
    _assertion(x, manual_x)

def test_steady_equations_entry(m):
    x = _create_list(m, "entry")
    manual_x = [0, 1]
    _assertion(x, manual_x)

