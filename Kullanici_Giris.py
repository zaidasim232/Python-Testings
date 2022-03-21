


print("""
************************************
Kullanıcı Giriş Programı
************************************

""")

sys_kullanici_adi = "memet"
sys_parola = "123456"
giris_hakki = 3
giris = 0
while True:
    musteri_kullanici_adi = input("Kullanıcı Adı : ")
    musteri_parola = input("Parola : ")

    if musteri_kullanici_adi == sys_kullanici_adi and musteri_parola == sys_parola:
        print("Sisteme hoş geldiniz")
        break
    else:
        print("Kullanıcı adı veya parola hatalıdır. lütfen şifreyi tekrar giriniz")
        giris += 1 
        print("Son {} giriş hakkınız bulunmaktadır.".format(giris_hakki-giris))
    
    if giris == giris_hakki:
        print("giriş haklarınızı tükettiniz")
        break



    
