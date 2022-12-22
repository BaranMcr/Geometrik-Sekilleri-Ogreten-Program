from turtle import Screen, Pen
def OruntuUcgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Üçgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    arttırmak = ekran.numinput("üçgneler", "Boyut artışını girin:", default=30, minval=10, maxval=50)
    Ucgenler = int(ekran.numinput("Ucgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))
    pen = Pen()

    for ucgen in range(Ucgenler):
        for _ in range(3):
            pen.forward(uzunluk + ucgen * arttırmak)
            pen.left(120)

    ekran.exitonclick()

def OruntuKare():
        ekran = Screen()
        uzunluk = ekran.numinput("Kare", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
        arttırmak = ekran.numinput("Kareler", "Boyut artışını girin:", default=30, minval=10, maxval=50)
        sekiller = int(ekran.numinput("Kareler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))
        pen = Pen()

        for sekil in range(sekiller):
            for _ in range(4):
                pen.forward(uzunluk + sekil * arttırmak)
                pen.left(90)

        ekran.exitonclick()


def OruntuBesgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Besgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    arttırmak = ekran.numinput("Besgen", "Boyut artışını girin:", default=30, minval=10, maxval=50)
    sekiller = int(ekran.numinput("Besgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))
    pen = Pen()

    for sekil in range(sekiller):
        for _ in range(5):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(72)

    ekran.exitonclick()

def OruntuAltigen():
    ekran = Screen()
    uzunluk = ekran.numinput("Altigen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    arttırmak = ekran.numinput("Altigenler", "Boyut artışını girin:", default=30, minval=10, maxval=50)
    sekiller = int(ekran.numinput("Altigenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))
    pen = Pen()

    for sekil in range(sekiller):
        for _ in range(6):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(60)

        ekran.exitonclick()


def OruntuYedigen():
    ekran = Screen()
    uzunluk = ekran.numinput("Yedigen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    arttırmak = ekran.numinput("Yedigen", "Boyut artışını girin:", default=30, minval=10, maxval=50)
    sekiller = int(ekran.numinput("Yedigenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))
    pen = Pen()

    for sekil in range(sekiller):
        for _ in range(7):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(51.42857142)

    ekran.exitonclick()

def OruntuSekizgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Sekizgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    arttırmak = ekran.numinput("Sekizgen", "Boyut artışını girin:", default=30, minval=10, maxval=50)
    sekiller = int(ekran.numinput("Sekizgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))
    pen = Pen()

    for sekil in range(sekiller):
        for _ in range(8):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(45)

    ekran.exitonclick()


def OruntuDokuzgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Dokuzgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    arttırmak = ekran.numinput("Dokuzgen", "Boyut artışını girin:", default=30, minval=10, maxval=50)
    sekiller = int(ekran.numinput("Dokuzgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))
    pen = Pen()

    for sekil in range(sekiller):
        for _ in range(9):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(40)

    ekran.exitonclick()

def OruntuOngen():
    ekran = Screen()
    uzunluk = ekran.numinput("Ongen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    arttırmak = ekran.numinput("Ongen", "Boyut artışını girin:", default=30, minval=10, maxval=50)
    sekiller = int(ekran.numinput("Ongenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))
    pen = Pen()

    for sekil in range(sekiller):
        for _ in range(10):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(36)

    ekran.exitonclick()

def OruntuOnbirgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Onbirgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    arttırmak = ekran.numinput("Onbirgen", "Boyut artışını girin:", default=30, minval=10, maxval=50)
    sekiller = int(ekran.numinput("Onbirgenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))
    pen = Pen()

    for sekil in range(sekiller):
        for _ in range(11):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(32.72727272)

    ekran.exitonclick()

def OruntuOnikigen():
    ekran = Screen()
    uzunluk = ekran.numinput("Onikigen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    arttırmak = ekran.numinput("Onikigen", "Boyut artışını girin:", default=30, minval=10, maxval=50)
    sekiller = int(ekran.numinput("Onikigenler", "İstediğiniz üçgen sayısını girin:", default=3, minval=1, maxval=5))
    pen = Pen()

    for sekil in range(sekiller):
        for _ in range(12):
            pen.forward(uzunluk + sekil * arttırmak)
            pen.left(30)

    ekran.exitonclick()






