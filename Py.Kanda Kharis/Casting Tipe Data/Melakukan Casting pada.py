# Penggunaan Tipe data Casting pada Integer

print("============Casting With Integer============")
Tanggal_tahun = 2023

#meminta pengguna menuliskan tahun lahirnya
Masukan_inputan_tahun_kelahiran = input("Kapan ulang tahun Anda : ")

#mengubah nilai yang diberikan pengguna menjadi int menggunakan fungsi int() dan menyimpannya di variabel baru
Masukan_inputan_tahun_kelahiran = int(Masukan_inputan_tahun_kelahiran)

#mengurangi tahun sekarang dengan tahun lahir yang diberikan pengguna dan sudah diubah menjadi int
Umur = Tanggal_tahun - Masukan_inputan_tahun_kelahiran

print(Umur)
print("\n")


# Penggunaan Tipe data Casting pada String

#  melakukan deklarasi pernyataan 

print("============Casting With String============")
Alamat_tinggal = ...

#  Penginputan data + melakukan pertanyaan dari (Alamat_tinggal)
Alamat_user = input ("Dimanakah Alamat Anda : ")

# Melakukan deklarasi outputan dari (Alamat_user)
Masukan_inputan_alamat_user = str ("Alamat_user")

# Outputnya dari barisan kedua
print (Alamat_user)
print("\n")


# Penggunaan Tipe data Casting pada Boolean yang bernilai True

# Pengguan Nilai True 1 ....

print("============Casting With Boolean (True)===========")
Berapakah_angkah_untuk_Menghasilkan_Nilai_True = ("1 ... ")

Nilai_True = input ("Nilai yang Menghasilkan Nilai True : ")

Masukan_angaka_bernilai_True = bool (Nilai_True)

Nilai_True = bool ("1 ....")

print (Nilai_True)
print("\n")


# Penggunaan Tipe data Casting pada Boolean yang bernilai False

print("============Casting With Boolean (False)===========")
Berapakah_angkah_untuk_Menghasilkan_Nilai_False = ("0, -1 ....")

Nilai_False = input ("Nilai yang Menghasilkan Nilai False : ")

Masukan_angaka_bernilai_False = bool (Nilai_False)

Nilai_False = bool (-0)

print (Nilai_False)
print("\n")

# """
# Penggunanan pada Nilai Bool (True and False), yang dimana ketika 
# kita melakukan deklarasi nilai True and False itu yang harus di perhatikan
# ialah: methodnya, penginputan dari inputan data yang akan di input 
# (Kolom yang akan di input). 
# """



# Penggunaan Tipe data Casting pada Float
print("============Casting With Float ===========")
Macam_macam_Nilai_Float = ("1.1 ....")

Nilai_Float = input ("Berapakah Nilai Float itu : ")

Masukan_Nilai_Float = float (1.1)


print (Masukan_Nilai_Float )
print("\n")

# """
# Penggunaan Casting pada nilai float ialah, yang dimana hanya bisa 
# menggunakan 1 nilai float pada setiap inputan seletah inputan pada string
# contohnya ialah:
# (Nilai_Float = input ("Berapakah Nilai Float itu : "))
# """



"""
Ini adalah short hand dari tulisan yang di atas
"""


print("============Ini Adalah Penulisan Short handnya============")
print("\n")

print("============Ini Adalah Inputan Integer============")
current_year = 2021
user_birth_year_input = input("What year were you born? ")

print(int(user_birth_year_input))
print("\n")


print("============Ini Adalah Inputan String============")
Alamat_tinggal = ("Jalan Merpati")
Alamat_user = input ("Dimana Alamat Anda?")

print(str(Alamat_user))
print("\n")


print("============Ini Adalah Inputan Boolean (True)============")
Berapakah_angkah_untuk_Menghasilkan_Nilai_True = (1)
Nilai_True = input ("Nilai yang Menghasilkan Nilai True : ")

print(bool(Nilai_True))
print("\n")


print("============Ini Adalah Inputan Boolean (False)============")
Berapakah_angkah_untuk_Menghasilkan_Nilai_True = (0)
Nilai_False = input ("Nilai yang Menghasilkan Nilai False : ")

print(bool(Nilai_False))
print("\n")


print("============Ini Adalah Inputan Float============")
Macam_macam_Nilai_Float = (1.1)
Nilai_Float = input ("Berapakah Nilai Float itu : ")

print(float(Nilai_Float))
print("\n")