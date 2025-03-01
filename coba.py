a = ["Hello" + " " "World"]
b = "". join(a)
print(b)

Nama = "Muhammad Fadel"
print(Nama [7])
print(Nama [5])

Nama   = ["Muhammad" " " "Fadel"]
result = "Penggabungan = " " " + "".join(Nama)
print(result)

# Penggunaan fitur .split dalam string
Nama   = ("Muhammad" "Fadel")
result = "Penghilangan =" " " + str(Nama.split("Fadel"))
print(result)


teks = "Halo dunia! Selamat datang di OpenAI!"

bagian = teks.rsplit(" ", 5)
print(bagian)

a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = a is a
print(c)

a = [1,2,3,4,5]
b = [1,2,3,4,5]

if a is b :
    print("jika a adalah a maka benar")
else:
    print("jika b adalah a maka salah")

b = a

if a is b :
    print("jika a dan b merujuk ke objek yang sama")
else:
    print("a dan b tidak merujuk ke objek yang sama")


teks = "   ini adalah contoh penggunaan syntax strip pada Python   "
hasil = teks.strip()
print(hasil)

teks = "\ini adalah contoh penggunaan syntax strip pada Python"
result = teks.strip()
print(result)

Data = [1,2,3,4,5]
Result = Data [1]
print(Result)

# Penulisan utama method string menggunakan find
string_utama = "Ini Adalah Contoh Penggunaan Method find Pada string"
substring = "Contoh"
hasil_find = string_utama.find(substring)
print(hasil_find) 

# Bisa menggunakan int, float, dan binary pada method find 
def Hasil_Data(daftar, nilai) :
    find = []
    for a in range(len(daftar)):
        if daftar[a] == nilai:
            find.append(a)
            return find

Number        = [1, 10, 11, 110, 111]
Cari_Number   = 110
result        = Hasil_Data(Number, Cari_Number)
print("find result", Cari_Number, "=", result)

# Hanya bisa menggunakan str pada method fid
main_string = "Hello, hello, Hello, HELLO! , hello"
sub_string = "hello"
count_er=0
start_index=0
for i in range(len(main_string)):
  j = main_string.find(sub_string,start_index)
  if(j!=-1):
    start_index = j+1
    count_er+=1
print("Total occurrences are: ", count_er)

Data = "Hello World"

print("Index dari H", Data.rfind("H" " " "="))


# Finding the last position of sub_str in my_str using rfind()

my_str = "I scream you scream, we all scream ice-cream"
sub_str = "cream"

x = my_str.rfind(sub_str)

print("Posisi dari kata cream of '{}', is '{}', '{}'".format(my_str,sub_str,x))


# nilai = int(input("Masukkan nilai Anda: "))

# # Memeriksa apakah nilai lebih besar dari atau sama dengan 60
# if nilai >= 60:
#     status = "Lulus"
# else:
#     status = "Tidak Lulus"

# # Mencetak hasil dengan menggunakan method format
# print("Nilai Anda: {}. Anda {}".format(nilai, status))

print ("\t")

# Penggunaan method replace dengan str (substring) pada importan stirng 
Word = ("Saya suka makan ayam")
print (Word.replace("makan", "tidak"))

"""
Catatan penting pada penggunaan syintax diatas yang dimana pada hasil output pada method replace pada double quote pertama kita menuliskan 
kembali string yang akan kita ubah pada data utama, dan pada double quote yang kedua yang dimana berfung sebagai penganti data (string) pada 
data utama yang bertuliskan makanan.
"""

original_list = ["apple", "banana", "cherry"]
replaced_list = [item.replace("a", "e") for item in original_list]
print(replaced_list)

# Given string
string='Ayush Saxena'
count=0

# Initialising new strings
newstring1 =""
newstring2 =""

# Iterating the string and checking for alphabets
# Incrementing the counter if an alphabet is found
# Finally printing the count
for a in string:
	if (a.isalpha()) == True:
		count+=1
		newstring1+=a
print(count)
print(newstring1)

# Given string
string='Ayush0212'
count=0
for a in string:
	if (a.isalpha()) == True:
		count+=1
		newstring2+=a
print(count)
print(newstring2)

print("¶".encode('utf-8'))


def greeting(name):
    print("Halo, " + name + "! Selamat datang.")

greeting("Ahmad")

nama_file = "contoh.txt"
if nama_file.endswith((".txt", ".pdf", ".docx")):
    print("File tersebut adalah sebuah dokumen.")
else:
    print("File tersebut bukan sebuah dokumen.")

    
text = "geeks for geeks."

# start parameter: 10
result = text.endswith('geeks.', 12)
print(result)



Data = 2 ^ 2
print(Data)