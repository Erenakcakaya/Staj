import tkinter as tk


# Bir çerçeve oluşturuldu ve ayarları yapıldı
mainframe = tk.Tk()
mainframe.config(bg="#363636")
mainframe.resizable(False, False)
mainframe.geometry("320x450")
mainframe.title("HESAP MAKİNESİ")

# Label'ler ve Entry'ler için renkler ayarlandı
bg = "#171515"
fg = "#6F5B3E"
bg1 = "#C4AE78"
fontc = "#6F5B3E"

# Hata sonucunu gösteren string
strvalue = str("Sadece sayı girebilirsiniz")

# Sayıları ve sonucu gösteren label'ların ayarları yapıldı ve hazırlandı
numberbox0 = tk.Label(text="İlk Sayı:      ",
                      font="Arial 15 bold", bg=bg, fg=fg)
numberbox0.pack(pady=10, anchor="w")

numberbox1 = tk.Label(text="İkinci Sayı: ",
                      font="Arial 15 bold", fg=fg, bg=bg)
numberbox1.pack(pady=10, anchor="w")

resultbox = tk.Label(text="Sonuç: ",
                     font="Arial 15 bold", fg=fg, bg=bg)
resultbox.pack(pady=10, anchor="w")

# resultbox label'ine bağlı görünen cevabın yazacağı label
labelbox = tk.Label(text="", font="Arial 15 bold", bg=bg, width="20", fg=fontc)
labelbox.place(x=78, y=110)

numberentry0 = tk.Entry(font="Arial 15 bold", bg=bg1, fg=fontc, width="15")
numberentry0.place(x=110, y=10, height=30)

numberentry1 = tk.Entry(font="Arial 15 bold", bg=bg1, fg=fontc, width="15")
numberentry1.place(x=110, y=60, height=30)

# Toplama fonksiyonu


def addition():
    while numberentry0 or numberentry1 != int:
        try:
            if numberentry0 or numberentry1 != int:
                n1 = int(numberentry0.get())
                n2 = int(numberentry1.get())
                labelbox["text"] = int(n1+n2)
                break
        except:
            labelbox["text"] = strvalue
            break


# Toplama butonu ve ayarları yapılıp "addition" fonksiyonu verildi
button0 = tk.Button(text="TOPLA", font="Arial 15 bold",
                    bg=bg, fg=fontc, command=addition,)
button0.place(x=30, y=180, width=85)

# Çıkarma fonksiyonu


def subtraction():
    while numberentry0 or numberentry1 != int:
        try:
            if numberentry0 or numberentry1 != int:
                n1 = int(numberentry0.get())
                n2 = int(numberentry1.get())
                labelbox["text"] = int(n1-n2)
                break
        except:
            labelbox["text"] = strvalue
            break


# Çıkarma butonu ve ayarları yapılıp "subtraction" fonksiyonu verildi
button1 = tk.Button(text="ÇIKAR", font="Arial 15 bold",
                    bg=bg, fg=fontc, command=subtraction)
button1.place(x=210, y=180, width=85)

# Bölme fonksiyonu


def division():
    while numberentry0 or numberentry1 != int:
        try:
            if numberentry0 or numberentry1 != int:
                n1 = int(numberentry0.get())
                n2 = int(numberentry1.get())
                x = float(n1/n2)
                labelbox["text"] = x
                break
        except:
            labelbox["text"] = strvalue
            break


# Bölme butonu ve ayarları yapılıp "subtraction" fonksiyonu verildi
button2 = tk.Button(text="BÖL", font="Arial 15 bold",
                    bg=bg, fg=fontc, command=division)
button2.place(x=30, y=250, width=85)

# Bölme fonksiyonu


def multiplication():
    while numberentry0 or numberentry1 != int:
        try:
            if numberentry0 or numberentry1 != int:
                n1 = int(numberentry0.get())
                n2 = int(numberentry1.get())
                labelbox["text"] = str(n1*n2)
                break
        except:
            labelbox["text"] = strvalue
            break


# Çarpma butonu ve ayarları yapılıp "multiplication" fonksiyonu verildi
button3 = tk.Button(text="ÇARP", font="Arial 15 bold",
                    bg=bg, fg=fontc, command=multiplication)
button3.place(x=210, y=250, width=85)


def exponential():
    while numberentry0 or numberentry1 != int:
        try:
            if numberentry0 or numberentry1 != int:
                n1 = int(numberentry0.get())
                n2 = int(numberentry1.get())
                labelbox["text"] = str(n1**n2)
                break
        except:
            labelbox["text"] = strvalue
            break


button4 = tk.Button(text="ÜS", font="Arial 15 bold",
                    bg=bg, fg=fontc, command=exponential)
button4.place(x=30, y=320, width=85)

mainframe.mainloop()
