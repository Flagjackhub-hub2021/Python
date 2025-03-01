# Belum di tulis dan wajib di tulis setelah operator bitwise

# Code 1 dengan melakukan deklarasi satu persatu dengan 2 inputan dan 1 outputan
print("Melakukan pengitungan di python \n")

Lebar   = int(input("Masukan nilai Lebar   :"))
Panjang = int(input("Masukan nilai Panjang :"))
Hasil = Lebar * Panjang
print(Hasil)

Hasil_nilai = (Lebar, Panjang < 35)
print (Hasil_nilai)
print("\n")

# Code 1 dengan melakukan deklarasi 1 inputan dan 2 outputan 

user_input = int(input("Masukan angka Kurang dari 3 dan Lebih besar dari 6\n"))

kurang_dari = (user_input < 3)
print ("Kurang daro 3", kurang_dari)
# print (user_input < 3)

lebih_dari = (user_input > 6)
print ("Lebih dari 6", lebih_dari)
# print (user_input < 6)
print("\n")


# Code 2 dengan melakukan 2 inputan dan 1 outputan 
jauh  = float(input("Masukan nilai jauh  :"))
dekat = float(input("Masukan nilai dekat :"))
Hasil = jauh + dekat
print (Hasil)

Hasil_nilai = (jauh, dekat < 20)
print (Hasil_nilai)
print ("\n")


# Code 2 dengan menggabungkan 1 inputan dan menghasilkan 2 outputan 
user_input = float(input("Masukan angkan yang bernilai lebih dari 10 dan kurang dari 20\n"))

kurang_dari = (user_input < 10)
print("Kurang dari 10", kurang_dari)
# print (user_input < 10)

lebih_dari = (user_input > 20)
print("Lebih dari 20", lebih_dari)
# print (user_input > 20)
print("\n")


"""
Code 3
Menggunakan tipe data bool serta melakukan deklarasi satu persatu
(2 inputan dan 1 outputan)
"""

print("Melakukan pengitungan di python \n")

Tinggi = bool(input("Masukan Nilai Tinggi :"))
Luas   = bool(input("Masukan Nilai Luas :"))
Hasil_Nilai = Tinggi / Luas
print(Hasil_Nilai)

Hasil_Nilai = (Tinggi, Luas < 10)
print(Hasil_Nilai)
print("\n")


# Menggunakan tipe data bool serta melakukan deklarasi 1 inputan 2 outputan

user_input = bool(input("Masukan angka yang bernilai 5 dan 10 \n"))

kurang_dari = (user_input < 5)
print ("Kurang dari 5 :", kurang_dari)
# print (user_input > 5)

lebih_dari = (user_input > 10 )
print ("Lebih dari 10 :", lebih_dari)
# print (user_input > 10)


"""
Code dia atas adalah code refresni dari pengunaan salah satu cara
komperasi dan logika di dalam python

Catatan penting 

Dalam melakukan melakukan deklarasi satu persatu dengan 2 inputan dan 1 outputan
yang dimana ketika membuat variable baru dan elemen di dalamnya menggunakan 
operator pembanding yang dimana hal tersebut mendekripsikan hasil dari 
penjumlahan antar variable 1 dan yang lainnya dan hasil dari angka tersebut 
yang akan keluar dan menentukan true ataupun false. Jika menggunakan operasi Bool, wajib di pahami yang 
dimana anda harus menggetahui lebih mendalam cara kerja operasi pembanding, dikarena kan untuk membaca
sebuah pernyataan yang akan di implemntasikan ke code membutuhkan analisa dan jam terbang yang tinggi 
(Sudah sangat di pahami dan dihafal)

Contoh :
variable 1 = 5
variable 2 = 10

Hasilnya :
(5, True)
"""