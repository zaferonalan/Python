
# ! Dictionary 

User = {
    "Name": "Zafer Günay",
    "Surname": "Önalan",
    "Age": 25,
    "Job": "SoftWare"
}

# print(User)
# print(type(User))
# print(len(User))
# print(User["Name"])
# User["marital status"]="singel"
# print(User)
# User["Name"] = "Merve"
# print(User)
# print(User.keys())
# print(User.values())
# print(User.items())

# ! Hem key hem de value değerini güncellemek için
# User.update({"isim": "Ali" , "kan grubu": "A Rh+"})
# print(User)

# ! İstediğim elemanı silmek için
# User.pop("kan grubu")
# print(User)

# ! Dictionary İle Döngü Kullanımı

# TODO: Key değerini döndürür
# for i in User:
#     print(i)

# TODO: Value değerini döndürür
# for i in User:
#     print(User[i])

# TODO: Hem key hem value değerini döndürür
# for i,j in User.items():
#     print(i,j)    

# ! Örnek-1
# ! Aşağıda verilen notlardan 50 ve üzeri olanları geçti diğerlerini kaldı olarak belirleyelim.

# Notes = {"Ahmet": 30 , "Selim": 58 , "Merve": 85 , "Berkay": 44 , "Zafer": 85}

# print(Notes.items())

# for name,point in Notes.items():
#     if point > 50:
#         print(f"Öğrenci adı : {name} , Öğrenci notu : {point} GEÇTİ ")
#     else:
#         print(f"Öğrenci adı : {name} , Öğrenci notu : {point} KALDI")


# ! Örnek-2
# dictionary = {
#     "hello": "Merhaba",
#     "book" : "Kitap",
#     "read" : "Okumak",
#     "good night" : "İyi geceler",
# }

# word = input("Kelime giriniz: ").lower()

# while True:
#     if word in dictionary:
#         print(f"{word} : {dictionary[word]}")
#         break
#     else:
#         print(f"Kelimenin karşılığı sözlükte yok. Tekrar giriniz!")
#         word = input("Kelime giriniz.").lower()


# ! Örnek-3

# students_noteList = {}

# while True:
#     students_name = input("Öğrenci adını giriniz (Çıkmak için q ya basınız) : ")

#     if students_name == "q":
#         break
    
#     students_point = int(input("Öğrencinin Notunu giriniz :"))

#     students_noteList[students_name] = students_point

#     # print(students_noteList)

# search_studentName = input("Aranan öğreniciyi giriniz :")
# if search_studentName in students_noteList:
#     print(f"{search_studentName}'in notu : {students_noteList[search_studentName]}")
#     # student_list = list(students_noteList.items())
#     # print(student_list)
#     print(students_noteList)
# else:
#     print(f"{search_studentName} adında öğrencimiz bulunmamaktadır.")



# ! Örnek-4

# veri = {"Ahmet": 30 , "Mehmet": 40, "Kerem": 20}

# veri_listesi = list(veri.keys())
# print(veri_listesi)


# ! Örnek 5

envanter = {}

menu = """"
1 Ürün Eklemek
2 Ürün Çıkarmak
3 Ürün Listelemek
4 Çıkış
"""

while True:
    print(menu)

    choose = input("Seçim yapınız :")

    if choose == "1":
        product = input("Eklemek istediğiniz ürünü giriniz :")
        number = int(input(f"Eklenecek {product} miktarını giriniz :"))

        if product in envanter:
            envanter[product] += number
        else:
            envanter[product] = number
    
    elif choose == "2":
        product = input("Çıkarmak istediğiniz ürünü giriniz :")
        number = int(input(f"Çıkarılacak {product} miktarını giriniz : "))

        if product in envanter:
            if envanter[product] >= number:
                envanter[product] -= number
                print(f"{number} adet {product} miktarından çıkarıldı")
            else:
                print(f"Envanterde yeterli {product} yok")
    
    elif choose == "3":
        print("Güncel Envanter Durumu")
        for key,value in envanter.items():
            print(f"{key} : {value} adet vardır.")

    elif choose == "4":
        break;
    else:
        print("Yanlış değer girdiniz")        


