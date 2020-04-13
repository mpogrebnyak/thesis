from Solver import Solver
from OptionsModel import Options

import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AnimationTypes(object):
    animateSpeed = 'animateSpeed'
    animateDistance = 'animateDistance'

class Animation(object):
    def __init__(self, animationType):
        self.animationType = animationType

        self.figure = plt.figure()
        ax = plt.axes(xlim=(0, 1000), ylim=(-1, 20))

        self.lines = []
        self.xdata = []
        self.ydata = []

        for i in range(Options.n):
            line, = ax.plot([], [], lw=2)
            self.lines.append(line)
            self.xdata.append([])
            self.ydata.append([])

    def animate(self):
        options = Options()
        sol = Solver(options)

        t, x, y = sol.solve()

        def init():
            for index in range(options.n):
                self.lines[index].set_data([], [])

        def animate(time):
            for index in range(options.n):
                self.xdata[index].append(time)

                if self.animationType == AnimationTypes.animateSpeed:
                    self.ydata[index].append(y[index, time])
                if self.animationType == AnimationTypes.animateDistance:
                    self.ydata[index].append(x[index, time])

                self.lines[index].set_data(self.xdata[index], self.ydata[index])

        anim = animation.FuncAnimation(self.figure, animate, init_func=init, frames=1000, interval=20, repeat=False)

        plt.show()