
import sys


from irispie.sources import (
    ModelSource,
)

from irispie.equations import (
    finalize_from_human,
)


from irispie.quantities import (
    create_name_to_qid,
)

from irispie.incidence import Token

s = Source.from_lists(
    transition_variables=["a", "y", "c", "i", "k", "r", "c_to_y", "i_to_y", "x"],
    parameters=["ss_a", "rho", "beta", "gamma", "delta"],
    transition_shocks=["shock_a"],
    transition_equations=[
        "c = beta*r*c{+1}",
        "k = (1 - delta)*k{-1} + i",
        "y = a^(1-gamma) * k{-1}^gamma",
        "gamma*y = k{-1} * (r - 1 + delta)",
        "y = i + c",
        "log(a) = rho*log(a{-1}) + (1 - rho)*log(ss_a) + shock_a",
        "c_to_y = c / y",
        "i_to_y = i / y",
        "x = 0.2*x{-1} + 0.1*x{-2} + 0.2*x{+1} + 0.1*x{+2} + (1-0.6)*4",
    ],
)

s1 = Source.from_lists(
    transition_variables=["a", "y", "c", "i", "k", "r", "c_to_y", "i_to_y", "x"],
    parameters=["ss_a", "rho", "beta", "gamma", "delta"],
    transition_shocks=["shock_a"],
    transition_equations=[
        "i_to_y = c*delta{+2}-ss_a*3",
        "shock_a = 4*x*y{-2}*r",
        "rho-i = r*2+gamma{-3}+83",
        "x-beta+i_to_y{-2} = rho*8"
    ],
)


q = s.quantities
e = s.equations
name_to_qids = create_name_to_qid(q)
finalize_equations_from_humans(e, name_to_qids)

q1 = s1.quantities
e1 = s1.equations
name_to_qids1 = create_name_to_qid(q1)
finalize_equations_from_humans(e1, name_to_qids1)


def create_t(list):
    return set( Token(*i) for i in list )

def assertion(t, e):
    assert t == e

def list1():
    """
    c = beta*r*c{+1}
    """
    list = [(2, 0), (12, 0), (5, 0), (2, 1)]
    return list

def list2():
    """
    k = (1 - delta)*k{-1} + i
    """
    list = [(4, 0), (14, 0), (4, -1), (3, 0)]
    return list

def list3():
    """
    y = a^(1-gamma) * k{-1}^gamma
    """
    list = [(1, 0), (0, 0), (13, 0), (4, -1)]
    return list

def list4():
    """
    gamma*y = k{-1} * (r - 1 + delta)
    """
    list = [(13, 0), (1, 0), (4, -1), (5, 0), (14, 0)]
    return list

def list5():
    """
    y = i + c
    """
    list = [(1, 0), (3, 0), (2, 0)]
    return list

def list6():
    """
    log(a) = rho*log(a{-1}) + (1 - rho)*log(ss_a) + shock_a
    """
    list = [(0, 0), (11, 0), (0, -1), (10, 0), (9, 0)]
    return list

def list7():
    """
    c_to_y = c / y
    """
    list = [(6, 0), (2, 0), (1, 0)]
    return list

def list8():
    """
    i_to_y = i / y
    """
    list = [(7, 0), (3, 0), (1, 0)]
    return list

def list9():
    """
    x = 0.2*x{-1} + 0.1*x{-2} + 0.2*x{+1} + 0.1*x{+2} + (1-0.6)*4
    """
    list = [(8, 0), (8, -1), (8, -2), (8, 1), (8, 2)]
    return list

def list1_s1():
    """
    i_to_y = c*delta{+2}-ss_a*3
    """
    list = [(7, 0), (2, 0), (14, 2), (10, 0)]
    return list

def list2_s1():
    """
    shock_a = 4*x*y{-2}*r
    """
    list = [(9, 0), (8, 0), (1, -2), (5, 0)]
    return list

def list3_s1():
    """
    rho-i = r*2+gamma{-3}+83
    """
    list = [(11, 0), (3, 0), (5,0), (13, -3)]
    return list

def list4_s1():
    """
    x-beta+i_to_y{-2} = rho*8
    """
    list = [(8, 0), (12, 0), (7, -2), (11, 0)]
    return list

def equation_test(list, equation):
    t = create_t(list)
    assertion(t, equation.incidence)

if __name__ == "__main__":
    equation_test(list1(), e[0])
    equation_test(list2(), e[1])
    equation_test(list3(), e[2])
    equation_test(list4(), e[3])
    equation_test(list5(), e[4])
    equation_test(list6(), e[5])
    equation_test(list7(), e[6])
    equation_test(list8(), e[7])
    equation_test(list9(), e[8])

    equation_test(list1_s1(), e1[0])
    equation_test(list2_s1(), e1[1])
    equation_test(list3_s1(), e1[2])
    equation_test(list4_s1(), e1[3])
