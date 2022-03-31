def mukemmel_sayi(sayi):
    
    toplam = 0
    for i in range(1,sayi):
        if sayi%i == 0:
            toplam += i

    if sayi == toplam:
        print(sayi," Bu bir Mükemmel sayıdır.")

for i in range(1,1000):
    mukemmel_sayi(i)