while True:
    print("Menghitung Luas")
    print("---------------")
    print("1. Segitiga")
    print("2. Persegi Panjang")
    print("3. Selesai")
    print("---------------")
    pilihan = int(input("Pilihan Anda: "))

    if pilihan == 1:
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print("Luas segitiga:", luas)
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        luas = panjang * lebar
        print("Luas persegi panjang:", luas)
    elif pilihan == 3:
        print("Selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")