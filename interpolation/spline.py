import numpy as np
from scipy.interpolate import CubicSpline

def spline(x, y):
    cs = CubicSpline(np.array(x, dtype=np.float), np.array(y, dtype=np.float), bc_type='natural')
    result = np.rot90(cs.c, 3)

    for i, line in enumerate(result):
        a = 97
        for j, column in enumerate(line):
            print(f'{chr(a+j)}{i} = {column:.14f}')