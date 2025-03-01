"""
Penggunaan Operator_Assigemnt menggunakan sintax sort (Melakukan deklarasi) serta melakukan operasi arikmatika
"""

print("Penulisan menggunakan 1. Variable dan langsung di eksekusi")
a = 5
print ("Nilai a =", a)
# Ini  adalah Variable dan nilai acuan yang akan di eksekusi, dan bersifat wajib di tulis sebelum melakukan oeprasi
a += 1 
print("Nilai a =", a)
a -= 2
print("Nilai a =", a)
a *= 5
print("Nilai a =", a)
a /= 3
print("Nilai a =", a)
a %= 5
print("Nilai a =", a)
a **= 2
print("Nilai a =", a)
a //= 4
print("Nilai a =", a)

"""
Cacatan penting!!!

Yang dimana pada pengunaan operator assigemnt dan cara kerjanya ialah, hal pertama yang harus dibuat ialah
sebuah variable dengan nilainya. Yang dimana akan menjadi acuan untuk melakukan pengoperasian pada simbol
yang ingin di pakai, tetapi pada case ini kita memakai operasi arikmatika. Cara kerja dari operasi ini ialah
mengambil data dari variable acuan sehingga ketika ingin menambahkan maka nilai dari hasil dari cuanlah
yang akan di eksekusi. 
"""

"""
Penggunaan Operator_Assigemnt menggunakan sintaks panjang (Melakukan deklarasi) serta melakukan operasi Bitwise
"""
print("\t")

# Pengunaan Assigemnt dalam operator Logika AND
b = True
print("Nilai b =", b)
# Ini  adalah Variable dan nilai acuan yang akan di eksekusi, dan bersifat wajib di tulis sebelum melakukan oeprasi
b &= False
print("Nilai b akan di konversi menjadi", b)
b = False
print("Nilai b =", b)
b &= True
print("Nilai b akan di konversi menjadi", b)

print("\n")

# Pengunaan Assigemnt dalam operator Logika OR
b = False
print("Nilai b =", b)
b |= True
print("Nilai b akan di konversi menjadi", b)
b = True
print("Nilai b =", b)
b |= False
print("Nilai b akan di konversi menjadi", b)

print("\n")

# Pengunaan Assigemnt dalam operator Logika XOR
b = True
print("Nilai b =", b)
b ^= False
print("Nilai b akan di konversi menjadi", b)
b = False
print("Nilai b =", b)
b = True
print("Nilai b akan di konversi menjadi", b)

print("\n")

# Pengunaan Assigemnt dalam operator Logika NOT
b = False
print("Nilai b =",b)
b = True
print("Nilai b akan di konversi menjadi", b)
b = True
print("Nilai b =", b)
b = False
print("Nilai b akan di konversi menjadi", b)


"""
Pada penggunaan Operatir_Assigemnt di gabungkan ke Operator Logika. Yang dimana harus menuliskan 2 kali variable utama (yang akan di eksekusi),
yang supaya operator tersebut tidak bigung untuk membacanya ketika akan di operasikan pada variable utama yang sudah ditulis
dan penggunaanya supaya ketika variable utama (1), memiliki turunan yang sudah di konversi, maka hukum penulisan variable yang 
kedua wajib. supaya bisa di tau asil, serta dalam programan tidak akan bigung ketika membaca
"""

print("\t")

# Pengunaan Assigemnt dalam operator Bitwise
# Contoh pengunaan bilangan decimal pada operator Assigemnt ke operator Bitwise
c = 5
print("Nilai c =", c)
c <<= 2
print("Nilai c akan di geser 2 (<<) kali =", c)
c >>= 1
print("Nilai c akan di geser 1 (>>) kali =", c)

print("\n")

# Contoh pengunaan bilangan biner pada operator Assigemnt ke operator Bitwise
c = 0b000110
print("Nilai c =", format(c,"06b"))
c <<= 2
print("Nilai c akan di geser (<<) menjadi =", format(c,"06b"))
c >>= 1
print("Nilai c akan di geser (>>) menjadi =", format(c,"06b"))

"""
Pada penggunaan operator assigemnt ke operator bitwise (Biner, Decimal) yang dimana penulisannya sama seperti 2 contoh code di atas
yang membedahkan ialah penulisan sintax. Yang pertama tampa tambahan code (format) yang kedua memakai code bawahan 
python (format), yang tampah format akan menghasilkan nilai outputan decimal dan sedangkan menggunakan code bawahan
python (format) akan menghasilkan nilai outputan biner.
"""

print("\t")

"""
Penggunaan Operator_Assigemnt menggunakan sintax Long dan menggabungkan, serta melakukan operasi arikmatika
"""

print("Penulisan menggunakan 4. Variable dan di gabungkan ke beberapa variable")
a = 1
b = 2
c = b + 1
d = a - 1
e = b * 3
f = a % 2
g = b / 4
h = a ** 6
j = b // 7
print("Nilai dari a", a)
print("Nilai dari b", b)
print("Nilai gabungan, berserta konversinya b =", c)
print("Nilai gabungan, berserta konversinya a =", d)
print("Nilai gabungan, berserta konversinya b =", e)
print("Nilai gabungan, berserta konversinya a =", f)
print("Nilai gabungan, berserta konversinya b =", g)
print("Nilai gabungan, berserta konversinya a =", h)
print("Nilai gabungan, berserta konversinya b =", j)

"""
Dalam pengunaan sintax long dan menggabungkan, yang dimana untuk codenya itu sendiri harus menggunakan 2 variable utama
dan untuk penulisan output dari code itu sendiri ialah harus di tulis berulang", akan tetapi untuk melakukan konversi 
nilainya maka wajib di taruh, nama variable (utama) + variable yang ingin di tambah + operator arikmatika. Dan bisa 
berlaku pada semua operator (Arikmatika, Logika, Bitwise, decimal, biner, dan exadesimal)
"""
