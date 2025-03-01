"""
Metode Python String isalnum() memeriksa apakah semua karakter dalam string tertentu adalah karakter
alfabet atau numerik (alfanumerik).

isalnum() Syntax :
                    string.isalnum()

isalnum() Parameters :
                        Metode isalnum() tidak mengambil parameter apa pun

isalnum() Return Value :
                            1. True  : jika semua karakter dalam string adalah alfanumerik
                            2. False : jika setidaknya satu karakter bukan alfanumerik
"""

print("\t")

# Contoh penggunaan metode isalnum() dengan string dengan huruf saja
a = "Muhammad Fadel" # Penulisan alfabet yang salah 
print(a.isalnum()) 

a = "Muhammad_Fadel" # Penulisan alfabet yang salah 
print(a.isalnum())

a = "MuhammadFadel" # Penulisan alfabet yang benar
print(a.isalnum())

# Pada penulisan ketiga syintax diatas yang dimana kita hanya mencari hasil penulisan yang benar (True) dari outputnya saja

print("\t")
# Contoh penggunaan metode isalnum() dengan string dengan angka saja
b = "1 2 3 4 5 6 7" # Penulisan angka yang salah 
print(b.isalnum())

b = "1,2,3,4,5,6,7" # Penulisan angka yang salah 
print(b.isalnum())

b = "1234567"
print(b.isalnum()) # Penulisan angka yang benar

# Pada penulisan ketiga syintax diatas yang dimana kita hanya mencari hasil penulisan yang benar (True) dari outputnya saja

print("\t")

# Contoh penggunaan metode isalnum() penggabungan string alfabet dan angka
c = "12343_afsel"
print(c.isalnum()) # Penulisan penggabungan string alfabet dan angka yang salah

c = "fdel 12434"
print(c.isalnum()) # Penulisan penggabungan string alfabet dan angka yang salah

c = "fadel13"
print(c.isalnum()) # Penulisan penggabungan string alfabet dan angka yang benar