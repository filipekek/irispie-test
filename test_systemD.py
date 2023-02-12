
import sys
sys.path.append('..')

import modiphy as md
import numpy
from math import exp

numpy.set_printoptions(linewidth=100000)

s = md.Source.from_lists(
    transition_variables=["a", "y", "c", "i", "k", "r", "c_to_y", "i_to_y", "x"],
    measurement_variables=["obs_c", "obs_y", "obs_i"],
    parameters=["ss_a", "rho", "beta", "gamma", "delta"],
    transition_shocks=["shock_a", "shock_b", "shock_c"],
    measurement_shocks=["shock_obs_i", "shock_obs_c"],
    transition_equations=[
        "c = beta*r*c{+1}*shock_a",
        "k = (1 - delta)*k{-1} + i*shock_c",
        "y = a^(1-gamma) * k{-1}^gamma + exp(shock_b)",
        "gamma*y = k{-1} * (r - 1 + delta) + exp(2*shock_b)",
        "y = i + c + shock_b^2",
        "log(a) = rho*log(a{-1}) + (1 - rho)*log(ss_a) + shock_a",
        "c_to_y = c / y",
        "i_to_y = i / y",
        "x = 0.2*x{-1} + 0.1*x{-2} + 0.2*x{+1} + 0.1*x{+2} + (1-0.6)*4 + r*shock_c",
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

def loop(s0, derivatives, num):
#    x = 0
    for i in range(len(derivatives)):
#        print(x)
#        x += 1
        assertion(list(s0.D[i])[num], derivatives[i])

def test_derivatives0(s0, asgn):
    derivatives = [
    asgn['beta']*asgn['r']*asgn['c'],
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0
]
    loop(s0, derivatives, 0)

def test_derivatives1(s0, asgn):
    derivatives = [
    0,
    0,
    1,
    2,
    0,
    0,
    0,
    0,
    0,
]
    loop(s0, derivatives, 1)

def test_derivatives2(s0, asgn):
    derivatives = [
    0,
    asgn['i'],
    0,
    0,
    0,
    0,
    0,
    0,
    asgn['r']
]
    loop(s0, derivatives, 2)
