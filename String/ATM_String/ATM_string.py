# Memodifikasi string 
print("Ini adalah string yang sering saya gunakan")

print('\t')

print("~ Bagian satu")

# String menggunakan singgle quote
print("'Ini adalah penggunaan single quote' ")
# String menggunakan double quote
print('"Ini adalah penggunaan doubke quote"')
# Menggubah single qoute menggunakan backslash
print('Besok hari jum\'at')

"""
Untuk melakukan memodifikasi sebuah string menggunakan (single quote, double quote, dan single quote ke backlash)
yang dimana harus wajib dipahami cara penggunaan string, supaya tidak bigung untuk melakukan ATM
"""

print("\t")

print('~ Bagian dua')

# Membuat kerakter spacial dalam string (Khusus)

# Menggunakan tanda backlash (\)
print("C:\\Windos\\Flag_Jack")
print('C:\\Linux\\Flag_Jack')

"""
Untuk pengunaan kerakter spacial dalam string khususnya menggunakan backlash, dari penulisan di atas
ketika kita memakia simbol backlash // 2x makah yang akan dioutput hanya satu simbol saja dari depan
(Belakng saja)
"""

# Menggunakan tab
print("Muhammad \t\t\tFadel")

# Menggunakan new line 
print('saya senang pergi ke\ntempat yang nyaman dan tenang') #Diguanakan pada linux, dan macOS
print("Saya suka makan\res crime")
print("Saya akan pergi\r\nke mana saja") #Digunakan pada windows

"""
Pada penggunaan pada line 44 dan 46, dalam menggunakan krakter spacial yang dimana pada windows bisa menggunakan 
simbol \n untuk melakukan baris baru (Yang pada umumnya digunakan), dan bisa juga menggunakan \r jika sudah memahami 
simbol \n
"""

print("\t")

print("~ Bagian 3")

# Membuat raw string, multiline literal string, multiline literal string row, 

# Menggunakan raw stirng 
print(r'C:\windows\Flag_jack')
print(r"C:\windows\Flag_jack")

print('\t')

# Menggunakan multiline literal string
print("""
User1 : Hai salam kenal
User2 : Hai salam kenal kembali
User1 : Apakah kau senang menjadi enginer ?
User2 : Yaaa, tentu saja Kamu ?
User1 : Iya sama, itu menjadi salah satu impian saya
""")

"""
Pada penggunaan multiline literal string, biasa di gunakan untuk melakukan chatbot dan untuk penulisan 
tidak terlalu sempurna contoh jika kita menaruh sebuah simbol seperti (\\) sebanyak 2X maka akan terbaca 
1 kali saja dalam penulisannya (output)
"""

print("\t")

# Menggunakan mutline literal string row
print(r"""
Fadel : Saya akan menjadi hukum clude di angaktan saya
Fadel : Itu wajib dan harus\\supaya saya bisa tunjukan bahwa bisa bersaing di kampus
""")

"""
Dalam penggunaan mutline literal string row. Yang dimana semua dari penulisannya akan di anggap sebuah string
termasuk itu sebuah simbol, angka dan hal yang bawahan dari sintax python itu sendiri
"""

word   = ("\tMuhammad Fadel")
result = word.strip()
print(result)

"""
Penggunaan dari fitur .strip(), yang dimana berguna untuk melakukan pengapusan sebuah karakter khusu maupun sebuah space yang di sengaja maupun tidak disengaja
dan karakter khusus yang dapat di hapus (di nonaktifkan) ialah (\t, \n, \r,) dan untuk space yaitu (" ") dan space bisa di dalam sebuah array, list, maupun tuple
"""