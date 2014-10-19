import numpy as np
from common.kernels import dot
from random import randint

def smo(C, tol, max_passes, pts, kernel=dot):
    a = np.array(pts)
    b = 0
    passes = 0
    while passes < max_passes:
        num_changes_alpha = 0
        for i in range(len(pts)):
            cur_p = pts[i]
            err_i = calc_e(cur_p, a, b, pts, kernel)
            if (cur_p.class_id * err_i < -tol and a[i] < C) or (cur_p.class_id * err_i > tol and a[i] > 0):
                j = i
                while i == j:
                    j = randint(0, len(pts) - 1)
                err_j = calc_e(pts[j], a, b, pts)
                a_old_i, a_old_j = a[i], a[j]
                l, h = calc_lh(i, j, pts, a, C)
                if l == h:
                    continue
                n = calc_n()
                if n >= 0:
                    continue

                a[j] -= pts[j].class_id * (err_i - err_j) / n
                a[j] = min(h, max(l, a[j]))
                if abs(a[j] - a_old_j) < 1e-5:
                    continue
                a[i] += a[i].class_id * a[j].class_id * (a_old_j -  a[j])
                b_help = b - a[i].class_id * (a[i] - a_old_i) * kernel(pts[i], pts[i]) - a[j].class_id * (a[j] - a_old_j) * kernel(pts[j], pts[j])
                b1, b2 = b_help - err_i, b_help - err_j
                if 0 < a[i] and a[i] < C:
                    b = b1
                elif 0 < a[j] and a[j] < C:
                    b = b2
                else:
                    b = (b1 + b2) / 2
                num_changes_alpha += 1

        if num_changes_alpha == 0:
            passes += 1
        else:
            passes = 0
    return a, b


def calc_n(x_i, x_j, kernel):
    return 2 * kernel(x_i, x_j) - kernel(x_i, x_j) - kernel(x_j, x_j)


def calc_e(x, a, b, pts, kernel):
    return calc_f(x, a, b, pts, kernel) - x.class_id


def calc_lh(i, j, pts, a, c):
    if pts[i].class_id != pts[j].class_id:
        return max(0, a[j] - a[i]), min(c, c + a[j] - a[i])
    else:
        return max(0, a[i] + a[j] - c), min(c, a[i] + a[j]);


def calc_f(x, a, b, pts, kernel):
    res = b
    for i in range(len(a)):
        res += a[i] * pts[i].class_id * kernel(x, pts[i])
    return res


