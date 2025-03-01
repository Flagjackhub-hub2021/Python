# Penggunaan if else, if elif, else, dan switch_case

print("\t")

# Penggunaan method find dengan melakukan pengujian menggunakan if else pada string
Data  = "Muhammad Fadel"

if Data.find("Fadel") != -1 : # Data Untuk melakukan pengujian 
    print("Jika ditemukan makah hasilnya True")
else :
    print("Jika tidak di temukan maka hasilnya False (-1)")

"""
Pada penggunaan method find dengan melakukan penggujian menggunakan if else pada string. Yang dimana anda harus membuat sebuah variable baru berserta isian sebuah string menggunaka tuple, berguna sebagai ajuan
pada data yang ini ditemukan, setalah itu makah buat lah stament if dan masukan variable dari data utama dan menaru method find di depannya. Dan tidak lupa pulah melakukan penutupan menggungan string  serta
melakukan pengisian data, dan menambahkan simbol operator != (Tidak sama dengan) dan menambahan angka min setelahnya, berguna untuk membaca dari simbol yang di depannya. Contohnya ialah ketika anda menaruh sebuah 
data yang berisi nama yang tidak sesuai dari isian data dari varibale utama maka yang akan di input adalah min -1 (False), jika anda melakukan pengisian string yang ada data di varibale pertama maka bisa di pastikan
outputnya ialah True
"""

# Penggunaan method find dengan melakukan pengujian pada operator int yang menggunakan if else pada string
Data = ("1,2,3,4,5,6")

if Data.find("8") != -1 :
    print("Jika ditemukan makah hasilnya True")
else :
    print("Jika tidak ditemukan maka hasilnya False (-1)")

"""
Pada case ini yang dimana hanya menulisan menggunakan tuple saja, kenapa dikarankan pada method find hanya bisa melakukan pengoperasian berupa str saja, dan jika ingin benar mau mencari sebuah int, floting, binary, 
makah anda harus membuat ebuah deklarasi terlebih dahulu yang menggunakan range untuk menentukan atau mencari angka int maupun float serta binar serta bisa menggunakan simbol penutup [], ().
"""

print("\t")

# penggujian method rfind dengan melakukan pengujian menggunakan if else pada string
Data = "Saya suka makan"

if Data.rfind("suka") != -1 :
    print("Jika ditemukan makah hasilnya True")
else:
    print("Jika tidak ditemukan maka hasilnya False (-1)")

"""
Pada penggunaan method rfind menggunakan if dan else, sama seperti contoh pada penggunaan method find pada string
"""

# Penggunaan mehtod rfind dengan melakukan pengujian pada operator floting yang menggunakan if else pada string
Data  = ("22.54.77.82.93")

if Data.rfind("65") != -1 :
    print("Jika ditemukan makah hasilnya True")
else:
    print("Jika tidak di temukan maka hasilnya False (-1)")

"""
Pada case yang satu ini sama hal seperti contoh method find yang menggunakan angka int
"""

print("\t")

# penggunaan method fortmat dengan melakuakn pengujian pada operator string yang menggunakan if else pada tuple 
Data    = "Nama lengkap saya Muhammad Fadel"
inputan = "Senang betemu denganmu"

result = "Perkenal kan {}. ".format(Data)
if inputan == "senang bertemu denganmu":
    inputan += "senang bertemu denganmu"
else:
    result += "panggil saja Fadel"
    print(result, inputan)

