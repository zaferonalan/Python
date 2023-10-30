
# ! WHİLE DÖNGÜSÜ

# ! Örnek 1

# notu = 0
# while notu < 60:
#     print("Öğrenci başarısız")
#     notu = int(input("Notunuzu giriniz:"))  
# print("öğrenci başarılı oldu.")


# startNumber = int(input("Başlangıç Sayısı Giriniz :"))
# endNumber = int(input("Bitiş Sayısını Giriniz :"))
# numberSum=0

# while startNumber<= endNumber:
#     if startNumber % 2 == 0:
#        numberSum = numberSum + startNumber
#     startNumber = startNumber + 1
# print(f"{startNumber} dan {endNumber} kadar olan çift sayıların toplamı {numberSum}") 

# ! Örnek 2

# passwordEntry = input("Parola Gİriniz :")
# password = "123456"
# rights = 3

# while passwordEntry != password:
#     rights -= 1
#     if rights == 0:
#         print("Hakkınız tükenmiştir.")
#         break
#     print(f"{rights} Hakkınız kaldı. Tekrar deneyiniz!")
#     input("Parolayı Giriniz :")
# if passwordEntry == password:
#     print("Giriş Başarılı") 



# ! Örnek 3

# import random
# randomNumbers = random.randint(1, 100)
# print(randomNumbers)
# rights = 3
# guess = ""

# while randomNumbers != guess:
    
#     guess = int(input("1-100 Arasında Tahmin Sayınızı Giriniz :"))
#     rights -= 1

#     if randomNumbers == guess:
#         print(f"Tebrikler bildiniz.")
#     if guess < randomNumbers:
#         print("Sayıyı arttırın")
#     if guess > randomNumbers:
#         print("Sayıyı azaltın")
#     if rights == 0:
#         print(f"Hakkınız bitti.")
#         break
#     print(f"Kalan Hakkınız {rights}")

