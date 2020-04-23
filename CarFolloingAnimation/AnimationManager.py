import numpy as np
from DrawCarHelper import drawCar
from Solver import Solver
from OptionsModel import Options
from OptionsModel import Mode
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AnimationTypes(object):
    animateSpeed = 'animateSpeed'
    animateDistance = 'animateDistance'

class Animation(object):
    def __init__(self, figure, ax, options, animationType=None):
        self.calculate(options)

        self.animationType = animationType

        self.figure = figure
        self.ax = ax

        self.lines = []
        self.xdata = []
        self.ydata = []

        self.cars = []

        cmap = plt.get_cmap('hsv')
        colors = [cmap(i) for i in np.linspace(0, 1, Options.n)]
        carIm = drawCar()
        for i in range(Options.n):
            line, = self.ax.plot([], [], lw=2, color=colors[i])
            self.lines.append(line)
            self.xdata.append([])
            self.ydata.append([])

            car, = plt.plot([], [], marker=carIm, lw=2, color=colors[i], markersize=20)
            self.cars.append(car)

    def calculate(self, options):
        self.options = options
        sol = Solver(self.options)
        self.t, self.x, self.y = sol.solve()

    def animate(self):
        t, x, y = self.t, self.x, self.y

        def init():
            for index in range(self.options.n):
                self.lines[index].set_data([], [])

        def animate(time):

            for index in range(self.options.n):
                self.xdata[index].append(t[time])

                if self.animationType == AnimationTypes.animateSpeed:
                    self.ydata[index].append(y[index, time])
                if self.animationType == AnimationTypes.animateDistance:
                    self.ydata[index].append(x[index, time])

                self.lines[index].set_data(self.xdata[index], self.ydata[index])

        return animation.FuncAnimation(self.figure, animate, init_func=init, frames=1000, interval=1, repeat=False)


    def animateCars(self):
        t, x, y = self.t, self.x, self.y

        self.annotate= []
        self.currentTime = -self.options.tau
        self.prevTime = 0
        def init():
            self.timeAnnotate = self.createTimeAnnotate(t[0])

            if (self.options.mode == Mode.secondMode):
                self.timer = self.createTimer(self.options.timer, True)

            for index in range(self.options.n):
                self.cars[index].set_data(x[index, 0]-3.5, 1)
                self.annotate.append(self.createAnnotate(index, x[index, 0]-3.5, y[index, 0],  x[index, 0]))

        def animate(time):
            self.timeAnnotate.remove()
            self.timeAnnotate = self.createTimeAnnotate(t[time])

            if (self.options.mode == Mode.secondMode):
                self.timeRound(t[time])
                self.timer.remove()
                if self.currentTime >= 0:
                    self.timer = self.createTimer(self.options.timer-self.currentTime, True)
                else:
                    self.timer = self.createTimer(-self.currentTime, False)

            for index in range(self.options.n):
                self.cars[index].set_data(x[index, time]-3.5, 1)
                self.annotate[index].remove()
                self.annotate[index] = self.createAnnotate(index, x[index, time]-3.5, y[index, time], x[index, time])


        return animation.FuncAnimation(self.figure, animate, init_func=init, frames=1000, interval=1, repeat=False)

    def initCars(self):
        t, x, y = self.t, self.x, self.y
        self.createTimeAnnotate(t[0])

        if (self.options.mode == Mode.secondMode):
            self.timer = self.createTimer(self.options.timer, True)

        for index in range(self.options.n):
            self.cars[index].set_data(x[index, 0]-3.5, 1)
            self.ann = self.createAnnotate(index, x[index, 0]-3.5, y[index, 0],  x[index, 0])


    def createTimeAnnotate(self, time):

        return self.ax.annotate(
            "Время:\n " + str(round(time+Options.tau,0)),
            xy=(0, 1), xycoords='data',
            xytext=(0, 1.8), textcoords='data',
            size=10, va="center", ha="center",
            bbox=dict(boxstyle="round4", fc="w"),
           )

    def createTimer(self, time, move):
        color = "r"
        if move:
            color = "g"

        return self.ax.annotate(
            "Время:\n " + str(round(time, 0)),
            xy=(0, 1), xycoords='data',
            xytext=(0, 0.2), textcoords='data',
            size=10, va="center", ha="center",
            bbox=dict(boxstyle="round4", fc=color, ec=color),

        )

    def createAnnotate(self, number, x, speed, distance):
        y = 1.35
        if (number % 2 == 0):
            y = 0.65

        return self.ax.annotate("car " + str(number+1) + ": \n V = " + str(round(speed,1)) + "\n S =" + str(int(round(distance,0))),
                          xy=(x, 1), xycoords='data',
                          xytext=(5+x, y), textcoords='data',
                          size=8, va="center", ha="center",
                          bbox=dict(boxstyle="round4", fc="w"),
                          arrowprops=dict(arrowstyle="-|>",
                                          connectionstyle="arc3,rad=-0.2",
                                          fc="w"),)

    def timeRound(self, time):
        t = round(time, 0)

        if t > self.prevTime:
            self.currentTime = self.currentTime + 1
            self.prevTime = t

        if self.currentTime == self.options.timer:
            self.currentTime = -self.options.stopTime