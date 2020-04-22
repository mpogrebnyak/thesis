class Mode(object):
    firstMode = 'firstMode' #старт и стоп
    secondMode = 'secondMode' #один цикл светофора
    thirdMode = 'thirdMode' #работа светофора

class Options(object):
    h = 0.1
    tau = 1
    lambd0 = 0
    lambd = 72
    n = 30
    mu = 0.6
    g = 9.8
    L = 1000
    a = 1
    q = 1
    l = 4
    vmax = 16.7
    vmin = 0
    mode = Mode.firstMode
    timer = 10