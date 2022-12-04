import turtle
from turtle import Screen, Pen

from turtle import *
pen = turtle.Turtle()

shape("turtle")
speed(5)
pensize(5)



def kare():
    for i in range(4):
        forward(100)
        left(90)
        pencolor("black")

def dikdortgen():
    for i in range(2):
        forward(150)
        left(90)
        forward(75)
        left(90)
        pencolor("black")
        pen()

def ucgen():
    for i in range(3):
        left(120)
        forward(150)
        pencolor("black")
        pen()



def besgen():
    for i in range(5):
        left(72)
        forward(150)
        pencolor("black")
        pen()

def altigen():
    for i in range(6):
        left(60)
        forward(150)
        pencolor("black")
        pen()


def yedigen():
    for i in range(7):
        left(51.4285714)
        forward(150)
        pencolor("black")
        pen()

def dokuzgen():
    for i in range(9):
        left(40)
        forward(150)
        pencolor("black")
        pen()

def ongen():
    for i in range(10):
        left(60)
        forward(150)
        pencolor("black")
        pen()

def onbirgen():
    for i in range(11):
        left(32.727272)
        forward(150)
        pencolor("black")
        pen()

def onikigen():
    for i in range(12):
        left(30)
        forward(150)
        pencolor("black")
        pen()

def daire():
    right(90)
    forward(100)
    left(90)
    pendown()
    circle(100)
    penup()
    setposition(0, 0)

def sekizgen():
        for i in range(8):
            forward(50)
            left(45)
            pencolor("black")
            pen()

def GirdiUcgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Üçgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(3):
            pen.forward(uzunluk)
            pen.left(120)

    ekran.exitonclick()


def GirdiKare():
    ekran = Screen()
    uzunluk = ekran.numinput("Kare", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(4):
            pen.forward(uzunluk)
            pen.left(90)

    ekran.exitonclick()

def GirdiBesgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Beşgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(5):
            pen.forward(uzunluk)
            pen.left(72)

    ekran.exitonclick()

def GirdiAltigen():
    ekran = Screen()
    uzunluk = ekran.numinput("Altıgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(6):
            pen.forward(uzunluk)
            pen.left(60)

    ekran.exitonclick()


def GirdiYedigen():
    ekran = Screen()
    uzunluk = ekran.numinput("Yedigen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(7):
            pen.forward(uzunluk)
            pen.left(51.42857142)

    ekran.exitonclick()


def GirdiSekizgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Sekizgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(8):
            pen.forward(uzunluk)
            pen.left(45)

    ekran.exitonclick()


def GirdiDokuzgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Dokuzgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(9):
            pen.forward(uzunluk)
            pen.left(40)

    ekran.exitonclick()

def GirdiOngen():
    ekran = Screen()
    uzunluk = ekran.numinput("Ongen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(10):
            pen.forward(uzunluk)
            pen.left(36)

    ekran.exitonclick()

def GirdiOnbirgen():
    ekran = Screen()
    uzunluk = ekran.numinput("Onbirgen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(11):
            pen.forward(uzunluk)
            pen.left(32.72727272)

    ekran.exitonclick()


def GirdiOnikigen():
    ekran = Screen()
    uzunluk = ekran.numinput("Onikigen", "Başlangıç kenar uzunluğunu girin:", default=40, minval=10, maxval=70)
    pen = Pen()
    for ucgen in range(12):
            pen.forward(uzunluk)
            pen.left(30)

    ekran.exitonclick()

turtle.done()