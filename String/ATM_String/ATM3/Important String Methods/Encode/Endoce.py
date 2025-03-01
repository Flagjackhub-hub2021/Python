# Contoh penggunaan encode pada string dalam importan string
Data = "Múhàmmăđ FÆđęł" 
print(Data)
print(Data.encode())

Data = "Muhammad Fadel" #Contoh yang salah pada inputan value dalam encode  
print(Data.encode())

# Contoh penggunaan encode pada simbol tertentu dalam importan string
Data = "🤣"
print(Data)
print(Data.encode())

"""
Pada 2 code di atas yang dimana salah satu contoh penggunaan dari method encode itu sendiri, untuk contoh penggunaan encode pada string dalam importan string yang dimana code ini adalah bentuk dasar dari penggunaan encode pada string 
yang harus anda ketahui ialah menggunakan encode pada string itu tidak bisa menginputkan string biasa "M, h, mm, F" mesikupun anda menggunakan method encode pada string biasa, inputannya akan menginputkan sesuai dari isian string yang dimasukan 
liat contoh pada variable 2. Untuk penggunaan method encode huruf, tanda baca, simbol, spasi putih, dan karakter kontrol akan menjadi angka dan, akhirnya, bit. Setiap karakter dapat dikodekan ke urutan bit yang berbeda. Untuk mencapai proses pengkodean ini, fungsi Python encode() 
""" 

# Contoh pengkodean dengan parameter error dalam importan string
Data = "Múhàmmăđ FÆđęł"
print(Data.encode())
print("\t")
print(Data.encode("ascii", "ignore"))
print("\t")
print(Data.encode("ascii", "replace"))
print("\t")
print(Data.encode("ascii", "xmlcharrefreplace"))
print("\t")
print(Data.encode("ascii", "backslashreplace"))
print("\t")
print(Data.encode("ascii", "namereplace"))

print("\t")

c = '\u0061'
print(c.encode())
c = '\u0041'
print(c.encode())
c = '\u004D''\u0055''\u0048''\u0041''\u004D''\u004D''\u0041''\u0044''\u0046''\u0041''\u0044''\u0045''\u004C'
print(c.encode())

"""
Pada code diatas yang dimana kita melakukan penulisan syintax serta memasukan isian parameter Unicode Symbols Number.
Yang dimana hasil dari inputan tersebut akan menghasilkan ouputan alfabet capslock dari Unicode Symbols Number.
"""

"""
kamus Python () mengikuti sintaks yang disebutkan : string.encode(encoding, errors)

1. encoding (Optional): menentukan standar encoding yang akan digunakan. Jika tidak ada penyandian yang ditentukan, Python menganggap UTF-8 sebagai standar penyandian default.
2. errors (Optional)  : a. respons default, yang melontarkan pengecualian UnicodeDecodeError jika gagal
                        b. (ingnore) mengabaikan semua karakter yang tidak dapat dikodekan dari hasil
                        c. (replace) itu mengabaikan semua karakter yang tidak dapat dikodekan dari hasil
                        d. (xmlacharrefreplace) mengganti referensi karakter XML untuk Unicode yang tidak dapat dikodekan
                        e. (namereplace) alih-alih Unicode yang tidak dapat dikodekan, ia menyisipkan urutan escape{…}
                        f. (backlashreplace) Unicode yang tidak dapat dikodekan, masukkan urutan escape uNNNN
3. ASCII(Optional)    : Encoding yang hanya mendukung karakter ASCII (7-bit) tanpa karakter khusus atau internasional.


Metode “string.encode()” digunakan untuk menyandikan string tertentu ke dalam urutan byte tergantung pada pengkodean tertentu. Parameter 'encoding' dan 'errors' digunakan untuk menentukan pengkodean yang akan digunakan 
dan metode error yang akan digunakan untuk menangani error. Penulisan Python ini memberikan panduan komprehensif tentang metode “string.encode()”
"""

print("\t")

# penggunaan UTF pada pengkodean 
print(Data.encode("UTF-8"))
print(Data.encode("UTF-16"))
print(Data.encode("UTF-32"))

"""
1. UTF-8 (default): Encoding yang paling umum digunakan untuk merepresentasikan karakter Unicode dalam bentuk byte.
2. UTF-16: Encoding yang merepresentasikan karakter Unicode menggunakan 16-bit atau 2 byte per karakter.
"""

print("\t")

# Contoh penggunaan kode default python menggunakan UTF-8
Data = "Bèľájãř"
print(Data.encode())
print(Data.encode("UTF-8"))

"""
Jika tidak ada parameter yang ditentukan, maka fungsi string encode() Python akan menggunakan nilai defaultnya. Untuk 
parameter encoding, nilai defaultnya adalah UTF-8, dan untuk parameter error, nilai defaultnya adalah strict
"""

print("\t")

# Contoh program untuk memeriksa semua Standar Pengkodean dengan Python dalam encode
# from encodings.aliases import aliases

# print("Pengkodean yang tersedia adalah : ")
# print(aliases.keys())

"""
Ada skema pengkodean tertentu yang didukung oleh metode Python String encode() . Kami bisa mendapatkan pengkodean yang didukung menggunakan kode Python di atas ini.
"""

print("\t")

# Contoh penggunaan bagaimana encode URL di dalam python 
import urllib

Data = "ÝÈŚ WÈ HÀĆĶ"
print(urllib.parse.quote(Data)) # parse.quote() adalah sandi untu menggunakan encode pada URL


# Contoh penggunaan bagaimana berubah space menjadi +
print(urllib.parse.quote_plus(Data)) # urllib.parse.quote_plus() adalah sandi untuk mengubah space menjadi + sehingga tidak ada lagi space dalam sebuah URL

# Contoh penggunaan bagaimana encode pada beberapa parameter dalam URL
Data = {"Hi" : "Please come", "website" : "WWW.Hack.The.Box.Indonesia"}
print(urllib.parse.urlencode(Data))

"""
Pada penggunaan import urllib yang dimana ini berguna untuk melakukan encode pada sebuah sub domain dalam url pada pengggunaan "urlib.parse.qoute" yang dimana akan menghinputkan simbol (%) 
pada setiap kata yang telah di encode. Untuk penggunaan "urlib.parse.quote_plus" yang dimana pada setiap abjad yang tidak normal (Seperti yang layaknya digunakan) akan di encode + pada setiap
abjad yang normal akan di taruh tanda "+" yang dimana berguna untuk melakukan space pada inputan abjad normalnya. Pada penggunaan "urllib.parse.urlendcode" sama seperti layaknya url yang sering kita
temukan dalam intener dan pada setiap simbol ":" akan di ganti menjadi simbol =
"""

