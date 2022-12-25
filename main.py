import tkinter as tk
pencere = tk.Tk()
pencere.geometry('800x600')


def page2():  # 0-6 yaş menü penceresi
    pencere2 = tk.Tk()
    pencere2.geometry('800x600')
    pencere2.title("6 Yaş ve Üstü Grubu")
    dugme4 = tk.Button(pencere2, text='Çıkış', command=pencere2.destroy)
    dugme4.pack(side=tk.BOTTOM, pady=5)
    pencere.destroy()
def page3():  # 6 yaş ve üzeri menü penceresi
    pencere3 = tk.Tk()
    pencere3.geometry('800x600')
    pencere3.title("6 Yaş ve Üstü Grubu")
    dugme5 = tk.Button(pencere3, text='Çıkış', command=pencere3.destroy)
    dugme5.pack(side=tk.BOTTOM, pady=5)
    pencere.destroy()


etiket = tk.Label(text = 'Hoşgeldiniz')
etiket.pack()

dugme = tk.Button(text='0-6 yaş', command=page2)
dugme.pack(padx=5, side=tk.LEFT)

dugme2 = tk.Button(text='6 yaş ve üstü', command=page3)
dugme2.pack(padx=5, side=tk.RIGHT)

dugme3 = tk.Button(text='Çıkış', command=pencere.destroy)
dugme3.pack(side=tk.BOTTOM, pady=5)

pencere.title("Öğretici Çizen Robot")



pencere.mainloop()