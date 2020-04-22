import numpy as np

class Solver:
    def __init__(self, options):
        h = options.h
        tau = options.tau
        n = options.n
        self.h = h
        self.N = int(tau / h) + 1
        self.n = n
        self.t = np.arange(-tau, h, h)
        self.x = np.zeros((n, self.N))
        self.y = np.zeros((n, self.N))
        self.mu = options.mu
        self.g = options.g
        self.L = options.L
        self.a = options.a
        self.q = options.q
        self.l = options.l
        self.vmax = options.vmax
        self.vmin = options.vmin

        self.timer = options.timer

        for i in range(n):
            for j in range(self.N):
                self.x[i, j] = options.lambd0 - i * options.lambd
        for i in range(n):
            for j in range(self.N):
                self.y[i, j] = 0

    def R(self, x, y, n):

        l = ((y[n, -1] ** 2) / (2 * 0.6 * 9.8)) + 5

        if n == 0:
            if self.L - x[n, -1] > l:
                return True
            else:
                return False
        else:
            if x[n - 1, -self.N] - x[n, -1] > l:
                return True
            else:
                return False

    def F(self, x, y, n):
        return y[n, -1]

    def G(self, x, y, n):

        if n == 0:
            if self.R(x, y, n):
                return self.a * (self.vmax - y[n, -1])
            else:
                speed = ((y[n, -1]** 2 *(self.vmin - y[n, -1]))/(self.L-x[n, -1]-self.l)**2)
        else:
            if self.R(x, y, n):

                speed = self.a * (y[n - 1, -self.N] - y[n, -1])
            else:
                speed = ((y[n, -1]** 2 *(y[n - 1, -self.N] - y[n, -1]))/(x[n - 1, -self.N]-x[n, -1]-self.l+1)**2)

        if (speed > self.vmax):
            return self.vmax
        elif (speed < -self.vmax):
            return -self.vmax
        else:
            return speed

    def solve(self):
        for i in range(1000):
            row1 = np.zeros((self.n, 1))
            row2 = np.zeros((self.n, 1))
            for j in range(self.n):
                row1[j, 0] = self.x[j, -1] + self.h * self.F(self.x, self.y, j)
                row2[j, 0] = self.y[j, -1] + self.h * self.G(self.x, self.y, j)
            self.t = np.append(self.t, self.t[-1] + self.h)
            self.x = np.append(self.x, row1, axis=1)
            self.y = np.append(self.y, row2, axis=1)
        return self.t, self.x, self.y