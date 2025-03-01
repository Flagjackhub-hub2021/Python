# """
# Penggunaan Tipe Data Boolean pada python terkhusnya ialah :
# pengguan true, false pada Operetor Perbandingan 
# berserta Operator Logika 
# """



# Penggunaan nilai dari Operator Logika
# AND (Konjungsi) ^

a = True and True
print (a)

b = True and False
print (b)

c = False and True
print (c)

d = False and False
print (d)


# Penggunaan nilai dari Operator Logika
# Dijungsi (OR) V

a = True or True
print (a)

b = False | True
print (b)

c =  True | False
print (c)

d = False | False
print (d)



# Penggunaan nilai dari Operator Logika
# Negasi (Not) ~

a = not True and False
print (a)

b = not False and True
print (b)

c = not True and True
print (c)

d = not False and False
print (d)



# Penggunaan nilai dari Operator Logika
# Ekseklusif (- or x-OR) 

a = True ^ True
print (a)

b = True ^ False
print (b)

c = False ^ True
print (c)

d = False ^ False
print (d)


# Penggunaan nilai dari Operator Logika
# Implikasi (IF...THEN) (-->) 

a = True and True
print (a)

b = not True and False
print (b)

c = not False and True
print (c)

d = not False ^ False
print (d)


# Penggunaan nilai dari Operator Logika
# Biimplikasi (IF...and only IF) (<-->)

a = True and True
print (a)

b = not True and False
print (b)

c =  not False ^ True
print (c)

d = not False ^ False
print (d)




# """
# Ini adalah contoh penguanan operator perbandingan yang menggunakan
# true or false di dalam operator logika.
# """
# Operator Perbandingan (Lebih Dari)

Nilai = (5 > 10)
print(Nilai)

# Operator Perbandingan (Kurang Dari)

Nilai = (10 < 20 )
print(Nilai)

# Operator Perbandingan (Lebih Dari sama dengan)

Nilai = (20 >= 30)
print(Nilai)

# Operator Perbandingan (Kurang Dari sama dengan)

Nilai = (30 <= 40)
print(Nilai)

# Operator Perbandingan (Sama Dengan)

Nilai = (50 == 50)
print(Nilai)

# Operator Perbandingan (Sama Dengan Sama Tipe)

Nilai = (40 != 40)
print(Nilai)


# """
# Pembuatan Tipe Data Boolean + Menggunakan IF and Else
# berserta Operator Pembanding.
# """

# Code 

a = 60
b = 40

if a < b :
    print ("Apakah a lebih besar dari b")
    print (True)
else:
    print ("Apakah b lebih besar dari a")
    print (False)

if a > b :
    print ("Apakah a lebih besar dari b")
    print (True)
else :
    print ("Apakah b lebih besar dari a")
    print (False)
