
import sys
sys.path.append("/home/filip")

from modiphy import diff_single

from math import log
import random

first_expression = lambda x, y, z: log(x)*12+38*y-3+z**2
first_exp_str = "log(x)*12+38*y-3+z**2"
first_exp_x = lambda x, y, z: 12/x
first_exp_y = lambda x, y, z: 38
first_exp_z = lambda x, y, z: 2*z
tolerated = 1e-8

second_expression = lambda x, y, z: x**4+382-2*log(y+3)/6*z
second_exp_str = "x**4+382-2*log(y+3)/6*z"
second_exp_x = lambda x, y, z: 4*x**3
second_exp_y = lambda x, y, z: z/(3*(y+3))
second_exp_z = lambda x, y, z: -(log(y+3))/3


def toleration(x, y, tolerated):
    difference = abs(x-y)
    assert difference < tolerated

def test_act(expression, str_exp, exp_x, exp_y, exp_z, tolerated):
    """
    Test for results from 'diff_single' from modiphy

    input:
    Mathematical expression of 3 unknowns
    str of expression

    Derivation of x
    Derivation of y
    Derivation of z

    Tolerated difference of 2 results (act and manual expression)
    """

    for _ in range(10):
        values = {"x": random.uniform(1, 10), "y": random.uniform(1, 50), "z": random.uniform(1,20)}
        inputs = [values["x"], values["y"], values["z"]]

        exp_result = expression(*inputs)
        exp_x_result = exp_x(*inputs)
        exp_y_result = exp_y(*inputs)
        exp_z_result = exp_z(*inputs)

        act, *_ = diff_single(str_exp, ["x", "y", "z"], values)

        act = list(act[:,0])

        results = [exp_x_result, exp_y_result, exp_z_result]

        [ toleration(*i, tolerated) for i in zip(act, results) ]

