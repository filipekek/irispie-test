import sys
sys.path.append("/home/filip")

from modiphy import diff_single

from math import log

#x**5*log(y)+83-z**3

f = lambda x, y, z: x**5*log(y)+83-z**3

fx = lambda x, y, z: 5*x**4 * log(y)

fy = lambda x, y, z: 1/y * x**5

fz = lambda x, y, z: -3*z**2

xyz_values = {'x': 3, 'y': 12, 'z': 23}
xyz_inputs = [xyz_values['x'], xyz_values['y'], xyz_values['z']]

def counting_f(f, fx, fy, fz, xyz_values, xyz_inputs):
    f_result = f(*xyz_inputs)
    fx_result = fx(*xyz_inputs)
    fy_result = fy(*xyz_inputs)
    fz_result = fz(*xyz_inputs)

    xp = xyz_values['x'] + 1e-6
    xm = xyz_values['x'] - 1e-6
    f_xp = f(xp, *xyz_inputs[1:3])
    f_xm = f(xm, *xyz_inputs[1:3])
    fx_num = (f_xp-f_xm)/(xp-xm)

    yp = xyz_values['y'] + 1e-6
    ym = xyz_values['y'] - 1e-6
    f_yp = f(xyz_inputs[0], yp, xyz_inputs[2])
    f_ym = f(xyz_inputs[0], ym, xyz_inputs[2])
    fy_num = (f_yp-f_ym)/(yp-ym)

    zp = xyz_values['z'] + 1e-6
    zm = xyz_values['z'] - 1e-6
    f_zp = f(*xyz_inputs[0:2], zp)
    f_zm = f(*xyz_inputs[0:2], zm)
    fz_num = (f_zp-f_zm)/(zp-zm)

    return f_result, fx_result, fy_result, fz_result, fx_result-fx_num, fy_result-fy_num, fz_result-fz_num

x, *_ = diff_single("3*x^2+y", ["x", "y"], {"x": 3, "y": 21.5})
print(x)
