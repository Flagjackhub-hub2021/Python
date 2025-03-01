a = 40
b = 50 
c = a + b
jumlah = (input("silahkan jumlah angka tersebut : "))

if jumlah < "80":
    print("Maka benar")
elif jumlah > "80" :
    print("Maka salah")
else:
    print("Bye")

# Penggunaan Elife_Statment yang standar. Yang mana penulis mengdeklarasikan 3 variabel, 2 variabelnya
# memiliki parmeter angkata arikmatika, sedangkan parameter yang terakhir berguna untuk menjumblahkan 2 variabel
# berserta parameter (angka arikmatikanya). Dan penulis membuat elife statmen, yang mana statment tersebut memiliki parameter arikmatika dalam bentuk string
# berguna untuk membandingkan simbol pembanding agar terbaca sebagai string bukan int. Dan itu merupakan bentuk dari penulisan code yang diterapkan oleh python itu sendiri#

print("\b")

Harga = 30000
print("total", Harga)

if Harga >  400:
    pajak = Harga / 10/1
elif Harga > 200 :
    pajak = Harga /  10/10
elif Harga > 150  :
    pajak = Harga / 10 /9
else :
    pajak= 0
print("Harga yang harus dibaya", Harga - pajak)

print ("\b")

a = 2
b = 330
print("A") if a > b else print("B")

# Short Hand If ... Else with  2 statment

a = 150
b = 330
c = 350
print("A") if a > b > c else print("B") if a > b > c else print("C")

# Short Hand If ... Else with  3 statment