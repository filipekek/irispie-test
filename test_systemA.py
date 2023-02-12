
import sys
sys.path.append('..')

import modiphy as md
import numpy

numpy.set_printoptions(linewidth=100000)

s = md.Source.from_lists(
    transition_variables=["a", "y", "c", "i", "k", "r", "c_to_y", "i_to_y", "x"],
    measurement_variables=["obs_c", "obs_y", "obs_i"],
    parameters=["ss_a", "rho", "beta", "gamma", "delta"],
    transition_shocks=["shock_a"],
    measurement_shocks=["shock_obs_i", "shock_obs_c"],
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
    measurement_equations=[
        "obs_y = y",
        "obs_c = c",
        "obs_i = i + shock_obs_i",
    ],
)

    # all_but=True,
    # log_variables=["c_to_y", "i_to_y", "r"],


m = md.Model.from_source(s)

m.assign(
    a=1,
    y=3.275862068965518,
    c=2.202734839476814,
    i=1.073127229488705,
    k=10.731272294887045,
    r=1.0526315789473685,
    c_to_y=2.202734839476814/3.275862068965518,
    i_to_y=1.073127229488705/3.275862068965518,
    x=0,
    beta=0.95,
    gamma=0.50,
    delta=0.10,
    rho=0.8,
    ss_a=1,
    obs_y=3.275862068965518,
    obs_c=2.202734839476814,
    obs_i=1.073127229488705,
)

asgn = {
    'a':1,
    'y':3.275862068965518,
    'c':2.202734839476814,
    'i':1.073127229488705,
    'k':10.731272294887045,
    'r':1.0526315789473685,
    'c_to_y':2.202734839476814/3.275862068965518,
    'i_to_y':1.073127229488705/3.275862068965518,
    'x':0,
    'beta':0.95,
    'gamma':0.50,
    'delta':0.10,
    'rho':0.8,
    'ss_a':1,
    'obs_y':3.275862068965518,
    'obs_c':2.202734839476814,
    'obs_i':1.073127229488705,
}

m.systemize()
s0 = m._variants[0]._system

m.change_logly(True, ["c"])
m.systemize()
s1 = m._variants[0]._system


v = m._system_vectors
qid_to_name = m.create_qid_to_name()

def assertion(s0, derivative):
    if s0 == derivative:
        pass
    if s0 != derivative:
        assert abs(s0-derivative) < 0.0000001

def test_derivatives0(s0, asgn):
    """
    Token(qid=8, shift=2)
    x{+2}
    """
    derivatives = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0.1
]
    for i in range(len(derivatives)):
       assertion(list(s0.A[i])[0], derivatives[i])

def test_derivatives1(s0, asgn):
    """
    Token(qid=2, shift=1)
    c{+1}
    """
    derivatives = [
    asgn['beta']*asgn['r'],
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
]
    for i in range(len(derivatives)):
        assertion(list(s0.A[i])[1], derivatives[i])

def test_derivatives2(s0, asgn):
    """
    Token(qid=8, shift=1)
    x{+1}
    """
    derivatives = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0.2
]
    for i in range(len(derivatives)):
        assertion(list(s0.A[i])[2], derivatives[i])

def test_derivatives3(s0, asgn):
    """
    Token(qid=0, shift=0)
    a
    """
    derivatives = [
    0,
    0,
    (asgn['gamma']-1)*(-asgn['a']**-asgn['gamma'])*asgn['k']**asgn['gamma'],
    0,
    0,
    -(1/asgn['a']),
    0,
    0,
    0,
]
    for i in range(len(derivatives)):
        assertion(list(s0.A[i])[3], derivatives[i])

def test_derivatives4(s0, asgn):
    """
    Token(qid=1, shift=0)
    y
    """
    derivatives = [
    0,
    0,
    -1,
    -(asgn['gamma']),
    -1,
    0,
    -(asgn['c']/asgn['y']**2),
    -0.1,
    0,
]

    for i in range(len(derivatives)):
        assertion(list(s0.A[i])[4], derivatives[i])

def test_derivatives5(s0, asgn):
    """
    Token(qid=2, shift=0)
    c
    """
    derivatives = [
    -1,
    0,
    0,
    0,
    1,
    0,
    1/asgn['y'],
    0,
    0,
]

    for i in range(len(derivatives)):
        assertion(list(s0.A[i])[5], derivatives[i])

def test_derivatives6(s0, asgn):
    """
    Token(qid=3, shift=0)
    i
    """
    derivatives = [
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    1/asgn['y'],
    0
]

    for i in range(len(derivatives)):
        assertion(list(s0.A[i])[6], derivatives[i])

def test_derivatives7(s0, asgn):
    """
    Token(qid=4, shift=0)
    k
    """
    derivatives = [
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
    for i in range(len(derivatives)):
        assertion(list(s0.A[i])[7], derivatives[i])

def test_derivatives8(s0, asgn):
    """
    Token(qid=5, shift=0)
    r
    """
    derivatives = [
    asgn['beta']*asgn['c'],
    0,
    0,
    asgn['k'],
    0,
    0,
    0,
    0,
    0
]
    for i in range(len(derivatives)):
        assertion(list(s0.A[i])[8], derivatives[i])

def test_derivatives9(s0, asgn):
    """
    Token(qid=6, shift=0)
    c_to_y
    """
    derivatives = [
    0,
    0,
    0,
    0,
    0,
    0,
    -1,
    0,
    0
]
    for i in range(len(derivatives)):
        assertion(list(s0.A[i])[9], derivatives[i])

def test_derivatives10(s0, asgn):
    """
    Token(qid=7, shift=0):
    i_to_y
    """
    derivatives = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    -1,
    0
]
    for i in range(len(derivatives)):
        assertion(list(s0.A[i])[10], derivatives[i])

def test_derivatives11(s0, asgn):
    """
    Token(qid=8, shift=0)
    x
    """
    derivatives = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    -1
]
    for i in range(len(derivatives)):
        assertion(list(s0.A[i])[11], derivatives[i])

def test_derivatives12(s0, asgn):
    """
    Token(qid=8, shift=-1)
    x{-1}
    """
    derivatives = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0.2
]
    for i in range(len(derivatives)):
        assertion(list(s0.A[i])[12], derivatives[i])

if __name__ == '__main__':
    test_derivatives0(s0, asgn)
    test_derivatives1(s0, asgn)
    test_derivatives2(s0, asgn)
    test_derivatives3(s0, asgn)
    test_derivatives4(s0, asgn)
    test_derivatives5(s0, asgn)
    test_derivatives6(s0, asgn)
    test_derivatives7(s0, asgn)
    test_derivatives8(s0, asgn)
    test_derivatives9(s0, asgn)
    test_derivatives10(s0, asgn)
    test_derivatives11(s0, asgn)
    test_derivatives12(s0, asgn)
