
#Program menghitung rata-rata nilai

n1= float (input("Masukkan Nilai 1"))
n2= float (input("Masukkan Nilai 2"))
n3= float (input("Masukkan Nilai 3"))

rata = (n1 + n2 + n3) / 3

print("Rata-rata =", round(rata,2))
if rata >= 75:
    print("Status Lulus")
else: 
    print("Status Tidak Lulus")