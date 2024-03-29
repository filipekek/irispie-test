import sys
sys.path.append('..')

from irispie.models.core import Model
from irispie.quantities import QuantityKind
from irispie.equations import EquationKind


source = r"""


    !transition-shocks
        shk_x1 

    !transition-variables
        "Variable x1" x1 

    !parameters
        rho_x1, ss_x1

    !transition-equations
        "Equation x1" x1 = rho_x1 * x1{-1} + (1 - rho_x1) * ss_x1 + shk_x1 !! x1 = 0;


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
    manual_x = ['x1', 'shk_x1', 'rho_x1', 'ss_x1']
    _assertion(x, manual_x)

def test_quantities_descriptions(m):
    x = _create_list(m, "descript")
    manual_x = ['Variable x1', '','','']
    _assertion(x, manual_x)

def test_quantities_kinds(m, q):
    x = _create_list(m, "kind")
    manual_x = [q.TRANSITION_VARIABLE, q.TRANSITION_SHOCK, q.PARAMETER, q.PARAMETER]
    _assertion(x, manual_x)

def test_quantities_entry(m):
    x = _create_list(m, "entry")
    manual_x = [0, 1, 2, 3]
    _assertion(x, manual_x)

def test_dynamic_equations_human(m):
    x = _create_list(m, "human")
    manual_x = ['x1 = rho_x1 * x1{-1} + (1 - rho_x1) * ss_x1 + shk_x1']
    _assertion(x, manual_x)

def test_dynamic_equations_descriptions(m):
    x = _create_list(m, "descript")
    manual_x = ['Equation x1']
    _assertion(x, manual_x)

def test_dynamic_equations_kinds(m, q):
    x = _create_list(m, "kind")
    manual_x = [q.TRANSITION_EQUATION]
    _assertion(x, manual_x)

def test_dynamic_equations_entry(m):
    x = _create_list(m, "entry")
    manual_x = [0]
    _assertion(x, manual_x)

def test_steady_equations_human(m):
    x = _create_list(m, "human")
    manual_x = ['x1 = 0']
    _assertion(x, manual_x)

def test_steady_equations_descriptions(m):
    x = _create_list(m, "descript")
    manual_x = ['Equation x1']
    _assertion(x, manual_x)

def test_steady_equations_kinds(m, q):
    x = _create_list(m, "kind")
    manual_x = [q.TRANSITION_EQUATION]
    _assertion(x, manual_x)

def test_steady_equations_entry(m):
    x = _create_list(m, "entry")
    manual_x = [0]
    _assertion(x, manual_x)

