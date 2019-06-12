from tkinter import *

anaform = Tk()

anaform.title("katalog")


def verial():
    veri = giris.get()
    veritabani = open("liste.txt", "a+")
    if veri=="1":
        etiket2.config(text="Kitaplarımız şunlardır:", font=("Flux", 24, "bold"), fg="red")
        araetiket.config(text="_________________________", font=("Flux", 24, "bold"), fg="red")
        veritabani.seek(0)
        etiket3.config(text=veritabani.read(), font=("Corbal", 12))
    elif veri=="2":
        ekle()
    elif veri=="3":
        bul1()
    elif veri=="4":
        bul2()
    elif veri=="5":
        bul3()
def bul1():
    kişi_defteri = {"yaşar kemal": "İnce Memed",
                    "Orhan Pamuk": "Benim Adım Kırmızı",
                    "Canan Tan": "Piraye",
                    "Nazım Hikmet": "Çile", "Peyami Safa":"Dokuzuncu Hariciye Koğuşu"}

    kişi = input("Yazar adı girin: ")

    if kişi in kişi_defteri:
        cevap = "{} 'in kitabı: {}"
        print(cevap.format(kişi, kişi_defteri[kişi]))
    else:
        print("Aradığınız kişi katalogda yok..")
def bul2():
    kitap_defteri = {"İnce Memed": "yaşar kemal",
                     "Benim Adım Kırmızı": "Orhan Pamuk",
                     "Piraye": "Canan Tan",
                     "Dokuzuncu Hariciye Koğuşu": "Peyami Safa"}

    kitap = input("Kitap giriniz: ")

    if kitap in kitap_defteri:
        cevap = "{} yazarı: {}"
        print(cevap.format(kitap, kitap_defteri[kitap]))
    else:
        print("Aradığınız kitap katalogda yok..")
def bul3():
    yıl_defteri = {"1994": "İnce Memed, yaşar kemal",
                   "1959": "Benim Adım Kırmızı, Orhan Pamuk",
                   "1960": "Piraye, Canan Tan",
                   "1855": "masallar-servin sarıyer",
                   "1549": "Dokuzuncu Hariciye Koğuşu, Peyami Safa"}
    
    yıl = input("Yıl girin: ")

    if yıl in yıl_defteri:
        cevap = "{} yılı: {}"
        print(cevap.format(yıl, yıl_defteri[yıl]))
    else:
        print("Aradığınız yıl katalogda yok..")

def ekle():
    list = open("liste.txt")
    print(list.read())
    with open("liste.txt", "a") as f:
        f.write("\nAhmet Haşim: Piyale :1926")


girisekrani = Label(text="""Eserler için 1'i tıklayınız
-kitap eklemek için 2'yi tıklayınız 
 -Yazar ismine göre aramak için 3'ü tuşlayınız
 -kitaba göre 4
 -yıla göre 5:) 
""", font=(24))
girisekrani.pack()

etiket = Label(text="Seçimizi yapınız: ", font=(24))
etiket.pack()

giris = Entry()
giris.pack()

giris2 = Entry()

buton2 = Button(text="Ekle!", command=ekle, font=(24))

buton = Button(text="Gir!", command=verial, font=(24))
buton.pack(expand="yes", anchor="center")

etiket2 = Label(text="")
etiket2.pack()

araetiket = Label(text="")
araetiket.pack()

etiket3 = Label()
etiket3.pack()

mainloop()

pencere.mainloop()
