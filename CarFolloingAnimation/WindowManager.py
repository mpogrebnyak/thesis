from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from AnimationManager import *
from OptionsModel import Options
from OptionsModel import Mode
from tkinter import *
import matplotlib.pyplot as plt
from tkinter import ttk


class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

        self.options = Options

        self.initEmpty(master)
        self.initGrid()
        self.initSpeedDiagram()
        self.initDistanceDiagram()
        self.initCarAnimation()
        self.initCars()

    def start(self):
        self.initSpeedDiagram()
        self.initDistanceDiagram()
        self.initCarAnimation()

        self.startAnimate()

    def applyChanging(self):
        if self.var.get() == Mode.firstMode:
            self.options.mode = Mode.firstMode
        elif self.var.get() == Mode.secondMode:
            self.options.mode = Mode.secondMode
        elif self.var.get() == Mode.thirdMode:
            self.options.mode = Mode.thirdMode

        self.options.n = self.n.get()
        self.options.L = self.L.get()
        self.options.vmax = self.vmax.get()
        self.options.vmin = self.vmin.get()

        self.initSpeedDiagram()
        self.initDistanceDiagram()
        self.initCarAnimation()
        self.initCars()

    def clear(self):
        self.options.n = 30
        self.options.L = 1000
        self.options.vmax = 16.7
        self.options.vmin = 0

        self.n.set(30)
        self.L.set(1000)
        self.vmax.set(16.7)
        self.vmin.set(0)

        self.initSpeedDiagram()
        self.initDistanceDiagram()
        self.initCarAnimation()
        self.initCars()

    def initEmpty(self, master):
        self.master.title("Title")

        self.config(bg='white')
        self.style = ttk.Style()
        self.style.theme_use("vista")

        ttk.Style().configure('TLabel', foreground='black', background='white', font="Arial 10")
        ttk.Style().configure('TButton', foreground='black', background='white', font="Arial 12")
        ttk.Style().configure('TRadiobutton', foreground='black', background='white', font="Arial 12")

        self.pack(fill='both', expand=1)

    def initGrid(self):
        self.mainLable = ttk.Label(self, text="Application", font="Arial 16").grid(row=0, column=0, columnspan=3)

        self.stopButton = ttk.Button(self, text="Сбросить все изменения", command=self.clear).grid(row=11, column=0, columnspan=3, sticky='we', padx=5)
        self.startButton = ttk.Button(self, text="Начать движение", command=self.start).grid(row=12, column=0, columnspan=3, sticky='we', padx=5)

        self.n = IntVar()
        self.n.set(Options.n)
        self.labelN = ttk.Label(self, text="Количество \nмашин:").grid(row=1, column=0, sticky=W)
        self.entryN = ttk.Entry(self, textvariable=self.n, font="Arial 8").grid(row=1, column=1)

        self.L = IntVar()
        self.L.set(Options.L)
        self.labelL = ttk.Label(self, text="Дистанция \nдо остановки:").grid(row=2, column=0, sticky=W)
        self.entryL = ttk.Entry(self, textvariable=self.L, font="Arial 8").grid(row=2, column=1)

        self.vmax = DoubleVar()
        self.vmax.set(Options.vmax)
        self.labelVmax = ttk.Label(self, text="Максимальная \nскорость:").grid(row=3, column=0, sticky=W)
        self.entryVmax = ttk.Entry(self, textvariable=self.vmax, font="Arial 8").grid(row=3, column=1)

        self.vmin = DoubleVar()
        self.vmin.set(Options.vmin)
        self.labelVmin = ttk.Label(self, text="Минимальная \nскорость:").grid(row=4, column=0, sticky=W)
        self.entryVmin = ttk.Entry(self, textvariable=self.vmin, font="Arial 8").grid(row=4, column=1)

        self.var = StringVar()
        self.var.set(Mode.firstMode)
        self.firstMod = ttk.Radiobutton(self, text='First', variable=self.var, value=Mode.firstMode).grid(row=7, column=0, columnspan=3, sticky=W, padx=5)
        self.secondMod = ttk.Radiobutton(self, text='Second', variable=self.var, value=Mode.secondMode).grid(row=8, column=0, columnspan=3, sticky=W, padx=5)
        self.thirdMod = ttk.Radiobutton(self, text='Third', variable=self.var, value=Mode.thirdMode).grid(row=9, column=0, columnspan=3, sticky=W, padx=5)

        self.changeMod = ttk.Button(self, text="Применить изменения", command=self.applyChanging).grid(row=10, column=0, columnspan=3, sticky='we', padx=5)

    def initCarAnimation(self):
        self.figureC = plt.figure(figsize=(8, 3))
        #self.axC = plt.axes([0.03,0.1,0.93,0.8],xlim=(-400, 1100), ylim=(0, 2))
        self.axC = plt.axes([0.03, 0.1, 0.93, 0.8], xlim=(-40, 120), ylim=(0, 2))
        self.axC.spines['top'].set_visible(False)
        self.axC.spines['right'].set_visible(False)
        self.axC.spines['left'].set_visible(False)
        self.axC.get_yaxis().set_ticks([])

        self.axC.vlines(0, 0.4, 1.6, color='r', lw=2)
        if self.options.mode == Mode.firstMode:
            self.axC.vlines(self.options.L, 0.4, 1.6, color='r', lw=2)
        if self.options.mode == Mode.thirdMode:
            self.axC.vlines(self.options.stopL, 0.4, 1.6, color='r', lw=2)
        self.axC.hlines(0.4, -40, 120)
        self.axC.hlines(1.6, -40, 120)
        self.axC.set_title('Движение')
        self.axC.grid()

        self.canvas = FigureCanvasTkAgg(self.figureC, master=self)
        self.canvas.get_tk_widget().grid(column=4, row=0, columnspan=8, rowspan=10)

    def initCars(self):
        init = Animation(self.figureC, self.axC, self.options)
        init.initCars()

    def initSpeedDiagram(self):
        self.figureS = plt.figure(figsize=(4,3))
        self.axS = plt.axes(xlim=(0, 100), ylim=(0, 20))
        self.axS.hlines(self.options.vmax, 0, 100, linestyles='dashed')
        self.axS.hlines(self.options.vmin, 0, 100, linestyles='dashed')
        self.axS.set_title('График изменения скорости')
        self.axS.grid()

        self.canvas = FigureCanvasTkAgg(self.figureS, master=self)
        self.canvas.get_tk_widget().grid(column=4, row=10, rowspan=10, columnspan=2)

    def initDistanceDiagram(self):
        self.figureD = plt.figure(figsize=(4,3))
        self.axD = plt.axes(xlim=(0, 100), ylim=(-50, 150))
        self.axD.hlines(0, 0, 100, linestyles='dashed')
        if self.options.mode == Mode.firstMode:
            self.axD.hlines(self.options.L, 0, 100, linestyles='dashed')
        if self.options.mode == Mode.thirdMode:
            self.axD.hlines(self.options.stopL, 0, 100, linestyles='dashed')
        self.axD.set_title('График пройденного пути')
        self.axD.grid()

        self.canvas = FigureCanvasTkAgg(self.figureD, master=self)
        self.canvas.get_tk_widget().grid(column=6, row=10, rowspan=10, columnspan=2)

    def startAnimate(self):
        distanceAnimation = Animation(self.figureD, self.axD, self.options, AnimationTypes.animateDistance)
        self.animD = distanceAnimation.animate()

        speedAnimation = Animation(self.figureS, self.axS, self.options, AnimationTypes.animateSpeed)
        self.animS = speedAnimation.animate()

        carAnimation = Animation(self.figureC, self.axC, self.options)
        self.animC = carAnimation.animateCars()