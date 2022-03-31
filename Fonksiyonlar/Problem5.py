#1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları 
#ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

def pisagor():

    pisagor_liste = list()
    for i in range(1,101):
        for j in range(1,101):
            c = (i**2+j**2)**0.5
            if c == int(c):
                if int(c) == 100:
                    break
                pisagor_liste.append((int(c),i,j))
        
    return pisagor_liste
pis = pisagor()
for i in pis:
    print(i)
    