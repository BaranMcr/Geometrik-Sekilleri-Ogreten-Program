import tkinter as tk
import turtle
from turtle import *

pencere = tk.Tk()
pencere.geometry("700x600")
pencere.title("Öğretici Çizen Robot")
etiket = tk.Label(text='Hoşgeldiniz', font=12)
etiket.pack(pady=10)

def page2():  # 0-6 yaş menü penceresi
    pencere2 = tk.Tk()
    pencere2.geometry('700x600')
    pencere2.title("6 Yaş ve Üstü Grubu")

    # canvas = tk.Canvas(pencere2, width=600, height=400)
    # canvas.pack(side=tk.TOP)
    # t = turtle.RawTurtle(canvas)


    dugme4 = tk.Button(pencere2, text='Çıkış', command=pencere2.destroy)
    dugme4.pack(side=tk.BOTTOM, pady=5)

    dugmekare = tk.Button(pencere2, text='Kare', command=kare)
    dugmekare.place(x=10, y=500)

    dugmedikdortgen = tk.Button(pencere2, text='Dikdörtgen', command=dikdortgen)
    dugmedikdortgen.place(x=50, y=500)

    dugmeucgen = tk.Button(pencere2, text='Üçgen', command=ucgen)
    dugmeucgen.place(x=125, y=500)

    dugmebesgen = tk.Button(pencere2, text='Beşgen', command=besgen)
    dugmebesgen.place(x=175, y=500)

    dugmealtigen = tk.Button(pencere2, text='Altıgen', command=altigen)
    dugmealtigen.place(x=230, y=500)

    dugmeyedigen = tk.Button(pencere2, text='Yedigen', command=yedigen)
    dugmeyedigen.place(x=285, y=500)

    dugmesekizgen = tk.Button(pencere2, text='Sekizgen', command=sekizgen)
    dugmesekizgen.place(x=343, y=500)

    dugmedokuzgen = tk.Button(pencere2, text='Dokuzgen', command=dokuzgen)
    dugmedokuzgen.place(x=405, y=500)

    dugmeongen = tk.Button(pencere2, text='Ongen', command=ongen)
    dugmeongen.place(x=475, y=500)

    dugmeonbirgen = tk.Button(pencere2, text='Onbirgen', command=onbirgen)
    dugmeonbirgen.place(x=528, y=500)

    dugmeonikigen = tk.Button(pencere2, text='Onikigen', command=onikigen)
    dugmeonikigen.place(x=593, y=500)

    dugmedaire = tk.Button(pencere2, text='Daire', command=daire)
    dugmedaire.place(x=655, y=500)


    pencere.destroy()


# 6 yaş ve üzeri menü penceresi
def page3():
    pencere3 = tk.Tk()
    pencere3.geometry('700x600')
    pencere3.title("6 Yaş ve Üstü Grubu")

    dugme5 = tk.Button(pencere3, text='Çıkış', command=pencere3.destroy)
    dugme5.pack(side=tk.BOTTOM, pady=5)

    dugmecizdir = tk.Button(pencere3, text='Çizdir')
    dugmecizdir.place(x=50, y=560)

    label1 = tk.Label(pencere3, text='Kenar Sayısını giriniz:')
    label1.place(x=10, y=470)

    entry1 = tk.Entry(pencere3)
    entry1.place(x=125, y=470)

    label2 = tk.Label(pencere3, text='Açı Değerini Giriniz:')
    label2.place(x=10, y=500)

    entry2 = tk.Entry(pencere3)
    entry2.place(x=125, y=500)

    label3 = tk.Label(pencere3, text='Köşe Sayısını Giriniz:')
    label3.place(x=10, y=530)

    entry3 = tk.Entry(pencere3)
    entry3.place(x=125, y=530)



    pencere.destroy()


dugme = tk.Button(text='0-6 yaş', font=12, command=page2)
dugme.pack(padx=5, side=tk.LEFT)

dugme2 = tk.Button(text='6 yaş ve üstü', font=12, command=page3)
dugme2.pack(padx=5, side=tk.RIGHT)

dugme3 = tk.Button(text='Çıkış', font=12, command=pencere.destroy)
dugme3.pack(side=tk.BOTTOM, pady=5)


def kare():
    for i in range(4):
        forward(100)
        left(90)

def dikdortgen():
    for i in range(2):
        forward(150)
        left(90)
        forward(75)
        left(90)

def ucgen():
    for i in range(3):
        left(120)
        forward(150)

def besgen():
    for i in range(5):
        left(72)
        forward(150)

def altigen():
    for i in range(6):
        left(60)
        forward(150)

def yedigen():
    for i in range(7):
        left(51.4285714)
        forward(150)

def dokuzgen():
    for i in range(9):
        left(40)
        forward(150)

def ongen():
    for i in range(10):
        left(60)
        forward(150)

def onbirgen():
    for i in range(11):
        left(32.727272)
        forward(150)

def onikigen():
    for i in range(12):
        left(30)
        forward(150)

def daire():
    penup()
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

pencere.mainloop()