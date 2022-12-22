from turtle import Screen, Pen
def GirdiUcgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Üçgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(3):
            pen.forward(uzunluk )
            pen.left(120)

    ekran.exitonclick()


def GirdiKare():
    ekran = Screen()
    uzunluk = ekran.numinput("Kare", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(4):
            pen.forward(uzunluk )
            pen.left(90)

    ekran.exitonclick()

def GirdiBesgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Beşgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(5):
            pen.forward(uzunluk )
            pen.left(72)

    ekran.exitonclick()

def GirdiAltıgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Altıgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(6):
            pen.forward(uzunluk )
            pen.left(60)

    ekran.exitonclick()


def GirdiYedigen():
    ekran = Screen()
    uzunluk = ekran.numinput("Yedigen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(7):
            pen.forward(uzunluk )
            pen.left(51.42857142)

    ekran.exitonclick()


def GirdiSekizgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Sekizgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(8):
            pen.forward(uzunluk )
            pen.left(45)

    ekran.exitonclick()


def GirdiDokuzgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Dokuzgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(9):
            pen.forward(uzunluk )
            pen.left(40)

    ekran.exitonclick()

def GirdiOngen():
    ekran = Screen()
    uzunluk = ekran.numinput("Ongen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(10):
            pen.forward(uzunluk )
            pen.left(36)

    ekran.exitonclick()

def GirdiOnbirgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Onbirgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(11):
            pen.forward(uzunluk )
            pen.left(32.72727272)

    ekran.exitonclick()


def GirdiOnikigen():
    ekran = Screen()
    uzunluk = ekran.numinput("Onikigen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(12):
            pen.forward(uzunluk )
            pen.left(30)

    ekran.exitonclick()