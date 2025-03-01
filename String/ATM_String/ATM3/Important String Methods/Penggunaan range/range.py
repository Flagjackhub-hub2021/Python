# Penggunaan method slicing pada range dalam important string methods
Sampel   = [1,2,3,4,5,6,7,8]
testing  = list(range(3))
result   = Sampel, testing
print(result)

"""
Pada penggunaan method slicing pada range anda harus menggubaha terlebih dahulu cara penggunaannya serta cara kerjanya menggunakan list, untuk memahami cara kerja dari case range ini sama seperti cara kerja method is menggunakan 
int, binary, floting. Untuk simbol dari slicing yaitu menggunakan kurung siku untuk melakukan [] pengoperasian untuk mengisi angka Plus maupun min (1 atau -1) untuk mencari data yang akan di outputkan.() pada variable ke dua 
yang dimana wajib di tulis di bahasa
"""

# Penggunaan method find dengan string serta range, berguna untuk menentukan lokasi dari Data itu sendiri
print("\t")
Data    = "a, b, c, d, e, f, g, h, i"
Sampel  = "f"
jumlah  =  0
start   =  0

for x in range(len(Data)):
    f = Data.find(Sampel, start)
    if (f!= -1):
        start   = f + 1
        jumlah += 1
print("Lokasi data ditemukan di :" " " "=", start)

print("\t")

"""
Pada penggunaan method find dengan range, yang dimana cara kerja dan penggunaanya sangat lah mudah ketika anda sudah menggetahui tinggat lanjut dari penggunaan range dan tentunnya method .find, untuk cara kerjanya 
yaitu : Anda harus membuat sebuah Variable yang terdiri dari 4 yang dimana ke 4 variable tersebut berisi sebuah data utama, data sampel yang akan di ambil dari data utama dan variable dengan isian angka 0 yang bertujuan
untuk menggetahui yang mana yang akan di isi, dan variable star berguna untuk melakukan step pada pencarian data yang di inginkan, dan menuliskan code range seperti biasa dan untuk outputnya saya menggunakan cara assigmnet dan
tidak lupa untuk mencantupkan data (variable utama)
"""

# Penggunaan method find dengan string serta range, berguna untuk menentukan lokasi dari Data itu sendiri
Data   = "22.3, 44.5, 65.2, 77.1"
Sampel = "65.2"
jumlah = 0
start  = 0

for y in range(len(Data)):
    f = Data.rfind(Sampel, start)
    if (f!= -1):
        start   = f + 1
        jumlah += 1
print("Lokasi data ditemukan di '{}' antara '{}' dan '{}'", " ", (Data, Sampel) )

"""
Pada penggunaan method .rfind menggunakan range yang dimana cara kerja dan penggunaannya sama halnya seperti contoh di atas (mehtod .find)
"""


# Tugas buatlah semua method pada important string menggunakan range, mulai dari string hingga angka

"""
Tugas buatlah semua method pada importan string menggunakan if else, if elif else, dan switch_case +
wajib menggunakan shortcut
"""