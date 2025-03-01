# Pembuatan dasar - dasar operator (+, -, *, /, %, **, //)

"""
Ini adalah pembuatan operator yang menggunakan +
"""
print("\n")

a = 20
b = 13
c = a + b
print( a, "+", b, "HASILNYA", "=", c  )

print("\n")

"""
Ini adalah pembuatan operator yang menggunakan -
"""
a = 20
b = 13
c = a - b
print( a, "-", b, "HASILNYA", "=", c  )

print("\n")

"""
Ini adalah pembuatan operator yang menggunakan *
"""

a = 20
b = 13
c = a * b
print( a, "*", b, "HASILNYA", "=", c  )

print("\n")

"""
Ini adalah pembuatan operator yang menggunakan /
"""

a = 20
b = 13
c = a / b
print( a, "/", b, "HASILNYA", "=", c  )

print("\n")

a = 20
b = 13
c = a % b
print(a, "%", b, "HASILNYA", "=", c)

print("\n")

a = 20
b = 13
c = a ** b
print(a, "**", b, "HASILNYA", "=", c)

print("\n")

a = 20
b = 13
c = a // b
print(a, "//", b, "HASILNYA", "=", c)

print("\n")
"""
Yang di atas adalah salah satu contoh pengguanaan oprator mendasar dari 
arkmatika
"""

print("=============Batasan Dari Penggunaan Operator Arikmarika=============")
print("\n")

"""
Ini adalah pembuatan operator Pembandingan (>, <, >=, <=, ==, ===, !=, !==)
"""

# Ini adalah pembuatan operator pembanding < (Kurang dari)

d = 40
e = 30
f = d < e
print(d, "<", e, "HASILNYA", "=", f)

print("\n")
# Output dari pengeluarannya ialah False


# Ini adalah pembuatan operator pembanding > (Lebih dari)

d = 40 
e = 30
f = d > e
print(d, ">", e, "HASILNYA", "=", f)

print("\n")


# Ini adalah pembuatan operator pembanding <= (Kurang dari sama dengan)

d = 40
e = 30
f = d <= e
print(d, "<=", e, "HASILNYA", "=", f)

print("\n")


# Ini adalah pembuatan operator pembanding >= (Lebih dari sama dengan)

d = 40
e = 30
f = d >= e
print(d, ">=", e, "HASILNYA", "=", f)

print("\n")


# Ini adalah pembuatan operator pembanding == (sama dengan)

d = 40
e = 30
f = d == e
print(d, "==", e, "HASILNYA", "=", f)

print("\n")


# Ini adalah pembuatan operator pembanding === (Sama dengan Sama Tipe)

d = 30
e = 30
f = d, "===", e
print (d, "===", e, "HASILNYA", "=", f)

print("\n")

"""
Operator pembanding "sama dengan" (===) pada Python dapat digunakan untuk 
membandingkan apakah dua nilai sama atau tidak, sedangkan operator "sama tipe"
(is)digunakan untuk memeriksa apakah dua nilai memiliki tipe data yang sama.
Namun, terdapat beberapa kasus di mana operator pembanding ini tidak dapat 
digunakan dengan benar. Misalnya, jika kita membandingkan dua objek dengan 
tipe data yang berbeda, seperti string dan integer, maka operator "sama dengan" 
akan mengembalikan False karena nilai dan tipe data dari kedua objek berbeda.
"""


# Ini adalah pembuatan operator pembanding != (Tidak Sama Dengan)

d = 40
e = 30 
f = d != e
print(d, "!=", e, "HASILNYA", "=", f)

print("\n")


# Ini adalah pembuatan operator pembanding !== (Tidak Sama Tipe)

d = 30
e = 30
f = d, "!==", e
print(d, "!==", e, "HASILNYA", "=", f)

print("\n")


"""
Operator "Tidak Sama Tipe" (is not) pada Python digunakan untuk memeriksa 
apakah dua nilai memiliki tipe data yang berbeda. Operator ini akan mengembalikan 
nilai True jika kedua nilai memiliki tipe data yang berbeda, dan False jika kedua
nilai memiliki tipe data yang sama.Selain itu, operator "Tidak Sama Tipe" juga tidak
akan berfungsi dengan benar jika kedua objek yang dibandingkan memiliki nilai
yang sama, tetapi tipe data yang berbeda. Dalam kasus seperti itu, sebaiknya 
menggunakan operator pembanding "sama tipe" (is) atau "sama dengan" (==) untuk 
memeriksa apakah kedua objek sama atau tidak, tergantung pada kebutuhan 
pemrograman.
"""