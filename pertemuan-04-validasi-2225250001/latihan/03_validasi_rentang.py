
nilai = float(input("Masukkan nilai (0-100): "))

if 0 <= nilai <= 100:
    print(f"Nilai {nilai:.2f} valid.")
else:
    print("Nilai tidak valid.")