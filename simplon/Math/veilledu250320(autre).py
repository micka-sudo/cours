import numpy as np
import scipy.optimize as spo

def func(x) :
    return 2*x[0] + x[1]

def func_deriv(x):
    dfdx = 2
    dfdy = 1
    return np.array([dfdx, dfdy])

cons = ({'type': 'ineq',
          'fun' : lambda x: np.array([x[0] - x[1] + 1]),
          'jac' : lambda x: np.array([1.0, -1.0])},
        {'type': 'ineq',
          'fun' : lambda x: np.array([x[0] + x[1] - 2]),
          'jac' : lambda x: np.array([1.0, 1.0])},
        {'type': 'ineq',
          'fun' : lambda x: np.array([x[1]]),
          'jac' : lambda x: np.array([0.0, 1.0])},
        {'type': 'ineq',
          'fun' : lambda x: np.array([4 - x[0] + 2*x[1]]),
          'jac' : lambda x: np.array([-1.0, 2.0])}
          )

#res = spo.minimize(func, [-1.0,1.0], jac=func_deriv,
#                    method='SLSQP', options={'disp': True})

res = spo.minimize(func, [-1.0,1.0], jac=func_deriv,
                constraints=cons, method='SLSQP', options={'disp': True})

print(res.x)