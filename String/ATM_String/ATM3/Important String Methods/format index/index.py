"""
index() Syntax -> str.index(sub[, start[, end]] )

indeks() Parameter
Metode ini index()mengambil tiga parameter:

                                            sub - substring yang akan dicari dalam stringstr.
                                            mulai dan akhir (opsional) - substring dicari dalam str[mulai:akhir]

indeks() Nilai Pengembalian :
                                Jika substring ada di dalam string, ia mengembalikan indeks terendah dalam string tempat substring ditemukan.
                                Jika substring tidak ada di dalam string, ini akan memunculkan pengecualian ValueError.
                                
"""

print("\t")

# Penggunaan cara format index pertama

# indeks() Hanya dengan argumen Substring

a = "Saya suka minum kopi".index('minum')
print("Mencari posisi kata minum di variable a = ",a)

a = "Saya suka minum kopi"
b = a.index('minum')
print("Mencari posisi kata minum di variable b = ",b)

a = "Saya suka minum kopi"
b = "minum"
c = a.index(b)
print ("Mencari posisi kata minum di variable c = ",c)

"""
Catatan: Metode index() mirip dengan find() . Satu-satunya perbedaan adalah find() mengembalikan -1 jika string yang dicari tidak ditemukan dan index() memunculkan pengecualian dalam kasus ini.
Pada code diatas yang dimana saya membuat 3 cara metode untuk melakukan pencarian, dan hasilnya tetap sama.
"""

print("\t")

"""
Indeks String Python() dengan Argumen Awal dan Akhir

Metode index()dalam Python digunakan untuk menemukan indeks kemunculan pertama substring dalam sebuah string. Ia mengembalikan indeks substring jika ditemukan, dan 
memunculkan jika substring tidak ada.ValueError
""" 

cari = "1 2 3 4 5 6 7 8 9 10"
print("Mencari Argumen Awal dan Akhir = ",cari.index("5", 8, 17))

"""
Pada penggunaan code diatas yang dimana cara untuk mendapatkan hasil dari angka "5", tersebut pertama anda harus menghitung posisi sebelah kanan awal ke angka 5.
Dan setelah itu hitunglah posisi terakhir pada angka "5" (Lanjut lah menghitung dari sebelah kiri hingga mencapai angka "5").
"""

cari = "Muhammad Fadel 13"
print("Mencari Argumen Awal dan Akhir = ",cari.index("Fadel", 9, len(cari)))

"""
Pada penggunaan code diatas yang dimana pada cara pertama saya menghitung baris (posisi) pada bagian sebelah kiri ke kanan (ke angka 13), dan setelah itu saya menambahkan 
fungsi bawaan array (len) dan menambahkan parameter "cari" guna untuk melakukan deklarasi Array.

catatan penting :
                    Fungsi len() dalam Python digunakan untuk menghitung jumlah elemen atau item dalam suatu urutan, koleksi, atau tipe data lainnya,
                    yang dimana 'len' akan mengembalikan jumlah karakter dalam string.
"""

print("\t")

"""
Metode Python String Index() menggunakan Pemahaman Daftar

Metode index()dalam Python digunakan untuk menemukan indeks kemunculan pertama substring dalam sebuah string. 
Contoh ini menggunakan pemahaman daftar untuk menemukan indeks beberapa substring dalam string.
"""
a = "Saya suka menikmati waktu saat malam hari"
b = ["menikmati", "malam", "Saya"]
c = [a.index(b) if b in a else -1 for b in b] 
print (c)

"""
Pada code yang diatas yang dimana kita melakukan pencarian menggunakan pemahaman daftar guna untuk mengetahui kemunculan pertama substring dalam sebuah string. 
Contohnya variable 'a' berguna sebagai data yang ingin dicari, pada variable 'b' sebagai inputan data yang telah dicari, dan pada variable 'c' yang dimana 
berguna untuk melakukan pencarian menggunakan method 'index' dan melakukan sub pada pada variable a dan b.

Catatan penting 

1.  Dalam pemrograman Python, sub adalah salah satu operator yang dapat digunakan dalam pemahaman daftar. Operator sub digunakan untuk mengganti nilai-nilai dalam 
    daftar berdasarkan kondisi tertentu, dan simbol pada sub ini ialah 'if', 'else' dan 'in'.

2.  Setelah else kenapa ada angka '-1' yang dimana berguna jika pada parameter variable 'b' tidak terdapat kalimat yang sesuai pada variable 'a' maka hasilnya akan -1 (not found).
"""