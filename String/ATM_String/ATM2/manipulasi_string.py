# 1. Melakukan panipulasi string
# melakukan penyambungan string (concatenete)
Nama_Pertama = "Muhammad"
Nama_Tengah  = "Muslimin"
Nama_Akhir   = "Fadel"
Nama_Lengkap = Nama_Pertama + " " + Nama_Tengah + " " + Nama_Akhir 
print(Nama_Lengkap)

"""
Untuk melakukan penyambungan stringg concatenete pada python, yang harus di perhatikan ialah membuat variable berserta
string didalamnya, setelah itu buatlah variable baru untuk menyimpan semua variable yang telah dibuat sebelumnya. Dan pada 
variable baru tersebut harus ditulis kembali variable yang telah di ketik sebelumnya, dan jangan lupa untuk menaruh operator
tambah pada setiap variable yang ditulis. Dan setelah melakukan pengcodean operator tambah tulislah lagi string bisa single quote 
maupun double qoute, fungsinya ialah (Untuk melakukan space pada setiap variable yang akan dicodekan)
"""

# 1.1 Melakukan penyambungan string menggunakan (.join)
word   = ("Muhammad Muslimin Fadel")
result = "".join(word)
print(result)

"""
Penggunaan fitur .join yang dimana fitur ini melakukan penggabungan antar string. Dan bisa meliputi list, tuple. cara kerjanya sama seperti
melakukan penyambungan string yang menggunakan tanda operator (+)
"""

# 2. Menghitung panjang string
panjang = len(Nama_Lengkap)
print("panjang dari" + " "+ Nama_Lengkap + " =" + " " + str(panjang))

"""
Melakukan menghitung panjang string, yang dimana ketika kita akan melakukan penghitung pastikan anda apakah ingin melakukan 
pengitungan dengan variable yang sudah ada atau ingin membuat baru dan melakukan penghitungan. Sebagai contoh yaitu melakukan
penghitungan dari variable yang sudah ada, yang dimana buatlah sebuah variable baru, dan tambahkan sintax len jangan lupa masukan
variable dari keseluruhan variable yang telah dibuat (Variable yang akan diprint yang sebelumnya yang di tulis di dalam len),
jangan lupa pula untuk menambahkan class (str)
"""

print("\t")

# 3. Operator untuk string (Melakukan pengecekan terhadap sebuah string)

F = "F"
status = F in Nama_Lengkap
print(F + " " + "Ditemukan" + " " + Nama_Lengkap + " " + str(status))

D = "d"
status = D in Nama_Akhir
print(D + " " + "Ditemukan" + " " + Nama_Akhir + " " + str(status))

L = "l"
status = L in Nama_Pertama
print(L + " " + "Ditemukan" + " " + Nama_Pertama + " " + str(status))

"""
Pada case ini ialah melakukan pengecekan char yang kita inginkan disuatu variable yang telah dicodekan sebelumnya, akan tetapi 
sebelum melakukan pengecekan terlebih dahulu pastikan anda membuat variable baru, yang dimana variable tersebut akan mencamtumkan
variable yang ingin temukan (Variable yang telah dimasukan sebuah string), setelah itu makah anda harus melakukan penulisan code str
(class) supaya hasil ouputnya berupa sebuah kalimat (char). Bukan (int, float, atau boolean)
"""

print("\t")

# 4. Melakukan penambahan string (output)
print(5*"Fadel")
print("Fadel"*5)

"""
Code diatas adalah cara penulisan dan penambahan dari sebuah string tanpa harus di ketik termenerus
"""

print("\t")

# 5. Indexing
print("Index dari 0 : " + Nama_Lengkap [0])
print("Index dari 2 : " + Nama_Lengkap [2])
print("Index dari 7 : " + Nama_Lengkap [7])
print("Index dari 1- : " + Nama_Lengkap[-1])
print("Index dari -2 : " + Nama_Lengkap[-2])
print("Index dari -7 : " + Nama_Lengkap[-7])
print("Index dari 0:3 : " + Nama_Lengkap[0:3])
print("Index dari -0:-3 : " + Nama_Lengkap[-0:-3])

"""
Pada pengunaan Indexing yang dimana untuk cara kerjanya seperti menggunakan range, yang dimana ketika kita ingin menemukan
suatu char di dalam str, atau int dan kawan". Yang dimana untuk case ini anda harus melakukan penulisan dari sebuah variable 
dan dari variable tersebut akan di lakukan pengambilan data yang menggunakan array ataupun sebuah list di dalam array dengan 
menggunaka sebuah angka (int). Dan yang harus anda ketahui ialah penggunaan array ataupun list, dan untuk tinggkat lanjutnya 
maka anda harus menggetahui terlebih dahulu cara kerja sintax range pada python
"""

print("\t")

# 6. Pengunaan Item pada python
# Item paling kecil
print("Paling kecil :" + min(Nama_Lengkap))
# Item paling besar
print("Paling besar :" + " " + max(Nama_Lengkap))

"""
Penggunaan Item pada python, yang dimana berfungsi untuk menentukan (Mencari) sebuah char pada variable yang ingin dicari, akan tetapi
sebelum menyarinya maka anda harus menentukan variable mana yang akan dicari. Misalnya anda ingin mencari data didalam variable Nama_Lengkap
Maka anda harus memasukan variable tersebut di dalam variable(()) jika ingin membuat variable baru maka cara sama seperti cara sebelumnya. 
Dan cara ini bisa digunakan pada sebuah krakter saja (string)
"""

print("\t")

# 7. ASCII (Untuk mencari sebuah nilai menggunakan angka)
ascii_code = ord(" ")
print("ASCII code untuk spasi adalah" + " " + str(ascii_code))
data = 85
print("char untuk ASCII 85 adalah " + chr(data))

print("\t")

# 8. Operator dalam bentuk method bawahan
Data   = "Muhammad Fadel Del"
jumlah = Data.count("a")
print("Berapakah Jumlah a :" + " " + Data +" " + str(jumlah))

"""
Dalam pengunaan method (count) yang dimana hal ini akan mencari dan menghitung sebuat string dari variable utama. Yang bertujuan untuk
mengetahui. Contohnya mencari char (a) yang dimana method (count) akan melakukan pencarian dan penghitungan, dan yang harus diketahui 
ialah penempatan variable yang ingin dicari atau dimasukan di dalam pencarian ouputnya. Dan jangan bigung ketika ouputnya mengeluarkan semua
tulisan (str) dari variablenya, yang dimana hal itu melakukan penulisan kembali supaya kita bisa mengetahui berapa jumlah dari inputan yang
kita masukan
"""