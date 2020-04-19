from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from AnimationManager import *
from tkinter import *
import matplotlib.pyplot as plt

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

        self.initEmpty(master)
        self.initGrid()
        self.initSpeedDiagram()
        self.initDistanceDiagram()
        self.initCarAnimation()
        self.initCars()

    def Start(self):
        self.initSpeedDiagram()
        self.initDistanceDiagram()
        self.initCarAnimation()

        self.startAnimate()

    #def Stop(self):
    #    self.isStartApp = False
    #    self.startAnimate()


    def initEmpty(self, master):
        self.master.title("Title")
        self.pack(fill='both', expand=1)

    def initGrid(self):
        self.mainLable = Label(self, text="Application").grid(row=0, column=1, columnspan=2)
        self.startButton = Button(self, text="Start", command=self.Start,  width=12).grid(row=1, column=0, columnspan=2)
    #   self.stopButton = Button(self, text="Stop", command=self.Stop, width=12).grid(row=2, column=0, columnspan=2)

    def initCarAnimation(self):
        self.figureC = plt.figure(figsize=(8, 3))
        self.axC = plt.axes([0.01,0.1,0.96,1],xlim=(-200, 1000), ylim=(0, 2))
        self.axC.spines['top'].set_visible(False)
        self.axC.spines['right'].set_visible(False)
        self.axC.spines['left'].set_visible(False)
        self.axC.get_yaxis().set_ticks([])

        self.axC.vlines(0, 0, 2, color = 'r')
        self.axC.vlines(200, 0, 2, color='r')
        self.axC.hlines(0.5, -200, 1000)

        self.canvas = FigureCanvasTkAgg(self.figureC, master=self)
        self.canvas.get_tk_widget().grid(column=3, row=0, columnspan=8, rowspan=6)

    def initCars(self):
        init = Animation(self.figureC, self.axC)
        init.initCars()

    def initSpeedDiagram(self):
        self.figureS = plt.figure(figsize=(4,3))
        self.axS = plt.axes(xlim=(0, 100), ylim=(-1, 20))

        self.canvas = FigureCanvasTkAgg(self.figureS, master=self)
        self.canvas.get_tk_widget().grid(column=3, row=7)

    def initDistanceDiagram(self):
        self.figureD = plt.figure(figsize=(4,3))
        self.axD = plt.axes(xlim=(0, 100), ylim=(0, 1400))

        self.canvas = FigureCanvasTkAgg(self.figureD, master=self)
        self.canvas.get_tk_widget().grid(column=4, row=7)

    def startAnimate(self):
        distanceAnimation = Animation(self.figureD, self.axD, AnimationTypes.animateDistance)
        self.animD = distanceAnimation.animate()

        speedAnimation = Animation(self.figureS, self.axS, AnimationTypes.animateSpeed)
        self.animS = speedAnimation.animate()

        carAnimation = Animation(self.figureC, self.axC)
        self.animC = carAnimation.animateCars()