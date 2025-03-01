# Contoh penggunaan method format menggunakan Positional parameters
Nama = 'Fadel'
Umur = 20
Perkerjaan = "Blue Team"
Result = "Nama saya {}, Umur saya {}, Perkerjaan saya {}".format(Nama, Umur, Perkerjaan)
print(Result) 

"""
Pada code ini adalah bentuk dari default penulisan terhadap method format dengan menggunakan Positional parameters yang dimana kita tidak perlu harus menggisi
kurung kurawal dikarnakan string templat mereferensikan format()argumen sebagai '{0}' dan '{1}', argumen tersebut adalah argumen posisi.
"""

# Contoh penggunaan method format menggunakan Keyword parameters
Nama = 'Muhammad'
Umur = 20 
Result = 'Nama saya {0}, Umur saya {1}'.format(Nama, Umur)
print(Result) 

"""
Pada code ini adalah bentuk default penulisan terhadap method format menggunakan Keyword parameters yang dimana 
Python biasanya menetapkan placeholder dengan indeks default dalam urutan  seperti 0, 1, 2, 3…. untuk mengakses nilai yang 
diteruskan sebagai parameter. 
"""

# short hand syntax format in import string menggunakan keyword parameters
print("Nama {0}, Umur {1}".format("Muhammad Fadel", 20))

# Short hand syntax format in importan string menggunakan Positional parameters 
print("Nama {}, Umur {}".format("Muhammad Fadel", 20))

print("\t")

# Memformat String menggunakan Urutan Escape (\n, \t, \\, \', \"", \A )
Nama = "Muhammad Fadel"
Umur = 20
Perkerjaan = "programer"
Hasil = "\nNama saya {} \nUmur saya {} \nPerkerjaan saya {}".format(Nama, Umur, Perkerjaan)
print(Hasil) # Pada penggunaan menggunakan Escape '\n' yang dimana kegunaan dari Escape ini memecah string menjadi baris baru

print("\t")

Nama = "Muhammad Fadel"
Umur = 20
Perkerjaan = "programer"
Hasil = "Nama saya {}\t Umur saya {}\t Perkerjaan saya {}\t".format(Nama, Umur, Perkerjaan)
print(Hasil) # Pada penggunaan menggunakan Escape '\t' yang dimana kegunaan dari Escape ini Menambahkan tab horizontal

print("\t")

Nama = "Muhammad Fadel"
Umur = 20
Perkerjaan = "programer"
Hasil = "Nama saya {}\\Umur saya {}\\Perkerjaan saya {}".format(Nama, Umur, Perkerjaan)
print(Hasil) # Pada penggunaan menggunakan Escape '\\' yang dimana kegunaan dari Escape ini Mencetak garis miring terbalik

print("\t")

Nama = "Muhammad Fadel"
Umur = 20
Perkerjaan = "programer"
Hasil = "\'Nama saya {}\' \'Umur saya {}\' \'Perkerjaan saya {}\' ".format(Nama, Umur, Perkerjaan)
print(Hasil) # Pada penggunaan menggunakan Escape '\'' yang dimana kegunaan dari Escape ini Mencetak Mencetak satu kutipan

print("\t")

Nama = "Muhammad Fadel"
Umur = 20
Perkerjaan = "programer"
Hasil = "\"Nama saya {}\" \"Umur saya {}\" \"Perkerjaan saya {}\" ".format(Nama, Umur, Perkerjaan)
print(Hasil) # Pada penggunaan menggunakan Escape '\"' yang dimana kegunaan dari Escape ini Mencetak Mencetak kutipan ganda

print("\t")

Nama = "Muhammad Fadel"
Umur = 20
Perkerjaan = "programer"
Hasil = "\aNama saya {}\a \aUmur saya {}\a \aPerkerjaan saya {}\a ".format(Nama, Umur, Perkerjaan)
print(Hasil)

"""
Pada penggunaan menggunakan Escape '\a' yang dimana kegunaan dari Escape ini yang dimana melakukan 1X space dalam setiap value isian tuple pada tiap variable
"""

print("\t")

# Short hand syntax format with urutan Escape (\n, \t, \\, \', \"", \A ) in importan string 
print("\nNama {} \nUmur {}".format("Muhammad Fadel", 20))
print("Masakan mama {}\t for fuctere {}\t".format("Sangat enak sekali", "Keep grow 🤖"))
print("Saya akan {}\\Dan akan menjadi {}".format("lulus tepat waktu", "lulusan terbaik"))
print("\"Keep {}\" \"Pray {}\"".format("Grow", "Hard"))
print("Saya suka melakukan perkerjan menggunakan {}\a dan {}".format("otak", "otot"))

"""
pada penggunaan  Memformat String menggunakan Urutan Escape (\n, \t, \\, \', \"", \A ) Anda dapat menggunakan dua atau lebih karakter khusus dalam sebuah string 
untuk memformat string atau menjalankan perintah. Karakter-karakter ini disebut escape sequence. Urutan Escape di Python dimulai dengan garis miring terbalik (\). 
Misalnya, \n adalah rangkaian escape yang makna umum huruf n secara harafiah diloloskan dan diberi makna alternatif – baris baru.
"""

print("\t")

# Contoh penggunaan pemformatan angka integer, biner, hexadecimal, oktal dengan method format dalam importan string 

Data = 123
print("Menggunakan pemformatan angka dengan format 'Decimal' = {:d}".format(Data))

"""
Pada code diatas yang dimana pemformatan angka dengan format '{:d}', yang bertujuan untuk  melakukan hitungan bilangan bulat desimal
""" 

Data = 10
print("Menggunakan pemformatan angka dengan format 'Int' = {:b}".format(Data))

"""
Pada code diatas yang pemformatan angka dengan format '{:b}', dimana kita menggunakan angka integer sebagai inputan yang 
bertujuan untuk menghasilkan output angka biner, serta dari angka tersebut akan melakukan menambahan posisi terhadap bilang biner 
yang dioutputkan (Dimasukan sebagai data yang akan di format).
"""

Data = 0b001
print("Menggunakan pemformatan angka dengan format 'Biner' = {:o}".format(Data))

"""
Pada code diatas yang pemformatan angka dengan format '{:o}', dimana kita menggunakan angka biner sebagai inputan yang bertujuan
untuk menghasilkan outputkan angka oktal, dan yang harus anda ketahui ialah ketika menginput angka biner yang akan ke konversi ke
bilang oktal (hasil dari inputan yang akan dicari). Serta dari angka 
"""

Data = 0x06
print("Menggunakan pemformatan angka dengan format 'Hexadecimal' = {:X}".format(Data))

"""
Pada code diatas yang pemformatan angka dengan format '{:X}', dimana Bilangan heksadesimal adalah sistem bilangan yang 
menggunakan basis 16. Sistem ini umumnya digunakan dalam pemrograman komputer untuk mewakili alamat memori dan data. Setiap digit 
heksadesimal mewakili 4 bit biner. Digitnya mencakup angka 0-9 dan huruf A-F, dengan A mewakili nilai 10 dan seterusnya hingga 
F yang mewakili nilai 15, dan perrhitungan disesuaikan dengan deretan angka dari bagian sebelah kanan sistem bilangan.
"""

Data = 0x6A
print("Menggunakan pemformatan angka dengan format 'Hexadecimal' = {:x}".format(Data,))
"""
Pada code diatas yang pemformatan angka dengan format '{:x}', dimana sama seperti dokumentasi diatas akan tetapi pada code diatas
simbol digunakan ialah ':X' yang dimana akan menghasilkan format heksadesimal (huruf besar). Dan pada penggunaan code ':x' akan
menghasilkan format heksadesmal (huruf kecil).
"""


a = 2
b = 3
Result = 2**3 # Melakukan deklarasi pada inputan numerik pada penggunaan format Notasi eksponensial 
print("Mengguanakan pemformatan angka dengan format 'Notasi eksponensial (huruf besar E)' = {:E}".format(Result))

Data = 2**3 # Melakukan pengolahan serta pengoutputan dalam variable itu sendiri
print("Mengguanakan pemformatan angka dengan format 'Notasi eksponensial (huruf besar E)' = {:E}".format(Data))

# Menggunakan short hand yang berguna untuk melakukan penggolahan secara instan
print("Mengguanakan pemformatan angka dengan format 'Notasi eksponensial (huruf besar E)' = {:E}".format(2**3))

"""
Pada penggunaan code menggunakan format notasi eksponensial yang dimana kita bisa menggunakan 3 cara pencarian untuk penggunaan simbol '{:E}' yang dimana akan 
menginputkan hasil menggunakan huruf besar pada hasil outputan, sedangkan menggunakan simbol '{:e}' yang dimana akan menginput hasil huruf kecil pada hasil 
outputan, dan lebih disarankan menggunakan code diatas karna merupakan salah satu struktur code yang bersih (Clean code) dan mudah untuk dipahami bahkan 
untuk orang yang baru belajar bahasa pemrograman python.
"""

Data = 1
print("Menggunakan pemformatan angka dengan format 'Menampilkan nomor titik tetap (Default: 6)' = {:F}".format(Data))

"""
Pada code diatas yang pemformatan angka dengan format '{:F}', yang dimana akan melakukan penambahan 6 angka dibelakang nomor yang diinputkan, yang berarti ketika
kita melakukan operasi arikmatika menggunakan perkalian '2*2' yang dimana hasil input dari pengoperasian tersebut akan otomatis menambah angka '0' sebanyak 6X
"""

Data = 2 #Padaa code diatas yang pemformatan angka dengan format '{:G}', yang dimana sama halnya menggunakan pemformatan menggunnakan '{:d}' 
print("Menggunakan pemformatan angka dengan format 'Menampilkan nomor titik tetap (Default: 6)' = {:G}".format(Data))

Data = 3 
print("Menggunakan pemformatan angka dengan format 'Persentase. Kalikan dengan 100 dan beri % di akhir' = {:%}".format(Data))

"""
Pada code diatas yang pemformatan angka format '{:%}', yang dimana kita melakukan penginputan angka numerik terutama pada 'int' yang dimana setiap angka yang di
input maupun yang akan di operasikan menggunakan operator arikmatika akan menambahkan 8X angka '0' dibelakang hasil inputakn (angka yang telah di output)
"""

print("\t")

# Contoh penggunaan lebar minimum dengan angka integer

Data = 1234 
print("Menggunakan pemformatan angka dengan format 'lebar minimum dengan angka integer' = {:5d}".format(Data))

"""
Pada penggunaan code yang diatas yang dimnana kita akan melakukan padding terhadap hasil outputan dari inputan angka integer menggunakan format '{:d}', dan yang 
harus di perhatikan ialah hasil dari pemformatan menggunakan lebar minimum dengan angka integer akan di geser dari kiri ke kanan. Pastikan nilai angka dari 
pemformatan ({:'isian angka'd''}) tidak lebih dari inputan isian value terhadap simbol '{:}'. 
"""

# Contoh penggunaan angka floting pada padding (melakukan transisi posisi) serta  Melakukan pembulatan angka terahkir

Data = 13.2265478
print(
    "Menggunakan pemformatan angka dengan format 'floting pada padding (melakukan transisi posisi) serta  Melakukan pembulatan angka terahkir' = {:08.5f}".format(Data)
    )

"""
Pada penggunaan code diatas, yang dimana kita membuat sebuah variable berserta isian value dengan menggunakan angka floting serta melakukan transisi posisi pada angka
floting dan melakukan pembualatan terhadap 2 angka terakhirnya '78'. dan perlu diketahui bawah dengan menggunakan ini anda harus sangat hati" terhadap pengisian 
sebuah isian value pada angka terakhir tersebut '{:isian padding(Transisi posisi. isan value terakhir(angka yang akan dibulatkan))}'
"""

print("\t")

# Contoh penggunaan pemformatan angka dengan padding menggunakan numerik (int, floating, biner, oktal, hexadecimal) dengan method format dalam importan string 

Data = 1234567 #Pada pernyataan kedua, terlihat lebar (2) lebih kecil dari angka (1234567), sehingga tidak memakan spasi ke kiri tetapi juga tidak memotong angkanya. 
print("Menggunakan pemformatan angka integer dengan format 'lebar tidak berfungsi untuk angka yang lebih panjang dari padding' = {:2d}".format(Data))

Data = 1234567 #Pada pernyataan kedua, terlihat lebar (2) lebih kecil dari angka (1234567), sehingga tidak memakan spasi ke kiri tetapi juga tidak memotong angkanya. 
print("Menggunakan pemformatan angka floting dengan format 'lebar tidak berfungsi untuk angka yang lebih panjang dari padding' = {:02.0f}".format(Data))

"""
Pada penggunaan code menggunakan pemformatan angka floting dengan format lebar tidak berfungsi untuk angka yang lebih panjang dari padding yang dimana kita 
menggunakan cara pembulatan dikarnakan pada floting penggunaan simbol '{:}' dan kasus diatas yang dimana lebar tidak berfungsi sehingga akan dilakukan cara
pembulatan terhdapat digitnya. 
"""

Data = 0b010
print("Menggunakan pemformatan angka biner dengan format 'lebar tidak berfungsi untuk angka yang lebih panjang dari padding' = {:1.0f}".format(Data))

"""
Pada penggunaan code Menggunakan pemformatan angka biner dengan format lebar tidak berfungsi untuk angka yang lebih panjang dari padding yang dimana kita tetap
menggunakan cara pembulatan pada biner, dikarenakan ketika hanya menggunakan pemformatan format '{:d}' semata, itu tidak sama hasil dari output biner itu sendiri 
oleh karna itu kita melakukan pembulaatan menggunakan pemformatan format '{:f}' yang berguna sebagai sarana pencarian terhadap penggunaan angka biner dan hasil dari
penggunaan pemformatan format tersebut pada inputan biner akan menghasilkan outputan yang 100% akurat
"""

Data = 0o11
print("Menggunakan pemformatan angka oktal dengan format 'lebar lebar tidak berfungsi untuk angka yang lebih panjang dari padding = {:1.0f}".format(Data))

"""
Pada penggunaan code Menggunakan pemformatan angka biner dengan format lebar tidak berfungsi untuk angka yang lebih panjang dari padding yang dimana kita tetap 
menggunakan cara pembulatan pada biner, dikarenakan ketika hanya menggunakan pemformatan format '{:d}' semata, itu tidak sama hasil dari ouput oktal yang di bulatkan
ke bilangan decimal itu sendiri oleh karna itu kita melakukan pembulatan menggunakan pemformatan format '{:f}' yang berguna sebagai saran pencarian terhdap penggunaan angka
biner dan hasil dari penggunaan pemformatan format tersebut pada inputan oktal untuk menyamai hasil outputan pada angka decimal itu sendiri.
"""

Data = 7 + 0x7  
print("Menggunakan pemformatan angka biner dengan format 'lebar tidak berfungsi untuk angka yang lebih panjang dari padding' = {:1.0f}".format(Data))

"""
Pada penggunaan code menggunakan penggabungan pemformatan operator tambah '+' pada angka decimal dan angka hexadecimal, dengan format lebar tidak befungsi untuk angka yang lebih
panjang dari padding yang dimana penggabungan format ini berguna untuk menggetahui konversi pada angka decimal ke oktal, dan ketika hanya menggunakan pemformatan '{:d}' semata, itu
tidak sama hasil dari outputan yang dibulatkan ke bilangan penggabungan tersebut (decimal dan hexadecimal), oleh karna itu kita melakukan pembulatan menggunakan pemformatan format '{:f}'
yang berguna sebagai saran pencarian terhadap penggabungan angka descimal dan angka hexadecimal dan hasi dari penggunaan pemformatan format tersebut akan menghasilkan outputan yang 100% akurat.
"""

# Contoh penggunaan operator perataan (>, <, ^, =) dalam angka serta menggunakan pemformatan angka

Data = 5
print("Penggunaan operator perataan '>' = {:>5d}".format(Data))

"""
Pada penggunaan code diatas yang dimana kita akan melakukan deklarasi menggunakan 1 variable berserta isiannya (value), serta menggunakan simbol operator '>' yang dimana kegunaannya yaitu
melakukan sejajar kanan dengan ruang tersisa, yang dimaksud ruang tersisa ialah penginputan padding (memasukan angka) contoh angka '5' yang dimana berperan sebagai penanda (padding tersebut)
dan perlu perhatikan ialah melakukan penginputan nilai terhadap sebuah variable, dikarnakan ketika kita menggunakan jenis pemformatan angka yang tidak sama layaknya penginputan nilai (angka Numerik)
akan penyebabkan terjadi error saat melakukan running.
"""

Data = 0x001
print("Penggunaan operator perataan '<' = {:5x}".format(Data))

"""
Pada penggunaan code diatas yang dimana kita akan melakukan deklarasi menggunakan 1 variable berserta isiannya (Value), serta menggunakan simbol operator '<' yang dimana kegunaannya yaitu 
melakukan rata kiri pada ruang yang tersisa, yang dimaksud ruang tersisa ialah penginputan padding (memasukan angka) contoh angka '5' yang dimana berperan sebagai penanda (padding tersebut)
dikarnakan ketika kita menggunakan jenis pemformatan angka biner ke decimal 
"""

Data = 12.123458
print("Penggunaan operator perataan '^' = {:^16.6f}".format(Data))


"""
Pada penggunaan code diatas yang dimana kita akan melakukan deklarasi menggunkan 1 variable berserta isiannya (Value), serta menggunakan simbol operator '^' yang dimana kegunaannya yaitu 
melakukan rata tengah dengan ruang yang tersisa, yang harus anda ketahui tentang penggunaan code ini ialah ketika anda melakukan penginputan padding (memasukan angka) dan melakukan penginputan 
nilai terhadap jenis pemformatan angka menggunakan floting '{f}' pastikan anda melakukan pengisian angka yang benar terhadap nilai padding serta nilai terhadap jenis pemformatan angka.
Contohnya : '{:^6.6f}' yang dimana pada nilai padding (6 sebelum 6f) tidak akan berpindah meskipun kita sudah memasukan jenis operator '^' itu di sebabkan karena nilai awal (12) value pada variable
yang diinputkan tidak melebih niali tersebut. Sehingga inputan terhadap pemformatan angka pada padding tidak akan pindah dari tempatnya (ke tengah) meskipun kita menambahakan/melebihkan nilai jenis 
pemformatan angka dari variable berserta isiannya (Value) '123458'.
"""

Data = 0o10
print("Penggunaan operator perataan '=' = {:=5o}".format(Data))

"""
Pada penggunaan code diatas yang dimana kita akan melakukan deklarasi menggunakan 1 variable beserta isiannya (Value), serta menggunakan simbol '=' yang dimana kegunaannya yaitu
melakukan memaksa tanda (+) (-) ke posisi paling kiri yang harus anda ketahui tentang penggunaan code ini ialah ketika anda melakukan penginputan padding (memasukan angka) dan melaukan 
penginpuyan nilai terhadap jenis pemformatan angka menggunak oktal '{o}' contoh angka '5' yang dimana berperan sebagai penanda (padding tersebut).
"""

print("\t")

# Pemformatan string dengan padding

Data = 'Muhammad Fadel'
print("Penggunaan operator perataan '>' = {:>17}".format(Data))

"""
Pada penggunaan code diatas yang dimana kita, membuat sebuah variable serta melakukan deklarasi terhadap isian (Value) yang menggunakan string dalam tuple dan menggunakan menggunakan simbol operator '>' 
yang dimana kegunaannya yaitu melakukan sejajar kanan dengan ruang tersisa, yang dimaksud ruang tersisa  ialah penginputan padding (memasukan angka). Dan yang perlu anda ketahui ialah saat penginputan padding
yang dimana pada penggunaan string kita anda ingin menggisi padding maka hitunglah terlebih dahulu abjad pada kalimat yang anda masukan. Contohnya 'Muhammad Fadel' pada abjad tersebut memiliki 13 abjad + 1x space
yang dimana saat penginputan padding anda harus melebihi masukan abjad pada value dalam variable tersebut. 
"""

Data = "Muhammad Fadel"
print("Penggunaan operator perataan '<' = {:17}".format(Data))

"""
Pada penggunaan code diatas yang dimana kita, membuat sebuah variable serta melakukan deklarasi terhadap isian (Value) yang menggunakan string dalam tuple dan menggunakan menggunakan simbol operator '<' 
yang dimana kegunaannya yaitu rata kiri pada ruang yang tersisa, yang dimaksud ruang tersisa  ialah penginputan padding (memasukan angka). Dan yang perlu anda ketahui ialah saat penginputan padding
yang dimana pada penggunaan string kita anda ingin menggisi padding maka hitunglah terlebih dahulu abjad pada kalimat yang anda masukan.
"""

Data = "Muhammad Fadel"
print("Penggunaan operator perataan '^' = {:^20}".format(Data))

"""
Pada penggunaan code diatas yang dimana kita, membuat sebuah variable serta melakukan deklarasi terhadap isian (Value) yang menggunakan string dalam tuple dan menggunakan simbol operator '^'
yang dimana kegunaan yaitu Rata tengah dengan ruang yang tersisa yang dimaksud ruang tersisa  ialah penginputan padding (memasukan angka). Dan yang perlu anda ketahui ialah saat penginputan padding
yang dimana pada penggunaan string kita anda ingin menggisi padding maka hitunglah terlebih dahulu abjad pada kalimat yang anda masukan. Contoh Muhammad Fadel' pada abjad tersebut memiliki 13 abjad + 1x space
yang dimana kita harus menggetahui jenis operator yang dipakai contoh pada penggunaan operator ini, saat anda melakukan penginput nilai maka pasting masukan angka lebih dari '17' yang berguna untuk 
melakukan padding ke tengah.
"""

"""
catatan penting pada penggunaan Pemformatan string dengan padding

pada penggunaan pemformatan string dengan padding yang dimana saat kita menggunakan operator '=' (Memaksa tanda (+) (-) ke posisi paling kiri) complie pada python akan menggeluarkan pernyataab error karna pada
penggunaan operator '=' dalam pemformatan string tidak di dukung oleh python itu sendiri.
"""

print("\t")

# Memotong string dan numerik (int, decimal, biner, oktal, floting) dengan format() 

Data = 'Muhammad'
print("Melakukan pemmotongan abjad pada kalimat string  = {:.3}".format(Data))

"""
Pada code diatas yang dimana metode melakukan pemmotongan abjad pada kalimat string yang dimana cara kerjanya sama seperti melakukan pemformatan menggunaakan jenis format '{f}' pada pemformatan nilai floting-point
yang dimana ketika kita memasukan inputan simbol '.' dan memasukan angka setelah simbol itu yang dimana menentukan lebar minimum untuk string tersebut (Nilai dari value pada variabel tersebut).
Contohnya 'Muhammad' dan nilai yang dimasukan untuk memotong string ialah '34', yang dimana saat di run akan menggeluarkan 3 abjad pertama pada kalimat 'Muhamad' saja.
"""

Data = '1234324'
print("Melakukan pemmotongan angka pada nilai int = {:.3}".format(Data))

"""
Pada code diatas yang dimana  metode pemformatan string di python hanya dapat digunakan untuk memformat tipe data string dan bukan numerik (int, decimal, biner, oktal) kecuali floting/floting-point  Oleh karena itu, 
jika ingin memotong numerik, perlu diubah terlebih dahulu menjadi string.
"""

Data = 4.1342242
print("Melakukan pemmotongan angka pada nilai int = {:.5f}".format(Data))

"""

"""

# Penetapan Tipe lain yang berguna

print("Ini adalah contoh penggunaan bilangan bulat desimal tak bertanda '%u' {:i%} hasil".format(10))


# class orang:
#     Nama = 'Fadel'
#     Umur = 20
# print("Nama lengkap saya {o.Nama} Umur saya {o.Umur}".format(o=orang()))