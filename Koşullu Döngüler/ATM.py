print("""
************************************
        ATM Programı

ATM işlemleri

1. Bakiye gösterme
2. Para Yatırma
3. Para Çekme

Programdan çıkmak için "q" harfi basınız
************************************

""")

Bakiye = 2000

while True:
    
    islem = input("Yapmak istediğiniz İşlemi giriniz : ")

    if islem == "q":
        break
    elif islem == "1":
        print("Bakiyeniz {}TL'dir".format(Bakiye))
    elif islem == "2":
        Para_yatirma = int(input("Yatırmak istediğiniz miktarı giriniz : "))
        Bakiye += Para_yatirma
    elif islem == "3":
        Para_cek = int(input("Para çekmek istediğiniz miktarı giriniz : "))

        if Para_cek > Bakiye:
            print("Para çekemezsiniz çünkü Hesapta o kadar para yok.")
            continue
        else:
            Bakiye -= Para_cek


