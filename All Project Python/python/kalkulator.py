while True :
    print("_____________________________________")
    print("Masukkan '1' untuk penjumlahan")
    print("Masukkan '2' untuk pengurangan")
    print("Masukkan '3' untuk perkalian")
    print("Masukkan '4' untuk pembagian")	
    print("Masukkan '0' untuk *keluar*")
    while True :
        try :
            user_input = int(input("Pilihan : "))
        except ValueError:
            print("Maaf anda salah memasukan angka / pilihan")
            continue
        else :
            break
    if user_input == 0 :
        print("TERIMA KASIH")
        break
    elif user_input == 1:
        while True :       
            try :
                angka1 = int(input("Masukan Angka-1 : "))
                angka2 = int(input("Masukan Angka-2 : "))
            except ValueError :
                print("anda harus memasukan angka !")
                continue
            else:
                break
        hasil = angka1 + angka2
        print(">>> Hasil Penjumlahan = ", hasil)
    elif user_input == 2:
        while True :       
            try :
                angka1 = int(input("Masukan Angka-1 : "))
                angka2 = int(input("Masukan Angka-2 : "))
            except ValueError :
                print("anda harus memasukan angka !")
                continue
            else:
                break
        hasil = angka1 - angka2
        print(">>> Hasil Pengurangan = ", hasil)
    elif user_input == 3:
        while True :       
            try :
                angka1 = int(input("Masukan Angka-1 : "))
                angka2 = int(input("Masukan Angka-2 : "))
            except ValueError :
                print("anda harus memasukan angka !")
                continue
            else:
                break
        hasil = angka1 * angka2
        print(">>> Hasil Perkalian = ", hasil)
    elif user_input == 4:
        while True :       
            try :
                angka1 = int(input("Masukan Angka-1 : "))
                angka2 = int(input("Masukan Angka-2 : "))
            except ValueError :
                print("anda harus memasukan angka !")
                continue
            else:
                break
        hasil = angka1 / angka2
        print(">>> Hasil Pembagian = ", hasil)
    else :
        print(">>> Angka Yang Anda Masukan Salah <<<")