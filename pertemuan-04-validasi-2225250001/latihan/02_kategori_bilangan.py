

bilangan = int(input("Masukkan bilangan: "))

if bilangan < 0:
    print("Bilangan negatif")
elif bilangan == 0:
    print("Bilangan nol")
elif bilangan % 2 == 0:
    print("Bilangan positif genap")
else:
    print("Bilangan positif ganjil")