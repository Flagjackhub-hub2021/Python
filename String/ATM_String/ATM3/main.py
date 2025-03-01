"""
Pada Materi melakukan manipulasi string. Sekarang kita menggunakan str, int, bool.
"""

# Penggunaan method is dalam python menggunakan bool 

print("======= Penggunaan method is hanya menggunakan claas (Bool) =======")

a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]
c = a is b
print("Hasil dari :" " " + "a is b" " " + "=" + " " + str(c))

a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]
c = a is a
print("Hasil dari :" " " + "a is a" + " " + "=" + " " + str(c))

"""
Dalam penggunaan method pada case ini ialah apakah dua objek memiliki identitas yang sama, yang dimana mengacu pada lokasi memori tempat objek disimpan, dan 
Jika hasilnya True, jika dua objek tidak memiliki identitas yang sama yang dimana mengacu pada lokasi memori tempat objek disimpan maka hasilnya False
"""

print("\t")

# Penggunaan methond is dalam python menggunakan if and else, dan melakukan pemindahan elokasi

print("======= Penggunaan if and else dan melakukan pemindahan elokasi ======="  )

a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]

if a is b :
    print("Jika a is a maka hasilnya = True")
else:
    print("Jika b is a maka hasilnya \t " " = False")

# Melakukan elokasi terhadap hasil data
a = a 
b = a

if a is a :
    print("Maka a is a hasil dari elokasinya = True")
else :
    print("b = a adalah hasil dari elokasi = False")

"""
Pada pengunaan method is dalam python menggunakan if dan else serta melakukan elokasi (Pemindahan), yang dimana anda harus membuat sebuah varibale, dan sebuah class yang berupa
int di dalam sebuah array, serta melakukan pembuatan statmen if and else serta argumen, dan method di dalamnya. Jangan lupa untuk memberikan sebuah hasil dari statmen, setelah melakukan
pengisian sebuah isian terhadap statmen makah buatlah sebuah variable untuk melakukan pemindahan elokasi  sebagai contoh (a = b) setelah itu buatlah kembali sebuah statement baru untuk menentukan
hasil dari argumen berserta method (is). Dan jagan lupa untukk argumennya di samakan (a = a), dan begitupun untuk melakukan pemindagan (elokasi)
"""

print ("\t")

# Penggunaan methond is dalam python menggunakan switch_case dan melakukan pemindahan elokasi
print("======= Penggunaan switch_case dan melakukan pemindahan elokasi =======")
a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]

# Melakukan elokasi terhadap hasil data 
a = b
b = b

def switch_case(b):
    switcher = {
        1: "Jika a is b makah hasilnya = False",
        2: "Jika b is b makah hasilnya = True"
    }
    return switcher.get(b)
print(switch_case(1))
print(switch_case(2))

"""
Pada penggunaan switch_case, yang berbeda ialah cara untuk melakukan statment serta argumen pada pencarian swicth_case. Untuk variable dan melakukan pemindahan (elokasi) sebuah variable dan 
untuk melakukan penyamaan sebuah variable berserta isiannya (Data di dalam variable tersebut), sama seperti contoh case sebelumnya. Akan tetapi pada case ini kita menggunakan swicth_case pada 
dasarnya switch_case melakukan pengujian pada sebuah pilihan yang akan dipilih secarah satu persatu. Sedangkan if and else bisa langsung di tembak tanpa melakukan pengujian
"""

print("\t")
