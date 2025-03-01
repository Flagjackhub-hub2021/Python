
"""
Tipe data ada 4 ialah:

1. string
2. integer
3  float
4. boolean  
"""

# Penulisan + Penggunaan awal tipe int, float, boolean, dan string

# Penggunaan deklasrasi string 


print ("===========INTEGER===============")
# Ini adalah deklarinya untuk membuat 3 tipe data di bawahnya
data_integer = 9
print ("Data : ", data_integer, "type =", type(data_integer))
print("Ini adalah deklarisnya untuk membuat 3 tipe data di bawahnya")
print("\n")

data_float   = float(data_integer)
print ("Data : ", data_float, "type", type (data_float))

data_boolean = bool(data_integer)
print ("Data : ", data_boolean, "type", type(data_boolean))

data_string  = str(data_integer)
print ("Data : ", data_string, "type", type(data_string))
print("\n")


# Penggunaan deklasrasi float

print ("===========BOOLEAN===============")
# Ini adalah deklarinya untuk membuat 3 tipe data di bawahnya
data_boolean = 6.9
print ("Data : ", data_boolean, "type", type (data_boolean))
print("Ini adalah deklarisnya untuk membuat 3 tipe data di bawahnya")
print("\n")

data_integer = int(data_boolean,)
print ("Data : ", data_integer, "type", type(data_integer))

data_float = float(data_boolean)
print ("Data : ", data_float, "type", type(data_float))

data_string = str(data_boolean)
print ("Data : ", data_string, "type", type(data_string))
print("\n")


"""
Dalam penggunaan deklarasi penulisan nilai dari variable boolean 
(data_boolean = 7.9) itu harus menggunakan titik jangan titik koma
di karnakan akan menyebabkan terjadinya eror
pada saat pembacaan kode oleh komputer
"""

print ("============FLOAT===============")
# Ini adalah deklarinya untuk membuat 3 tipe data di bawahnya
data_float = 10
print ("Data : ", data_float, "type", type(data_float))
print("Ini adalah deklarisnya untuk membuat 3 tipe data di bawahnya")
print("\n")

data_integer = int(data_float)
print ("Data : ", data_integer, "type", type(data_integer))

data_boolean = bool(data_float)
print ("Data : ", data_boolean, "type", type(data_boolean))

data_string  = str(data_float)
print ("Data : ", data_string, "type", type(data_string))
print("\n")


"""
Pengguan Tipe data float yang dimana jika kita menaruhkan 
nilai dari variablenya (data_float = 0) maka hasil yang akan 
terbaca oleh komputer ialah False tetapi jika akun positif 
seperti : 1... sampai -1... itu akan terbaca oleh 
komputer menjadi True
"""

print ("===========STIRNG===============")
# Ini adalah deklarinya untuk membuat 3 tipe data di bawahnya
data_string = str("Muhammad Fadel")
print ("Data : ", data_string, "type", type(data_string))
print("Ini adalah deklarisnya untuk membuat 3 tipe data di bawahnya")
print("\n")

data_integer = int(data_string)
print ("Data : ", data_integer, "type", type(data_integer))

data_boolean = bool(data_string)
print ("Data : ", data_boolean, "type", type(data_boolean))

data_float   =  float(data_string)
print ("Data : ", data_float, "type", type(data_float))

"""
Pengguan Tipe data string yang dimana jika kita menaruhkan 
("Muhammad Fadel") pada deklasrasi penggunaan tipe data int dan float
(data_integer = int(data_string)) + (data_float = float (data_string))
makah yang akan terbaca oleh komputer ialah eror, yang mana hal ini
di sebabkan karena integer, dan float hanya bisa membaca tulisan angka
dan harus menggunakan titik bukan koma. Dalam penggunan casting di py
"""