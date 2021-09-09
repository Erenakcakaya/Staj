import tkinter as tk
import requests
import json
from decimal import getcontext, Decimal

mainframe = tk.Tk()
mainframe.resizable(False, False)
mainframe.config(bg="#182732")
mainframe.geometry("600x450")
mainframe.title("DÖVİZ HESAPLAMA")

font = "Arial 15 bold"
errorBg = "#FF0000"
bg = "#051019"
fg = "#425361"


def Mdestroy():
    errormessage["text"] = " "


def Sframe0():
    secondframe = tk.Tk()
    secondframe.geometry("360x65")
    secondframe.config(bg="#363636")
    secondframe.resizable(False, False)
    secondframe.title("DÖVİZLER")

    def USD0():
        errormessage["text"] = "Bu özellik şu anda kullanılamamaktadır."
        errormessage.after(3000, Mdestroy)
        secondframe.destroy()
    choosecash0 = tk.Button(secondframe, text="USD",
                            bg=errorBg, font=font, command=USD0)
    choosecash0.place(x=10, y=10)

    def EUR0():
        cash0["text"] = "EUR"
        secondframe.destroy()
    choosecash1 = tk.Button(secondframe, text="EUR", font=font, command=EUR0)
    choosecash1.place(x=80, y=10)

    def TRY0():
        errormessage["text"] = "Bu özellik şu anda kullanılamamaktadır."
        errormessage.after(3000, Mdestroy)
        secondframe.destroy()
    choosecash2 = tk.Button(secondframe, bg=errorBg,
                            text="TRY", font=font, command=TRY0)
    choosecash2.place(x=150, y=10)

    def GBP0():
        errormessage["text"] = "Bu özellik şu anda kullanılamamaktadır."
        errormessage.after(3000, Mdestroy)
        secondframe.destroy()
    choosecash3 = tk.Button(secondframe, bg=errorBg,
                            text="GBP", font=font, command=GBP0)
    choosecash3.place(x=220, y=10)

    def CAD0():
        errormessage["text"] = "Bu özellik şu anda kullanılamamaktadır."
        errormessage.after(3000, Mdestroy)
        secondframe.destroy()
    choosecash2 = tk.Button(secondframe, bg=errorBg,
                            text="CAD", font=font, command=CAD0)
    choosecash2.place(x=290, y=10)


def Sframe1():
    secondframe = tk.Tk()
    secondframe.geometry("360x65")
    secondframe.config(bg="#363636")
    secondframe.resizable(False, False)
    secondframe.title("DÖVİZLER")

    def USD1():
        cash1["text"] = "USD"
        secondframe.destroy()

        def cal():
            result = requests.get(url+cash0["text"])
            result = json.loads(result.text)
            value = float(result["rates"][cash1["text"]])
            getcontext().prec = 4
            n1 = float(howmanycash0.get())
            howmanycash1["text"] = float(Decimal(n1)*Decimal(value))

        calculate = tk.Button(text="Hesapla", bg=bg,
                              fg=fg, font=font, command=cal)
        calculate.place(x=250, y=190)
    choosecash0 = tk.Button(secondframe, text="USD", font=font, command=USD1)
    choosecash0.place(x=10, y=10)

    def EUR1():
        cash1["text"] = "EUR"
        secondframe.destroy()

        def cal():
            result = requests.get(url+cash0["text"])
            result = json.loads(result.text)
            value = float(result["rates"][cash1["text"]])
            getcontext().prec = 4
            n1 = float(howmanycash0.get())
            howmanycash1["text"] = float(Decimal(n1)*Decimal(value))

        calculate = tk.Button(text="Hesapla", bg=bg,
                              fg=fg, font=font, command=cal)
        calculate.place(x=250, y=190)
    choosecash1 = tk.Button(secondframe, text="EUR", font=font, command=EUR1)
    choosecash1.place(x=80, y=10)

    def TRY1():
        cash1["text"] = "TRY"
        secondframe.destroy()

        def cal():
            result = requests.get(url+cash0["text"])
            result = json.loads(result.text)
            value = float(result["rates"][cash1["text"]])
            getcontext().prec = 4
            n1 = float(howmanycash0.get())
            howmanycash1["text"] = float(Decimal(n1)*Decimal(value))

        calculate = tk.Button(text="Hesapla", bg=bg,
                              fg=fg, font=font, command=cal)
        calculate.place(x=250, y=190)
    choosecash2 = tk.Button(secondframe, text="TRY", font=font, command=TRY1)
    choosecash2.place(x=150, y=10)

    def GBP1():
        cash1["text"] = "GBP"
        secondframe.destroy()

        def cal():
            result = requests.get(url+cash0["text"])
            result = json.loads(result.text)
            value = float(result["rates"][cash1["text"]])
            getcontext().prec = 4
            n1 = float(howmanycash0.get())
            howmanycash1["text"] = float(Decimal(n1)*Decimal(value))

        calculate = tk.Button(text="Hesapla", bg=bg,
                              fg=fg, font=font, command=cal)
        calculate.place(x=250, y=190)
    choosecash3 = tk.Button(secondframe, text="GBP", font=font, command=GBP1)
    choosecash3.place(x=220, y=10)

    def CAD1():
        cash1["text"] = "CAD"
        secondframe.destroy()

        def cal():
            result = requests.get(url+cash0["text"])
            result = json.loads(result.text)
            value = float(result["rates"][cash1["text"]])
            getcontext().prec = 4
            n1 = float(howmanycash0.get())
            howmanycash1["text"] = float(Decimal(n1)*Decimal(value))

        calculate = tk.Button(text="Hesapla", bg=bg,
                              fg=fg, font=font, command=cal)
        calculate.place(x=250, y=190)
    choosecash3 = tk.Button(secondframe, text="CAD", font=font, command=CAD1)
    choosecash3.place(x=290, y=10)


cashname0 = tk.Label(
    text="Elinizdeki Para Birimini Seçiniz", bg=bg, fg=fg, font=font)
cashname0.place(x=10, y=12)

cashbutton0 = tk.Button(text="Dövizler", bg=bg, fg=fg,
                        font=font, command=Sframe0)
cashbutton0.place(x=310, y=5)

cashname0 = tk.Label(text="Dönüştürülecek Birimi Seçiniz",
                     bg=bg, fg=fg, font=font)
cashname0.place(x=10, y=72)

cashbutton1 = tk.Button(text="Dövizler", bg=bg, fg=fg,
                        font=font, command=Sframe1)
cashbutton1.place(x=310, y=65)

cash0 = tk.Label(text="EUR", bg=bg, fg=fg, font=font, width=15,)
cash0.place(x=10, y=150)

txt = tk.Label(text="~~", bg="#182732", fg="black", font=font)
txt.place(x=280, y=150)

cash1 = tk.Label(text="Birimi Seçin", bg=bg, fg=fg, font=font, width=15,)
cash1.place(x=400, y=150)

howmanycash0 = tk.Entry(font=font, bg=bg, fg=fg, width=10,)
howmanycash0.place(x=45, y=200)

howmanycash1 = tk.Label(text="", bg=bg, fg=fg, font=font, width=10)
howmanycash1.place(x=430, y=200)


url = "http://data.fixer.io/api/latest?access_key=327984854532c4da2716ba4bb056d8a9&format=1"

errormessage = tk.Label(
    text="", font=font, fg="red", bg="#182732")
errormessage.place(x=120, y=300)

mainframe.mainloop()
