import numpy as np
from OptionsModel import Mode

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

        self.mode = options.mode

        if(self.mode == Mode.secondMode):
            self.prevTime = 0
            self.timerValue = options.timer
            self.stopTime = options.stopTime
            self.firstCars = []
            self.firstCars.append(0)
            self.currentTime = 0

        if (self.mode == Mode.thirdMode):
            self.prevTimeF = 0
            self.prevTimeS = 0
            self.timerValueF = options.timerF
            self.timerValueS = options.timerS
            self.stopTimeF = options.stopTimeF
            self.stopTimeS = options.stopTimeS

            self.firstCarsF = []
            self.firstCarsF.append(0)
            self.firstCarsS = []
            self.firstCarsS.append(0)
            self.currentTime = 0

        for i in range(n):
            for j in range(self.N):
                self.x[i, j] = options.lambd0 - i * options.lambd
        for i in range(n):
            for j in range(self.N):
                self.y[i, j] = 0

    def R(self, x, y, n):

        l = ((y[n, -1] ** 2) / (2 * 0.6 * 9.8)) + 5
        if self.mode == Mode.firstMode:
            if n==0:
                if self.L - x[n, -1] > l:
                    return True
                else:
                    return False
            else:
                if x[n - 1, -self.N] - x[n, -1] > l:
                    return True
                else:
                    return False
        elif self.mode == Mode.secondMode:
            if self.firstCars.__contains__(n):
                L = 5000
                if self.currentTime < 0 and self.firstCars[-1] == n:
                    L = 0

                if L - x[n, -1] > l:
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
        speed = 0
        if self.mode == Mode.firstMode:
            if n == 0:
                if self.R(x, y, n):
                    return self.a * (self.vmax - y[n, -1])
                else:
                    speed = ((y[n, -1]** 2 *(self.vmin - y[n, -1]))/(self.L-x[n, -1])**2)
            else:
                if self.R(x, y, n):
                    speed = self.a * (y[n - 1, -self.N] - y[n, -1])
                else:
                    speed = ((y[n, -1]** 2 *(y[n - 1, -self.N] - y[n, -1]))/(x[n - 1, -self.N]-x[n, -1]-self.l+1)**2)
        elif self.mode == Mode.secondMode:
            L = 5000
            if self.currentTime < 0:
                L = 0

            if self.firstCars.__contains__(n):
                if self.R(x, y, n):
                    return self.a * (self.vmax - y[n, -1])
                else:
                    speed = ((y[n, -1] ** 2 * (self.vmin - y[n, -1])) / (L - x[n, -1]) ** 2)
            else:
                if self.R(x, y, n):
                    speed = self.a * (y[n - 1, -self.N] - y[n, -1])
                else:
                    speed = ((y[n, -1] ** 2 * (y[n - 1, -self.N] - y[n, -1])) / (
                                x[n - 1, -self.N] - x[n, -1] - self.l + 1) ** 2)

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

            if (self.mode == Mode.secondMode):
                self.timeRound(self.t[-1])
                if (self.isTimerEnd(self.timerValue, self.stopTime)):
                    for c in range(self.n):
                        if(self.x[c, i] < - 16): #(self.y[c, i]**2/2*self.g*self.mu )
                            if self.firstCars.__contains__(c):
                                break
                            self.firstCars.append(c)
                            break

            if (self.mode == Mode.thirdMode):
                self.timeRound(self.t[-1])
                if (self.isTimerEnd(0,0)):
                    for c in range(self.n):
                        if(self.x[c, i] < - 16): #(self.y[c, i]**2/2*self.g*self.mu )
                            if self.firstCars.__contains__(c):
                                break
                            self.firstCars.append(c)
                            break

        return self.t, self.x, self.y

    #def isTimerEnd(self):
     #   if self.currentTime == self.timerValue:
      #      self.currentTime = -self.stopTime
       #     return True

        #return False

    def isTimerEnd(self, timerValue, stopTime):
        if self.currentTime == timerValue:
            self.currentTime = -stopTime
            return True

        return False

    def timeRound(self, time):
        t = round(time, 0)

        if t > self.prevTime:
            self.currentTime = self.currentTime + 1
            self.prevTime = t

