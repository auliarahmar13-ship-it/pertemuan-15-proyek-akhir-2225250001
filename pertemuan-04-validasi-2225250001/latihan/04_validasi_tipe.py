

try:
    benar = int(input("Jumlah soal benar dari 20: "))

    if benar < 0 or benar > 20:
        print("Masukkan ditolak: jumlah harus berada pada rentang 0 sampai 20.")
    else:
        persen = benar / 20 * 100
        print(f"Skor = {persen:.2f} persen")

        if persen >= 75:
            print("Tuntas")
        else:
            print("Belum tuntas")

except ValueError:
    print("Masukkan ditolak: jumlah harus berupa bilangan bulat.")