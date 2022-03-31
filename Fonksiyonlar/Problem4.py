
birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz","on"]
onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def say(sayi):
    sayi = int(sayi)
    birler_bir = sayi%10
    onlar_on = sayi//10
    print(onlar[onlar_on],birler[birler_bir])
    





sayilan = input("sayı girin : ")
say(sayilan)