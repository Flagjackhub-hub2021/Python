
# Ini Adalah Short Hand Dari Penggunaan (int,str, bool, float) Dan Pengambungannya

print("==========Ini Adalah Contoh Casting Yang Menggunakan Operator + ==========")
print("\n")

a = 6
b = 6.2
c = a + b
print (c)


print("\n")
print("==========Ini Adalah Contoh Casting Yang Menggunakan Operator - ==========")
print("\n")

d = 6
e = 6.2
f = d - e
print("\n")

print(f)


print("\n")
print("==========Ini Adalah Contoh Casting Yang Menggunakan Operator * ==========")
print("\n")

g = 6
h = 6.2
i = g * h
print(i)


print("\n")
print("==========Ini Adalah Contoh Casting Yang Menggunakan Operator / ==========")
print("\n")


j = 6
k = 6.2
l = j / k

print (l)


print("\n")
print("==========Ini Adalah Contoh Casting Yang Menggunakan Operator % ==========")
print("\n")

p = 6
q = 6.2
r = p % q

print (r)


print("\n")
print("==========Ini Adalah Contoh Casting Yang Menggunakan Operator ** ==========")
print("\n")

s = 6
t = 6.2
u = s ** t

print (u)



"""
Ini adalah contoh casting pada implict yang menggabungkan 2 sampai 1 
Tipe Data pada Implict Casting
"""

# LONG HAND Penggunaan Tipe Data Casting + Pengambungan (int,str, bool, float)

# Pengambungan Str + int
print("=========Ini adalah Contoh Implict Casting pada str + int ==========")
print("\n")
nama = "Muhammad Fadel"
umur = 20
kalimat = "Nama saya " + nama + " dan umur saya " + str(umur) + " tahun."

print(kalimat)


# Pengambungan bool (True) dan  bool (False)
print("\n")
print("=========Ini adalah Contoh Implict Casting pada bool==========")
a = 10
b = 0

print(bool(a))  
print(bool(b)) 


# Pengambungan 2 File Float Dalam 1 Tipe Data Float
print("\n")
print("=========Ini adalah Contoh Implict Casting pada float 1 dan float 2==========")
print("\n")
c = 1.1
d = 2.2
e = c + d

print(e)

"""
Contohnya yang di atas , jika kita menambahkan sebuah angka bulat dengan
sebuah bilangan pecahan, Python akan mengkonversi nilai bulat ke
bilangan pecahan sebelum menjalankan operasi penjumlahan.
"""