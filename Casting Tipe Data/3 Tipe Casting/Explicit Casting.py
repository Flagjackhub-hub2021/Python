# Pembuatan Explicit Casiting pada integer

"""
Ini adalah Long hand dari perpindahan Tipe Data Integer
ke Tipe Data Float yang Menggunakan Variable_Integer dan Variable_float
"""

Variable_Integer = 10
Variable_float   = float(Variable_Integer)

print (Variable_float)
print("================================================") 
print("\n")



"""
Ini adalah Long hand dari perpindahan Tipe Data Float
ke Tipe Data Integer yang Menggunakan Variable_Float dan Variable_Integer
"""

Variable_float   = 10.1
Variable_Integer = int(Variable_Integer)

print (Variable_Integer)
print("================================================")
print("\n")



"""
Ini adalah Long hand dari perpindahan Tipe Data Float
ke Tipe Data String yang Menggunakan Variable_Float dan Variable_String
"""

Variable_float  = "10.1"
Varibale_string = str(Variable_float)

print (Varibale_string)
print("================================================")
print("\n")



"""
Ini adalah Long hand dari perpindahan Tipe Data String
ke Tipe Data Integer yang Menggunakan Variable_String dan Variable_Integer
"""

Varibale_string = "5"
Variable_Integer = int(Varibale_string)

print (Variable_Integer)
print("================================================")
print("\n")



"""
Ini adalah Long hand dari perpindahan Tipe Data String
ke Tipe Data Float yang Menggunakan Variable_String dan Variable_Float
"""

Variable_string = "5.5"
Variable_float  = float(Varibale_string)

print (Variable_float)
print("================================================")
print("\n")



"""
Ini adalah Long hand dari perpindahan Tipe Booloean (True)
ke Tipe Booloean (False) yang Menggunakan Variable_Booloean (True) dan Booloean (False)
"""

Variable_True  = 1
Variable_False = bool(0)

print (Variable_False)
print("================================================")
print("\n")



"""
Ini adalah Long hand dari perpindahan Tipe Booloean (False)
ke Tipe Booloean (True) yang Menggunakan Variable_Booloean (False) dan Booloean (True)
"""

Variable_False = 0
Variable_True  = bool(1)

print(Variable_True)
print("================================================")
print("\n")




#Ini adalah short hand dari pembuatan Expilicit Casting 

"""
Ini adalah short hand dari perpindahan Tipe Data Integer
ke Tipe Data Float yang Menggunakan Variable a dan b
"""
a = 10
b = float (a)

print(b)
print("================================================")
print("\n")

"""
Ini adalah short hand dari perpindahan Tipe Data Float
ke Tipe Data Integer yang Menggunakan Variable c dan d
"""

c = 10.1
d = int (c)

print(d)
print("================================================")
print("\n")


"""
Ini adalah short hand dari perpindahan Tipe Data Float
ke Tipe Data String yang Menggunakan Variable e dan f
"""

e = 10.1
f = str (e)

print (f)
print("================================================")
print("\n")


"""
Ini adalah short hand dari perpindahan Tipe Data String
ke Tipe Data integer yang Menggunakan Variable g dan h
"""

g = "5"
h = int (g)

print (g)
print("================================================")
print("\n")


"""
Ini adalah short hand dari perpindahan Tipe Data String
ke Tipe Data Float yang Menggunakan Variable i dan j
"""

i = "5.5"
j = float(i)

print(j)
print("================================================")
print("\n")



"""
Ini adalah short hand dari perpindahan Tipe Data Boolean (True)
ke Tipe Data Boolean (False) yang Menggunakan Variable k dan l
"""

k = 1
l = bool (0)

print(l)
print("================================================")
print("\n")


"""
Ini adalah short hand dari perpindahan Tipe Data Boolean (False)
ke Tipe Data Boolean (True) yang Menggunakan Variable m dan n
"""

m = 0
n = bool(1)

print(n)
print("================================================")
print("\n")

"""
Catatan Penting !!!

juga dikenal sebagai konversi tipe data manual. Ini adalah 
ketika kita secara manual mengubah tipe data dari sebuah nilai ke tipe data 
yang lain. Contohnya, jika kita memiliki sebuah string yang berisi angka,
kita dapat mengubahnya menjadi integer dengan menggunakan fungsi int().
"""