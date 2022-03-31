#Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan 
#sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

list_comp = list() 

for i in range(1,101):
    list_comp.append(i)

cift_sayilar = [x for x in list_comp if x%2 == 0 ]
print(cift_sayilar)

print("Bide bu da var ")
cift_sayi = [i for i in range(1,101) if i%2 == 0]
print(cift_sayi)

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = list()
for i in liste:
    for x in i:
        #print("x:",x)
        liste2.append(x)
print(liste2)
    
# List Comprehension 

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = [x for i in liste for x in i] # Biraz karmaşık
print(liste2)