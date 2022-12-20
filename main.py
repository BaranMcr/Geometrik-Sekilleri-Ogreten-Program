from turtle import *

shape("turtle")
speed(5)

pensize(5)



def kare():
    for i in range(4):
        forward(100)
        left(90)
        pencolor("black")
        pen()

def dikdörtgen():
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

def altıgen():
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
sekizgen()
