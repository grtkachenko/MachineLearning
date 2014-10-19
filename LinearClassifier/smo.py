from random import randint

from common.kernels import dot


class Smo:
    def __init__(self, c, tol, max_passes, kernel=dot):
        self.c = c
        self.tol = tol
        self.max_passes = max_passes
        self.kernel = kernel
    
    def minimize(self, pts):
        for p in pts:
            p.class_id = -1 if p.class_id == 0 else 1
        a = [0] * len(pts)
        b = 0
        passes = 0
        while passes < self.max_passes:
            num_changes_alpha = 0
            for i in range(len(pts)):
                cur_p = pts[i]
                err_i = self.__calc_e__(cur_p, a, b, pts)
                if (cur_p.class_id * err_i < -self.tol and a[i] < self.c) or (cur_p.class_id * err_i > self.tol and a[i] > 0):
                    j = i
                    while i == j:
                        j = randint(0, len(pts) - 1)
                    err_j = self.__calc_e__(pts[j], a, b, pts)
                    a_old_i, a_old_j = a[i], a[j]
                    l, h = self.__calc_lh__(i, j, pts, a)
                    if l == h:
                        continue
                    n = self.__calc_n__(pts[i], pts[j])
                    if n >= 0:
                        continue
    
                    a[j] -= pts[j].class_id * (err_i - err_j) / n
                    a[j] = min(h, max(l, a[j]))
                    if abs(a[j] - a_old_j) < 1e-5:
                        continue
                    a[i] += pts[i].class_id * pts[j].class_id * (a_old_j - a[j])
                    b_help = b - pts[i].class_id * (a[i] - a_old_i) * self.kernel(pts[i], pts[i]) - pts[j].class_id * (a[j] - a_old_j) * self.kernel(pts[j], pts[j])
                    b1, b2 = b_help - err_i, b_help - err_j
                    if 0 < a[i] < self.c:
                        b = b1
                    elif 0 < a[j] < self.c:
                        b = b2
                    else:
                        b = (b1 + b2) / 2
                    num_changes_alpha += 1
    
            if num_changes_alpha == 0:
                passes += 1
            else:
                passes = 0
        for p in pts:
            p.class_id = 0 if p.class_id == -1 else 1

        return a, b
    
    def __calc_n__(self, x_i, x_j):
        return 2 * self.kernel(x_i, x_j) - self.kernel(x_i, x_i) - self.kernel(x_j, x_j)
    
    def __calc_e__(self, x, a, b, pts):
        return self.__calc_f__(x, a, b, pts) - x.class_id
    
    def __calc_lh__(self, i, j, pts, a):
        if pts[i].class_id != pts[j].class_id:
            return max(0, a[j] - a[i]), min(self.c, self.c + a[j] - a[i])
        else:
            return max(0, a[i] + a[j] - self.c), min(self.c, a[i] + a[j])
    
    def __calc_f__(self, x, a, b, pts):
        res = b
        for i in range(len(a)):
            res += a[i] * pts[i].class_id * self.kernel(x, pts[i])
        return res
