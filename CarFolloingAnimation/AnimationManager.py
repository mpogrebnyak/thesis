import numpy as np
from DrawCarHelper import drawCar
from Solver import Solver
from OptionsModel import Options
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AnimationTypes(object):
    animateSpeed = 'animateSpeed'
    animateDistance = 'animateDistance'

class Animation(object):
    def __init__(self, figure, ax, animationType=None):
        self.calculate()

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

    def calculate(self):
        self.options = Options()
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

        def init():
            for index in range(self.options.n):
                self.cars[index].set_data(x[index, 0]-24, 1)

        def animate(time):
            for index in range(self.options.n):
                self.cars[index].set_data(x[index, time]-24, 1)
                #self.createAnnotate(index, x[index, 0] - 24, y[index, 0], x[index, 0])


        return animation.FuncAnimation(self.figure, animate, init_func=init, frames=1000, interval=1, repeat=False)

    def initCars(self):
        t, x, y = self.t, self.x, self.y

        for index in range(self.options.n):
            self.cars[index].set_data(x[index, 0]-24, 1)
            self.createAnnotate(index, x[index, 0]-24, y[index, 0],  x[index, 0])

    def createAnnotate(self, number, x, speed, distance):
        y = 1.5
        if (number % 2 == 0):
            y = 0.5
        return self.ax.annotate("car " + str(number+1) + ": \n V = " + str(speed) + "\n S =" + str(distance),
                          xy=(x, 1), xycoords='data',
                          xytext=(5+x, y), textcoords='data',
                          size=8, va="center", ha="center",
                          bbox=dict(boxstyle="round4", fc="w"),
                          arrowprops=dict(arrowstyle="-|>",
                                          connectionstyle="arc3,rad=-0.2",
                                          fc="w"),)

