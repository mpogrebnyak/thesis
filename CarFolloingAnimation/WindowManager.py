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
        self.defaultAvailable = False
        self.initEmpty(master)
        self.initRadiobuttons()
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

    def selected(self):
        self.initGrid()

    def applyChanging(self):
        self.options.n = self.n.get()
        self.options.vmax = self.vmax.get()

        if self.var.get() == Mode.firstMode:
            self.options.mode = Mode.firstMode
            self.options.L = self.L.get()
            self.options.vmin = self.vmin.get()

        elif self.var.get() == Mode.secondMode:
            self.options.mode = Mode.secondMode
            self.options.timer = self.greedTime.get()
            self.options.stopTime = self.redTime.get()

        elif self.var.get() == Mode.thirdMode:
            self.options.mode = Mode.thirdMode
            self.options.stopL = self.stopL.get()
            self.options.timerF = self.greedTimeF.get()
            self.options.timerS = self.greedTimeS.get()
            self.options.stopTimeF = self.redTimeF.get()
            self.options.stopTimeS = self.redTimeS.get()

        self.initSpeedDiagram()
        self.initDistanceDiagram()
        self.initCarAnimation()
        self.initCars()

    def clear(self):
        self.options.n = 30
        self.options.vmax = 16.7

        if self.defaultAvailable:
            self.options.mode = Mode.firstMode
            self.options.L = 100
            self.options.vmin = 0
            self.options.timer = 10
            self.options.stopTime = 15
            self.options.stopL = 60
            self.options.timerF = 5
            self.options.timerS = 15
            self.options.stopTimeF = 5
            self.options.stopTimeS = 10
        else:
            self.options.mode = Mode.offMode
            self.options.L = 0
            self.options.vmin = 0
            self.options.timer = 0
            self.options.stopTime = 0
            self.options.stopL = 0
            self.options.timerF = 0
            self.options.timerS = 0
            self.options.stopTimeF = 0
            self.options.stopTimeS = 0

        self.initGrid()
        self.initSpeedDiagram()
        self.initDistanceDiagram()
        self.initCarAnimation()
        self.initCars()

    def initEmpty(self, master):
        self.master.title("Модерирование движения автомобилей")

        self.config(bg='white')
        self.style = ttk.Style()
        self.style.theme_use("vista")

        ttk.Style().configure('TLabel', foreground='black', background='white', font="Arial 10")
        ttk.Style().configure('TButton', foreground='black', background='white', font="Arial 12")
        ttk.Style().configure('TRadiobutton', foreground='black', background='white', font="Arial 11")

        self.pack(fill='both', expand=1)

    def initGrid(self):
        if self.var.get() == Mode.firstMode:
            firstModeDis = NORMAL
            secondModeDis = DISABLED
            thirdModDis = DISABLED

        elif self.var.get() == Mode.secondMode:
            firstModeDis = DISABLED
            secondModeDis = NORMAL
            thirdModDis = DISABLED

        elif self.var.get() == Mode.thirdMode:
            firstModeDis = DISABLED
            secondModeDis = DISABLED
            thirdModDis = NORMAL
        else:
            firstModeDis = DISABLED
            secondModeDis = DISABLED
            thirdModDis = DISABLED

        self.mainLable = ttk.Label(self, text="Модерирование \nдвижения автомобилей", font="Arial 16", justify=CENTER).grid(row=0, column=0, columnspan=3)

        self.stopButton = ttk.Button(self, text="Сбросить все изменения", command=self.clear).grid(row=18, column=0, columnspan=3, sticky='we', padx=5)
        self.startButton = ttk.Button(self, text="Начать движение", command=self.start).grid(row=19, column=0, columnspan=3, sticky='we', padx=5)

        self.n = IntVar()
        self.n.set(Options.n)
        self.labelN = ttk.Label(self, text="Количество машин").grid(row=1, column=0, columnspan=2, sticky=W)
        self.entryN = ttk.Entry(self, textvariable=self.n, font="Arial 8", width=12).grid(row=1, column=2, padx=5)

        self.L = IntVar()
        self.L.set(Options.L)
        self.labelL = ttk.Label(self, text="Дистанция до остановки").grid(row=5, column=0, columnspan=2, sticky=W)
        self.entryL = ttk.Entry(self, textvariable=self.L, font="Arial 8", width=12, state=firstModeDis).grid(row=5, column=2, padx=5)

        self.vmax = DoubleVar()
        self.vmax.set(Options.vmax)
        self.labelVmax = ttk.Label(self, text="Максимальная скорость:").grid(row=2, column=0, columnspan=2, sticky=W)
        self.entryVmax = ttk.Entry(self, textvariable=self.vmax, font="Arial 8", width=12).grid(row=2, column=2, padx=5)

        self.vmin = DoubleVar()
        self.vmin.set(Options.vmin)
        self.labelVmin = ttk.Label(self, text="Минимальная скорость").grid(row=6, column=0, columnspan=2, sticky=W)
        self.entryVmin = ttk.Entry(self, textvariable=self.vmin, font="Arial 8", width=12, state=firstModeDis).grid(row=6, column=2, padx=5)

        self.greedTime = IntVar()
        self.greedTime.set(Options.timer)
        self.labelGreenLight = ttk.Label(self, text="Время работы зеленого \nсигнала светофора").grid(row=8, column=0, sticky=W)
        self.entryGreenLight = ttk.Entry(self, textvariable=self.greedTime, font="Arial 8", width=12, state=secondModeDis).grid(row=8, column=2, padx=5)

        self.redTime = IntVar()
        self.redTime.set(Options.timer)
        self.labelRedLight = ttk.Label(self, text="Время работы красного \n сигнала светофора").grid(row=9, column=0, columnspan=2, sticky=W)
        self.entryRedLight = ttk.Entry(self, textvariable=self.redTime, font="Arial 8", width=12, state=secondModeDis).grid(row=9, column=2, padx=5)

        self.stopL = IntVar()
        self.stopL.set(Options.stopL)
        self.labelStopL = ttk.Label(self, text="Дистанция до светофора").grid(row=11, column=0, columnspan=2, sticky=W)
        self.entryStopL = ttk.Entry(self, textvariable=self.stopL, font="Arial 8", width=12, state=thirdModDis).grid(row=11, column=2, padx=5)

        self.greedTimeF = IntVar()
        self.greedTimeF.set(Options.timerF)
        self.labelGreenLightF = ttk.Label(self, text="Время работы зеленого \nсигнала первого светофора").grid(row=12, column=0, columnspan=2, sticky=W)
        self.entryGreenLightF = ttk.Entry(self, textvariable=self.greedTimeF, font="Arial 8", width=12, state=thirdModDis).grid(row=12, column=2, padx=5)

        self.redTimeF = IntVar()
        self.redTimeF.set(Options.stopTimeF)
        self.labelRedLightF = ttk.Label(self, text="Время работы красного \nсигнала первого светофора").grid(row=13, column=0, columnspan=2, sticky=W)
        self.entryRedLightF = ttk.Entry(self, textvariable=self.redTimeF, font="Arial 8", width=12, state=thirdModDis).grid(row=13, column=2, padx=5)

        self.greedTimeS = IntVar()
        self.greedTimeS.set(Options.timerS)
        self.labelGreenLightS = ttk.Label(self, text="Время работы зеленого \nсигнала второго светофора").grid(row=14, column=0, columnspan=2, sticky=W)
        self.entryGreenLightS = ttk.Entry(self, textvariable=self.greedTimeS, font="Arial 8", width=12, state=thirdModDis).grid(row=14, column=2, padx=5)

        self.redTimeS = IntVar()
        self.redTimeS.set(Options.stopTimeS)
        self.labelRedLightS = ttk.Label(self, text="Время работы красного \nсигнала второго светофора").grid(row=15, column=0, columnspan=2, sticky=W)
        self.entryRedLightS = ttk.Entry(self, textvariable=self.redTimeS, font="Arial 8", width=12, state=thirdModDis).grid(row=15, column=2, padx=5)

        self.changeMod = ttk.Button(self, text="Применить изменения", command=self.applyChanging).grid(row=17, column=0, columnspan=3, sticky='we', padx=5)

    def initRadiobuttons(self):
        self.var = StringVar()
        #self.var.set(Mode.firstMode)
        self.firstMod = ttk.Radiobutton(self, text='Начало движения и остановка', variable=self.var, value=Mode.firstMode, command=self.selected).grid(row=3, column=0, columnspan=3, sticky=W, padx=5)
        self.secondMod = ttk.Radiobutton(self, text='Режим работы одного светофора', variable=self.var, value=Mode.secondMode, command=self.selected).grid(row=7, column=0, columnspan=3, sticky=W, padx=5)
        self.thirdMod = ttk.Radiobutton(self, text='Режим работы двух светофоров', variable=self.var, value=Mode.thirdMode, command=self.selected).grid(row=10, column=0, columnspan=3, sticky=W, padx=5)

    def initCarAnimation(self):
        self.figureC = plt.figure(figsize=(8, 3))
        #self.axC = plt.axes([0.03,0.1,0.93,0.8],xlim=(-400, 1100), ylim=(0, 2))
        if self.options.mode == Mode.thirdMode:
            self.axC = plt.axes([0.03, 0.1, 0.93, 0.8], xlim=(-20, 140), ylim=(0, 2))
        else:
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
        self.axC.hlines(0.4, -40, 200)
        self.axC.hlines(1.6, -40, 200)
        self.axC.set_title('Движение автомобилей')
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
        if self.options.mode == Mode.firstMode:
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