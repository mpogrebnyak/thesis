class Mode(object):
    firstMode = 'firstMode' #старт и стоп
    secondMode = 'secondMode' #один цикл светофора
    thirdMode = 'thirdMode' #работа светофора

class Options(object):
    h = 0.1
    tau = 1
    lambd0 = 0
    lambd = 6#60
    n = 10
    mu = 0.6
    g = 9.8
    L = 100
    a = 1
    q = 1
    l = 4
    vmax = 16.7
    vmin = 0
    mode = Mode.firstMode

    # для второго мода
    timer = 10
    stopTime = 15

    # для третьего мода
    timerF = 5
    timerS = 15
    stopTimeF = 5
    stopTimeS = 10
    stopL = 60
