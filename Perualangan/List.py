Jumlah_buku =  ["Buku1","Buku2","Buku3","Buku3",'Buku4']
print(Jumlah_buku[0])
print(Jumlah_buku[1])
print(Jumlah_buku[2])
print(Jumlah_buku[3])
print(Jumlah_buku[4])

#Pada code diatas yang mana penulisan code list yang sangat standar. Penulis memhuat sebuah variabel berserta isian parameternya.
#Dari isian paramternya terdapat 4 value yang masing-masing valuenya merupakan string yang sama yaitu buku dan angka sebagai pembedanya.
#Dan penulis melakukan deklarasi panggilan isian parameternya secara satu persatu agar penulis mengetahui berapakah jumlah isian value dari parameter variabel buku #

print("\b")

Jumlah_buku =  ["Buku1","Buku2","Buku3","Buku3",'Buku4']
print(Jumlah_buku)

print("\b")

#Pada code diatas yang mana penulisan code list yang sangat stanar. Penulis membuat sebuah variabel berserta isiannya parameternya.
#Dari isian parameternya terdapat 4 value yang masing-masing valuenya merupakan string yang sama yaitu buku dan angka sebagai pembedanya.
#Dan penulis hanya melakukan satu kali deklarasi (print), agar melihat outpunya sapa seperti inputan value parameternya #


Daftar_baju = ["Merah", "Hitam", "Hijau", "Putih"]
Daftar_baju.append("Coklat ")
print(Daftar_baju)

#Kegunaan dari list methods append yaitu Menambahkan item ke akhir daftar #

Daftar_baju = ["Merah", "Hitam", "Hijau", "Putih"]
Daftar_baju.remove("Hijau")
print(Daftar_baju)

# Kegunaan dari list methods remove yaitu Memerlukan nilai spesifik sebagai argumen untuk menghapus kemunculan pertama elemen dengan nilai yang ditentukan.#

Daftar_baju = ["Merah", "Hitam", "Hijau", "Putih"]
Daftar_baju.extend("Pink")
print(Daftar_baju)

# Kegunaan dari list methods exted yaitu Menambahkan item daftar dan iterable lainnya ke akhir daftar#

Daftar_baju = ["Merah", "Hitam", "Hijau", "Putih"]
Daftar_baju.insert(0, "Coklat")
print(Daftar_baju)

# Kegunaan dari list methods insert yaitu menyisipkan item pada indeks yang ditentukan #

Daftar_baju = ["Merah", "Hitam", "Hijau", "Putih"]
Daftar_baju.pop(3)
print(Daftar_baju)

#Kegunaan dari list method pop yaitu memerlukan angka indeks (posisi) sebagai argumen untuk menghapus item terakhir atau item berdasarkan indeks yang diberikan. 
# Metode ini juga mengembalikan item yang dihapus, yang dapat berguna untuk memproses data yang dihapus atau menyimpannya di tempat lain #

Daftar_baju = ["Merah", "Hitam", "Hijau", "Putih"]
Daftar_baju.clear()
print(Daftar_baju)

#Kegunaan dari list method clear yaitu Menghapus semua item dari daftar #

Daftar_baju = ["p","i","n","k","h","i","j","a","u"]
index= Daftar_baju.index ("k")
print(index)

#Kegunaan dari list method index yaitu Mengembalikan indeks item pertama yang cocok. fungsi dari mehtod ini mecari tempat lokasi dan menghitung tempatnya dalam bentuk arikmatika#

Daftar_baju = ["p","i","n","k","h","i","j","a","u"]
index= Daftar_baju.count ("i")
print(index)

#Kegunaan dari list method count yaitu mengemabalikan jumlah item tertentu dalam daftar. fungsi dari method ini menjumlahkan hufur atau angka yang berada dalam isian parameter #

