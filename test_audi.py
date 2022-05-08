
import sys
sys.path.append("/home/filip")

from modiphy import diff_single

from math import log
import random


def toleration(x, y, tolerated):
    difference = abs(x-y)
    assert difference < tolerated
#
#def test_act(str_exp, exp_x, exp_y, exp_z):
#    """
#    Test for results from 'diff_single' from modiphy
#
#    input:
#    str of mathematical expression of 3 unknowns
#
#    Derivation of x
#    Derivation of y
#    Derivation of z
#    """
#
#    tolerated = 1e-8
#
#    for _ in range(10):
#        values = {"x": random.uniform(1, 10), "y": random.uniform(1, 50), "z": random.uniform(1,20)}
#        inputs = [values["x"], values["y"], values["z"]]
#
##        exp_result = expression(*inputs)
#        exp_x_result = exp_x(*inputs)
#        exp_y_result = exp_y(*inputs)
#        exp_z_result = exp_z(*inputs)
#
#        act, *_ = diff_single(str_exp, ["x", "y", "z"], values)
#
#        act = list(act[:,0])
#
#        results = [exp_x_result, exp_y_result, exp_z_result]
#
#        [ toleration(*i, tolerated) for i in zip(act, results) ]
#
#
#
##first_expression = lambda x, y, z: log(x)*12+38*y-3+z**2
##first_exp_str = "log(x)*12+38*y-3+z**2"
##first_exp_x = lambda x, y, z: 12/x
##first_exp_y = lambda x, y, z: 38
##first_exp_z = lambda x, y, z: 2*z
##tolerated = 1e-8
#
#first = test_act(
#"log(x)*12+38*y-3+z**2",
#lambda x, y, z: 12/x,
#lambda x, y, z: 38,
#lambda x, y, z: 2*z)
#
##!!
##second_expression = lambda x, y, z: x**4+382-2*log(y+3)/6*z
##second_exp_str = "x**4+382-2*log(y+3)/6*z"
##second_exp_x = lambda x, y, z: 4*x**3
##second_exp_y = lambda x, y, z: z/(3*(y+3))
##second_exp_z = lambda x, y, z: -(log(y+3))/3
##!!
#
##test_act(
##"x**4+382-2*log(y+3)/6*z",
##lambda x, y, z: 4*x**3,
##lambda x, y, z: z/(3*(y+3)),
##lambda x, y, z: -(log(y+3))/3)
#
#
##third_expression = lambda x, y, z: 1
##third_exp_str = lambda x, y, z: "1"
##third_exp_x = lambda x, y, z: 0
##third_exp_y = lambda x, y, z: 0
##third_exp_z = lambda x, y, z: 0
#
#
##third_expression = lambda x, y, z: 1
#third_exp_str = lambda x, y, z: "x*0"
#third_exp_x = lambda x, y, z: 0
#third_exp_y = lambda x, y, z: 0
#third_exp_z = lambda x, y, z: 0

#========================================================================================

#def test_act_more_values(str_exp, exp_x, exp_y, exp_z):
#    tolerated = 1e-8

#    for testing in range(100):
values = {"x": random.sample(range(1, 10), 3), "y": random.sample(range(1, 10000), 3), "z": random.sample(range(1,1000), 3)}
print(values)
act, *_ = diff_single("x**4+382-2*log(y+3)/6*z", ["x", "y", "z"], values)
print(act)
