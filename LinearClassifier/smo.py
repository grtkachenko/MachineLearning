import numpy as np
from common.kernels import dot

def smo(C, tol, max_passes, pts, kernel=dot):
    a = np.array(pts)
    b = 0
    return a, b