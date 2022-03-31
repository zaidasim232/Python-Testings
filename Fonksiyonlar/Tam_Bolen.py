def tam_bolen(sayi):
    sayi = int(sayi)
    tam_bolen = []
    for i in range(2,sayi):
        if sayi%i == 0:
            tam_bolen.append(i)

    return tam_bolen

sayi = input("Sayi gir : ")
print("Girdiğin sayının tam böleni şudur: {}".format(tam_bolen(sayi)))


