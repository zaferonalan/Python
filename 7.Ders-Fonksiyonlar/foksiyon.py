# ! FONKSİYONLAR
# Parametresiz Fonksiyon Kullanımı

# def yazdir():
#     isim = input("İsim giriniz:")
#     print(f"Merhaba {isim}")

# yazdir()


# ! Örnek
# def tek_cift_ayirma():
#     ilkDeger = int(input("İlk sayıyı giriniz: "))
#     sonDeger = int(input("Son sayıyı giriniz: "))

#     tekSayilar = []
#     ciftSayilar = []

#     for sayi in range(ilkDeger,sonDeger):
#         if sayi % 2 == 0:
#             ciftSayilar.append(sayi)
#         else:
#             tekSayilar.append(sayi)

#     print(f"Tek sayılar : {tekSayilar}")
#     print(f"Çift Sayılar : {ciftSayilar}")

# tek_cift_ayirma()


# ! Örnek
# import datetime

# def tarih_ve_saat_göster():
#     suAn = datetime.datetime.now()
#     gün = suAn.day
#     ay = suAn.month
#     yil = suAn.year
#     saat = suAn.hour
#     dakika = suAn.minute
#     saniye = suAn.second

#     print(f"Tarih : {gün}-{ay}-{yil} ve Saat: {saat} : {dakika} : {saniye} ")

# tarih_ve_saat_göster()


# ! PARAMETRELİ FONKSİYON

# isim = input("Bir isim giriniz:")
# def yazdir(isim):
#     print(f"Merhaba {isim}")

# yazdir(isim)


# ! Örnek
# number1 = int(input("İlk sayıyı giriniz:"))
# number2 = int(input("İkinci sayıyı giriniz:"))

# def topla(sayi1, sayi2):
#     toplam = sayi1 + sayi2
#     print(toplam)

# topla(number1, number2)


# ! Örnek
# ! Boş bir dizi tanımlayalım. While döngüsü ile listeye istedğim kadar isim ekleyebileyim. Hiçbir şeye basmadan entere bastığımda dizi içerisinde bulunan isim terminale yazdıralım.

def liste():
    liste = []
    while True:
        isim = input("İsim giriniz :")
        if isim != "":
            liste.append(isim)
            print(f"{isim} adlı eleman listeye eklendi.")
        else:
            print("Programdan çıkılıyor")
            break
    print(liste)

liste()