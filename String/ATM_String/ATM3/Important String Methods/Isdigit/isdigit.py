"""
Metode Python String isdigit() mengembalikan " Benar " jika semua karakter dalam string adalah angka, 
Jika tidak, ia mengembalikan " Salah ".

Syntax of String isdigit() : 
                            string.isdigit()

isdigit() Parameters : 
                        isdigit() tidak mengambil parameter apa pun.

Return Value from isdigit() :
                                1. True  : jika semua karakter dalam string adalah angka.
                                2. False : jika setidaknya satu karakter bukan angka.
"""
a = "13MuhammadFadel" # Penulisan syintax yang salah
print(a.isdigit())

a = "Muhammad Fadel 13" # Penulisan syintax yang salah
print(a.isdigit())

a = "14322455"
print(a.isdigit()) # Penulisan syintax yang benar

"""
Pada penggunaan method string menggunaakan 'isdigit', yang dimana kita hanya berfokus pada inputan string 
yang bersifat numerik saja dan jangan ada tanda ',' '.' '+' '-' dan melakukan space meskipun itu 
memperbagus syintax (Clean Code)
"""

print ("\t")

"""
Dalam Python, superskrip dan subskrip (biasanya ditulis menggunakan Unicode) juga dianggap sebagai karakter 
digit. Oleh karena itu, jika string berisi karakter ini bersama dengan karakter desimal, isdigit() mengembalikan True. 
Angka Romawi, pembilang mata uang, dan pecahan (biasanya ditulis menggunakan Unicode) dianggap sebagai karakter numerik tetapi bukan angka.
isdigit() mengembalikan False jika string berisi karakter-karakter ini. Untuk memeriksa apakah suatu karakter merupakan karakter numerik atau bukan, 
kita dapat menggunakan metode isnumeric().
"""

# String Berisi angka dan Karakter Numerik
b = '¾' # Penulisan isian syintax yang salah
print(b.isdigit())
b = '123' # Penulisian isian syintax yang benar
print(b.isdigit())

print("\t")

b = '\u0034'
print(b.isdigit()) # Penulisian isian syintax yang benar
c = '\u0039'
print(c.isdigit())
c = '\u0061'
print(c.encode())


"""
Pada penulisan syintax code diatas yang dimana kita melakukan mencantumkan perbedaan 
antara metode isdecimal(), isdigit(), dan isnumeric() berdasarkan input yang diberikan. 
Dan dari ketiga metode tersebut harus inputannya sama (pada isdecimal 'True', isnumeric 'True', isnumeric 'True').
Dan pada isian parameter yang dimana saya memasukan code Ascii digit, pada kedua kode di atas, dan untuk code ketiga
yang dimana saya memasukan code Unicode syimbol Number yang dimana berguna untuk menghasilakn outputan alfabet.
"""

# https://www.tutorialsteacher.com/python/string-isdigit = Hasil True pada 3 metode (isdecimal, isdigit, isnumeric)
# https://symbl.cc/en/unicode/table/ = Hasil semua code unicode yang bisa di konversi di Python, HTML, dan CSS.
# https://symbl.cc/en/unicode/blocks/basic-latin/#subblock-0030 = Hasil code Ascii code yang bisa di konversi ke unicode.