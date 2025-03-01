# Menggunakan upper ke string
Nama    = "Muhammad Fadel"
panjang = Nama.upper()
print("Hasil dari upper" + " " + panjang)

# Menggunakan lower ke string
Nama    = "MUHAMMAD FADEL"
panjang = Nama.lower()
print("Hasil dari lower" + " " + panjang)

"""
Pada penggunaan fitur .upper dan .lower yang dimana hal ini digunakan hanya untuk sebuah char di dalam sebuah string. Dan kegunaan dari
fitur .upper yang dimana akan mengubah tulisan di dalam string menjadi BOLD, meskipun kita tidak melakukan bold pada tulisan kita.
Sedangkan pada fitur .lower yang dimana akan melakukan perbuahan tulisan dari dalam string menjadi normal, meskipun kita menulisan tulisan
menjadi bold, maupun huruf awalan bold.
"""

print("\t")

"""
Pada penggunaan fitur .upper dan .lower yang dimana hal ini digunakan hanya untuk sebuah char di dalam sebuah string. Dan kegunaan dari
fitur .upper yang dimana akan mengubah tulisan di dalam string menjadi BOLD, meskipun kita tidak melakukan bold pada tulisan kita.
Sedangkan pada fitur .lower yang dimana akan melakukan perbuahan tulisan dari dalam string menjadi normal, meskipun kita menulisan tulisan
menjadi bold, maupun huruf awalan bold.
"""


# Melakukan pengecekan menggunkan method is di dalam sebuah fitur .upper
testing = "muhammad fadel"
result  = testing.isupper()
print("Hasil dari : " + "is upper" + " " + "=" + " " +str(result))

# Melakukan pengecekan menggunakan method is di dalam sebuah fitur .lower
testing = "MUHAMMAD FADEL"
result  = testing.islower()
print("Hasil dari : " + "is lower" + " " + "=" + " " +str(result))

"""
Cara kerja dari sebuah method is menggunakan is upper dan is lower yang dimana akan melakukan penggujian terhadap sebuah string, menggunakan class stryang akan menggeluarkan hasil berupa
false maupun true. Yang dimana cara untuk menggetahui hasil yang akan keluar True atau False maka anda harus paham bagaimana cara kerja dari fitur .upper dan .lower
"""

print("\t")

# Alokasi krakter rjust(), ljust(), dan center()

rigth  = "rigth".rjust(10)
print("'" + rigth + "'")

left   = "left".ljust(10)
print("'" + left + "'")

center = "center".center(10)
print("'" + center + "'")

center = "center".center(10)
print("'" + center + "'")

print("\t")

"""
Penggunaan dan keggunaan dari alokasi krakter pada python, yang dimana bisa digunakan untuk melakukan penggisian sebuah variable dan penggunaannya bisa untuk melakukan pengisian data
pada sebuah data yang berupa string  saja dan dapat di gunakan dalam pembuatan website, pengisian sebuah data dan lain" sama halnya seperti PHP yang dimana befokus di web(dinamis)
"""

# Penggunaan fitur .join dalam string
Nama   = ["Muhammad" " " "Fadel"]
result = "Penggabungan = " " " + "".join(Nama)
print(result)

print("\t")

"""
Pada fitur join yang dimana anda bisa menggunkan list ataupun sebuah array di dalam sebuah variable atau string, yang dimana kegunaan dari fitur ini
ialah untuk melakukan penggabungan antar sebuah variable 
"""

# Penggunaan fitur .split dalam pengapusan string
Nama   = ("Muhamad" " " "Fadel")
result = "Pengapusan   = " " " + str(Nama.split("Fadel")) 
print(result)

# Pemisahan antar variable
Nama   = ("Muhammad Fadel 4 5")
result = "Pemisahan dimulai dari sebelah kiri  =" " " + str(Nama.split(" ",2))
print(result)

print("\t")

"""
Pada fitur split yang dimana untuk split pada case ini bisa digunakan untuk melakukan pengapusan serta melakukan pemisahan sebuah variable yang 
dimulai dari sebelah kiri ke kanan. Dan untuk pemisahannya sendiri itu bisa di isi sebuah krakter (variable), maupun sebuah angka yang di dalamnya dilapisi 
oleh string untuk hasil ouputnya akan sama seperti inputannya.

"""

# Penggunaan fitur .split dalam string
Sampel = ("1 2 3 4 5 6 7 8")
result = "Pemisahan dimulai dari sebelah kanan =" " " + str(Sampel.rsplit(" ",2))
print(result)

"""
Sedangkan untuk fitur rsplit yang dimana kegunaannya ialah untuk melakukan pemisahan sebuah variable yang dimulai dari sebelah kanan ke kiri. 
dan untuk pemisahannya sendiri itu bisa di isi sebuah krakter (variable), maupun sebuah angka yang di dalamnya dilapisi oleh string untuk hasil 
ouputnya akan sama seperti inputannya
"""

print("\t")

# Cara kerja dari fitur starswitch serta melakukan pengecekan
Data_testing  = "Muhammad Fadel".startswith("Muhammad")
print("Result : " +str(Data_testing))

# Cara kerja dari fitur endswitch serta melakukan penggecekan
Data_testing  = "Muhammd Fadel".endswith("Fadel")
print("Result : " +str(Data_testing))

"""
Cara kerja dari fitur .starswitch dan .endswitch yang dimana sama seperti fitur .upper dan fitur .lower yang dimana harus sangat di perhatikan huruf besar dan kecil,
akan tetapi pada case ini kita berfokus terhadap fitur .starswitch dan .endswitch yang dimana pemakainnya dan cara kerjanya. Yang dimana kitak anda sudah menulisakan code 
dari fitur(star dan end), maka anda harus menuliskan kembali sebuah variable di depan fitur tersebut. Contoh pada fitur .starswitch maka anda harus menuliskan sebuah variable
di dalam sebuah string dengan variable pertama anda, dan pada fitur .endswitch maka anda harus menuliskan sebuah variable di dalam sebuah string dengan variable terakhir anda. 
"""

print("\t")

# Menggambil sebuah string dengan string menggunakan slicing
Nama   = "Muhammmad Fadel"
result = (Nama [5])
print(result)

"""
Penggunaan sebuah string dengan string pada slicing yang dimana cara penggunaan dan kerjanya yaitu. Anda harus membuat sebuah variable yang di dalamnya ada string berisi sebuah string
dan membuat sebuah variable baru. serta menuliskan sebuah variable lama (Data utama), dan menaruh sebuah method slicing bisa disebut (subsequence). untuk simbol dari slicing yaitu
menggunakan kurung siku untuk melakukan [] pengoperasian, dan tidak lupa pulah untuk mengisi angka Plus maupun min (1 atau -1) untuk mencari data yang akan di outputkan.
Dan membuat simbol tuple () pada variable ke dua yang dimana wajib di tulis di bahasa ppemrograman pyhon
"""

# Menggambil sebuah angka decimal (floating-point atau floating), dengan list menggunakan slicing
Data   = [1.3, 3.74, 4.32,]
result = (Data [1:3])
print(result)

"""
Penggunaan sebuah angka decimal (floating-point atau floating) pada slicing yaitu anda harus paham terlebih dahulu cara floting (float) pada pemrograman. Dan untuk cara kerjanya dan 
menggunakannya sama seperti contoh string yang dimana anda harus membuat sebuah variable utama yang di dalamnya mennggunakan kurung siku [] untuk mengisi data berupa angka float
sebagai contoh (1.1), dan membuat variable baru berserta data yang akan di operasikan (Data utama) dan tidak lupa pulah menaruh slicing bisa disebut (subsequence). untuk simbol dari slicing yaitu
menggunakan kurung siku untuk melakukan [] pengoperasian untuk mengisi angka Plus maupun min (1 atau -1) untuk mencari data yang akan di outputkan.
Dan membuat simbol tuple () pada variable ke dua yang dimana wajib di tulis di bahasa pemrograman pyhon
"""

# Menggambil sebuah angka int dengan output tuple menggunakan slicing 
Data   = 1,2,3,4,5,6,7,8
result = (Data [-4:6])
print(result)

"""
Penggunanan sebuah angka int dengan output tuple pada slicing ialah anda harus sangat memahami cara penggunaan sintak int pada python. Dan untuk cara kerjanya dan menggunakannya ialah
membuat sebuah variable terlebih dahulu, dan memasukan inputan yang berupa angka int contoh (1 sampai ---), dan tidak lupa pulah untuk menaruh titik coma (,) yang berguna untuk melakukan 
space pada sebuah bahasa pemrograman. Dan buat lagi sebuah variable baru yang berguna untuk melakukan pengoperasian, serta membuat simbol tuple () yang wajib di tulis di bahasa ppemrograman pyhon.
Dan tidak lupa pulah menaruh slicing bisa disebut (subsequence). untuk simbol dari slicing yaitu menggunakan kurung siku untuk melakukan [] pengoperasian untuk mengisi angka Plus maupun min (1 atau -1) 
untuk mencari data yang akan di outputkan.() pada variable ke dua yang dimana wajib di tulis di bahasa pemrograman pyhon
"""

# Menggambil sebuah angka binary dengan input tuple menggunakan slicing
Data   = (1,10,110,111)
result = (Data [0:4:1])
print(result)

"""
Penggunanan sebuah angka binary dengan input tuple pada slicing ialah anda harus sangat memahami cara penggunaan sintak int pada python. Dan untuk cara kerjanya dan menggunakannya ialah
membuat sebuah variable terlebih dahulu, dan memasukan inputan yang berupa angka int contoh (1 sampai ---), dan tidak lupa pulah untuk menaruh titik coma (,) yang berguna untuk melakukan 
space pada sebuah bahasa pemrograman. Dan buat lagi sebuah variable baru yang berguna untuk melakukan pengoperasian, serta membuat simbol tuple () yang wajib di tulis di bahasa ppemrograman pyhon.
Dan tidak lupa pulah menaruh slicing bisa disebut (subsequence). untuk simbol dari slicing yaitu menggunakan kurung siku untuk melakukan [] pengoperasian untuk mengisi angka Plus maupun min (1 atau -1) 
untuk mencari data yang akan di outputkan.() pada variable ke dua yang dimana wajib di tulis di bahasa pemrograman pyhon
"""

# Pengabungan string, binary, floting, int dengan list dalam array menggunakan slicing  
Data   = [{"Hallo World"} , {1,10,110,111}, {12.3,6.5,44.6}, {5,4,3,2,1}]
result = (Data[-3:-1])
print(result)

"""
Pada penggunaan method slicng bisa digunakan pada string, binary, (floating-point atau floating), int yang cara penggunaan dan melakukan pengoprasian pada method ini sama seperti 4 contoh 
di atas, yang membedahkan ialah pengisian angka pada slicing (arugmen, [angka]) bisa menggunakan 1 angka, 2 angka menggunakan simbol (:), bisa menggunakan 2 angka berupa min atau plus, bisa
menggunakan kedua angka min (-2:-2), bisa menggunakan 3 angka. Dan tidak bisa menggunakan  hexadecimal,
"""

print("\t")

# Penggunaan method find dengan str (substring) pada importan stirng 
Word    = "Muhammad Fadel Ganteng dan berotot"
testing = "berotot"
result  = Word.find(testing)
print(result)

"""
Pada penggunaan method find yang dimana cara kerja dan penggunannya sama seperti penggunaan index.Dan untuk cara kerjanya anda harus membuat terlebih dahulu sebuah variable utama berseta 
isian, yang didalamnya ada sebuah string menggunakan tuple maupun list, setelah itu buatlah variable yang berujuk pada pencarian data pada variable utama dan harus di ingat bahwa
ketika menggunakan string pada variable utama, makah variable unutk testing (pengujian/pengambilan data) harus menggunakan string pulah. Dan buatlah kembali sebuah variable baru untuk
melakukan pengoperasian terhadapat variable utama + menambahakan sebuah method .find dan buatlah sebuah list berserta variable yang ingin dicari (variable ke dua)
"""

# Penggunaan method find dengan int (substring) pada importan string 
Number  = ("1,2,3,4,5,6,7")
testing = "4"
result  = Number.find(testing)
print(result)

"""
Pada penggunaan method find dengan int pada importan string, harus menggunakan tuple di dalam list atau hanya menulisan menggunakan tuple saja, kenapa dikarankan pada method find hanya 
bisa melakukan pengoperasian berupa str saja, jika ingin benar-benar menggunakan find maka anda harus membuat sebuah deklarasi terlebih dahulu yang menggunakan range untuk menentukan atau 
mencari angka int maupun float serta binar serta bisa menggunakan simbol penutup [], (), 
"""

# Penggunaan method find dengan str serta melakukan penginputan substring, start, end pada string
Sampel  = "Saya belajar pyhton untuk bisa belajar bahasa script dengan mudah"
testing = " "
result  = Sampel.find(testing, 7, 15)
print(result)

print("\t")


# Part 2 cara menggunakan method find
"""
Pada penggunaannya sama seperti contoh penggunaan str, akan tetapi cara kerjnya ialah pada variable ke2 untuk bagian datanya anda harus mengkosongkan isian tuple supaya bisa melakukan pencarian
pada variable utama ketika melakukan pengoperasian menggunakan method find, dan buatlah sebuah variable baru dengan isian menggunakan simbol tuple + melakukan space sekali, dan buatlah variable baru (ke 3)
sertah melakukan pengembalian variable utama (melakukan pengisian variable 1) dan menambahankan method .find pada isian variable baru tersebut dan melakukan penulisan pada variable ke 2 dan menaruh angka 
yang berguna untuk melakukan Star untuk angka pertama dan End untuk angka kedua. Rumus dari penggunaan find menggunakan 3 parameter yaitu (Substring, + Star + End)

Penggunaan code .find yang atas adalah bentuk dari shortcut penulisannya
"""

"""
Method find adalah sebuah fungsi pada tipe data string di Python yang digunakan untuk mencari indeks dari suatu substring pada string utama.

find() Syntax.
                str.find(Sub[, Star[, End]

find() Return Value :
                        1. Jika substring ada di dalam string, ia mengembalikan indeks kemunculan pertama substring tersebut.
                        2. Jika substring tidak ada di dalam string, ia akan mengembalikan -1 .
"""

#Contoh penggunaan method find() dalam importan string tanpa menggunakan argumen (parameter) Star dan End
Data = "Saya suka pergi keluar malam saat lagi pusing"
print(Data.find('suka'))

"""
Pada penggunaan method find tanpa menggunakan arugmen (Parameter) pada code diatas yang dimana kita hanya memasukan sebuah substring dari string dalam value pada sebuah variable. Dan untuk hasil inputannya berubah sebuah numerik (angka)
dan angka tersebut merupakan sebuah integer yang dimana setiap kita memasukan substirng dari string dalam value pada sebuah variable contohya pada variable pertama kita memasukan inputan substring 'suka' sehing metod find akan melakukan 
pencarian posisi substring 'suka', yang dimana akan menghasilkan angka 5, kenapa hasilnya angka 5. Itu dikarenakan pada method find akan menghitung posisi dari substring yang diinput. 
""" 

Data = "Berusah menjadi seorang yang ahli dalam sebuah pengamanan sistem"
print(Data.find("Cyber Security"))

"""
Pada code diatas bisa dilihat untuk inputan substringnya adalah 'Cyber Security' yang dimana tulisan 'Cyber Security' string dalam value pada sebuah variable. Itu tidak ada sehingga method find akan menggeluarkan angka -1 itu sebagai tanda 
bahwa substring yang diinputkan tidak ada dalam stirng alam value pada sebuah variable. 
"""

# Contoh penggunaan method find() Dengan parameter star dalam importan string
Data = "Saya tenang kita tidak ada orang yang banyak tanya"
print(Data.find("kita", 12,))  # Start parameter: 12


"""
Pada cara kerja dari code yang diatas dimana kita memasukan inputan substring dari string dalam value pada sebuah variable yang dimana pada penggunaan star akan mencari kalimat 'kita' pada value dalam variable yang dimana akan di hitung
dari sebelah kanan hingga akhiran abjad pada huruf pertama kalimat, dan untuk parameter star kenapa diinput '12' bukan '1', di karnakan pada penggunaan ini hanya awalan untuk memahami cara kerja menggunakan method find. 
"""

# Contoh penggunaan method find() Denagn parameter star dan end dalam importan string
Data = "Kita saya lagi sedih saya akan cepat tidur paada malam hari"
print(Data.find("cepat", 1, 36,))

"""
Pada cara kerja dari code yang diatas  kita memasukan inputan substring dari string dalam value pada sebuah variable yang dimana pada penggunaan star akan mencari kalimat 'cepat' pada value dalam variable yang dimana akan di hitung,
dari sebelah kanan hingga akhiran abjad pada huruf pertama kalimat. Dan untuk parameter pertama (star) kita menginput angka '1' yang dimana angka 1 ini bersifat default dari bawahan pencarian terhadap method find. Dan untuk parameter
kedua (end) kita menginput angka '36' dikarnakan kalimat 'cepat' berakhir pada abjad 't' kenapa bisa, itu kerena fungsi parameter 'end' akan slelau mengakhir abjad terakhir pada kalimat inputan substring.
"""

print("\t")

# penggunaan method rfind dengan str (substring) pada importan stirng 
Word     = "Saya akan menjadi mliader pertama di keluarga saya"
testing  = "pertama"
result   = Word.rfind(testing)
print("Pencarian sebuah substing 'pertama' di '{}' antara '{}' hasil '{}'" .format(Word, testing, result))

"""
Pada penggunaan method .rfind pada importan string. Yang dimana cara penggunaannya sama seperti method find dan cara kerjanya sama halnya layak method find.
"""

# penggunaan method rfind dengan angka menggunkan string di dalam pada importan string
Number   = ("22.1, 44.2, 32.3, 55.4, 65")
testing  = "32.3" 
result   = Number.rfind(testing)
print("Pencarian sebuah angka '32' di '{}' antara '{}' hasil '{}'" .format(Number, testing, result))

"""
Pada penggunaan method rfind pada case ini sama kayak contoh penggunaan pada method find pada case angka di lapisi tuple
"""

# penggunaan method rfind dengan str serta melakukan penginputan substring, start, end pada string
Word     = "Selalu menjadi orang yang bermanfaat bagi keluarga dan masyarakat"
testing  = " "
result   = Word.rfind(testing, 6, 8)
print("Hasil dari sub, star, end di '{}' antara '{}' hasil '{}'" .format(Word, testing, result))

"""
Pada penggunaan method rfind sama halnya seperti method find yang dimana berguna melakukan pembagian rumus (sub, star end) 

Penggunaan code .rfind yang di atas adalah bentuk dari long syintax, dan bisa digunakan pada method .find juga tentunya
"""

print("\t")

# penggunaan method format pada string
Data = (f"Hallo nama saya muhammad {{'fadel'}}")
print(Data)

"""
Pada penggunaan dari method .format yang dimana pada case ini kita langsung menambahkan variable baru di data utama kita, dan tidak lupa pulah untuk menaruh methodnya harus di luar tuple, stirng. dan untuk simbolnya
anda harus menggunakan simbol {} untuk menaruh/menambahkan char (Krakter) yang ingin di masukan. Dan wajib menaruhkan 2 kali simbolnya berseta single quate supaya mewakili angka yang ingin dimasukan
"""

Data    = "Hallo nama saya muhammad {'fadel'}"
print (format(Data))

"""
Pada penggunaanya yang dimana kita menaruh method format pada hasil outputnya, dan tidak lupa pulah memasukan variablw di dalam inputan pada output
"""

print("\t")

# Penggunaan method replace dengan str (substring) pada importan stirng 
Word = ("Saya suka makan ayam") #Data utama yang akan di modif
print (Word.replace("makan", "tidak"))

"""
pada penggunaan syintax diatas yang dimana pada hasil output pada method replace pada double quote pertama kita menuliskan kembali string yang akan kita ubah pada data utama, dan pada double quote yang kedua 
yang dimana berfung sebagai penganti data (string) pada data utama yang bertuliskan makanan.
"""

# Contoh method replace menggunakan 2 sampel Data
Data   = ("Saya suka makan ayam") #Data utama yang akan di modif
Result = Data.replace("makan", "tidak")
print (Result)

print("\t")

# Contoh method replace mengganti beberapa str (substring) dalam sebuah data utama, + membandingkannya (Data, Hasil datanya)
Sampel = ("Hari itu seperti hari lainnya, cerah dan cerah") #Data utama yang akan di modif
Result = Sampel.replace ("Hari", "Malam").replace ("cerah", "gelap").replace("cerah", "suram")
print(Sampel)
print(Result)

"""
Pada penggunaannya yang dimana kita bisa melakukan modif string pada suatu data, yang melebihi 2X argumen. Untuk cara tersebut anda harus melakukan penulisan method replace setiap kali selesai mendeskripsikan data 
yang akan diubah, dan data yang ingin di modif (penulisan) harus sama seperti data awalanya. Di karenakan pada python memiliki case-sensitive.
"""

# Contoh penggunaan method replace pada importan string dalam array
a = ["apple", "banana", "cherry"]
b = [item.replace("a", "e") for item in a]
print(b)

"""
Pada penggunaan method replace pada importan string dalam array, untuk cara penggunaannya sama hal seperti penggunaan method replace pada umumnya. Akan tetapi untuk cara melakukan pemrosesan yang agak berbedah yang dimana
pada case ini menggunakan elemen loop yaitu "for" dan "in" yang berguna melakukan pencarian terhadap abjad "a" dan abjad "b"
"""


# Contoh penggunaan int (Angka) dalam method replace pada importan string
Data = ("083812854878")
print(Data.replace("8", "-", 2))

"""
Pada contoh di atas, kita akan mengganti karakter “8” dalam teks nomor telepon ini menjadi karakter “-”, namun yang ingin kita ganti hanyalah tiga teks pertama yang ditemukan. Dengan menggunakan fungsi replace ini 
dan menentukan berapa banyak karakter yang akan diubah, maka kita bisa mengubah output dari tipe data teks ini menjadi bentuk lainnya.
"""

# Contoh method replace menggunakan 2 sampel Data
Data   = ("083812854878")
Sampel = Data.replace("8", "-", 3)
print(Sampel)


# Contoh penggunaan method replace pada importan string dalam array menggunakan int
a = ["083812854878", "083123492102", "085323858593"]
b = [item.replace("2", "-", 4) for item in a]
print(b)

"""
Pada penggunaanya sama seperti contoh penggunaan method repalce pada string dalam array, yang membedahkah ialah data yang dimasukan didalam ini menggunnakan int yang dilapisi oleh sebuah string 
"""

print("\t")

# Contoh penggunaan method tilte pada importan string 
Data = (
    "halo perkenalkan nama saya muhammad fadel saya perkuliah disalah satu kampus swasta di kota palu\n"
    "saya bercita-cita kerja sebagai konsultan cyber yang dimana saya harus belajar hampir semua hal di TI (teknik informatika)"
)
print(Data.title())

"""
Metode "title()" pada string Python digunakan untuk mengubah setiap kata dalam string menjadi format judul, di mana setiap kata dimulai dengan huruf kapital dan karakter lainnya diubah menjadi huruf kecil. Ini berguna ketika Anda 
ingin memformat string agar terlihat seperti judul, dengan huruf kapital di awal setiap kata.Namun, perlu diingat bahwa metode title() hanya mempertimbangkan kata-kata dalam string, jadi jika ada karakter non-kata di antara kata-kata, mereka juga 
akan dimulai dengan huruf kapital
"""

print("\t")

# Contoh penggunaan method is alpha pada importan string
Data   = ("MuhammadFadel")
print(Data.isalpha())

Data   = ("Muhammad Fadel")
print(Data.isalpha())

Data   = ("Muhammad Fadel 13")
print(Data.isalpha())

"""
Pada penggunaan method isalpaha yang dimana digunakan untuk memeriksa apakah semua karakter dalam sebuah string adalah alfabet (huruf), artinya tidak termasuk angka atau karakter khusus lainnya. Jika semua karakter dalam string adalah huruf, 
maka metode ini akan mengembalikan nilai True, dan jika ada setidaknya satu karakter yang bukan huruf, maka akan mengembalikan nilai False. Nilai false itu sendiri dikarenakan juga adanya space pada alfabet pada setiap karakter yang di input.
"""

print ("\t")

# Contoh penggunaan method casefold pada importan string 
Data = "MUHAMMAD FADEL"
print(Data.casefold())

# Contoh perbedaan casefold dan lower
sampel = "Helloß"
print("Menggunakan method casefold", sampel.casefold())
print("Menggunakan method islower", sampel.lower())

"""
casefold() digunakan untuk melakukan normalisasi string dalam hal perbandingan yang case-sensitive. Metode ini lebih kuat daripada lower() karena mampu menangani kasus khusus. casefold() mengubah karakter dalam string menjadi huruf kecil dan, 
juga menangani karakter-karakter yang tidak umum dalam bahasa Inggris dan bahasa-bahasa lainnya. Sedangkan lower() hanya mengubah karakter-karakter ASCII menjadi huruf kecil. 
"""

print("\t")

# Contoh penggunaan method capitalize pada importan string
Data = "Muhammad Fadel"
print(Data.capitalize())

# Contoh penggunaan 2 Data pada method capitalize dalam importan string
Data   = "Saya suka MAKANAN"
Result = Data.capitalize()
print(Result)

"""
Metode capitalize() mengembalikan salinan string dengan perubahan tersebut, sementara string asli tetap tidak berubah. Jadi jika Anda ingin mengubah string asli, Anda harus menyimpan hasil dari metode capitalize() dalam variabel yang sama atau variabel yang baru.
"""

# Contoh perbedaan antara capitelize dan title dalam importan string
Data = "saya suka makanan yang dimasak oleh mama saya"
print(Data.capitalize())

Data = (
    "saya suka makananan yang dimasak oleh mama saya"
)
print(Data.title())

"""
Pada perbedaan antara method capitalize dan method title. Yang dimana pada capitalize ketika kita menuliskan sebuah string pada inputan sebuah variable yang dimana pada alfabet dalam inputan varibale akan di capslock (Dipertebal), 
mesikpun pada variable yang menggunakan method capitalize ada huruf besar (capslock).
Sedangkan pada method tilte. Yang dimana pada title kita menulisakan sebuah string pada inputan varibale yang dimana pada setiap alfabet pertama yang di inputkan akan di capslock (Dipertebal), dikarnakan cara kerja dari
method title akan menghasilkan tulisan yang menghasilkan judul (Tulisannya).
"""

print("\t")

# Contoh penggunaan method count pada importan string
Data = "Saya suka sekali masakan ibu saya"
print(Data.count("s"))

# Contoh penggunaan method count pada 2 variable dalam importan string
Data   = "Saya suka sekali masakan ibu saya"
Result = Data.count("s")
print(Result)

# Contoh penggunaan count menggunakan int menggunakan 2 variable importan string
Data   = 1, 2, 3, 1, 3, 2, 5
tesing = Data.count(3)
print(tesing)

# Contoh penggunaan count menggunakan floating  menggunakan 2 variable importan string
Data   = 1.1, 3.2, 4.2, 1.1, 3.2
tesing = Data.count(4.2)
print(tesing)


"""
Pada penggunaan method count terutama dalam importan string yang dimana untuk penulisan syintax codenya sama seperti code importan string lainnya. Yang membedah kan ialah cara kerja dan kegunaannya yang dimana method ini berkerja layaknya penghitungan,
dan bisa digunakan pada tipe data (str, int, floating)
"""

# Contoh pengunaan method count character in multiple string dalam array
Data    = ["Martabak", "Nasi_kuning", "Ayam"]
testing = "u"
Result  = max(Data.count(testing) for Data in Data) 
print(Result)

"""
Pada penggunaan method count character in multiple string dalam array yang dimana untuk kegunaannya sama seperti penggunaan pada umumnya yang dimana akan mencari hasil dari value dalam variable utama. Akan tetapi dalam penyelesainya kita menggunakan,
2 variable dengan isian datanya (Value), pada variable pertama yang dimana akan menjadi sampel data yang akan di cari, pada variable ke 2 berfungsi sebagai pencarian data, pada variable utama. Dan pada variable ke 3 berfungsi sebagai penggabungan dari 
kedua variable berseta valuenya (isiannya), serta kita menambahkan fungsi matimatika dalam pytho (max) tanpa menggunakan modul math, dan tidak lupa pulah memasukan method count serta looping yaitu (for, in)
"""

# Contoh penggunaan method count menggunakan Regular Expression (modul) pada importan string 
import re

Data    = "Apakah besok cerah dan indah?"
testing = "cerah"
Result  = len(re.findall(testing, Data))
print(Result)

"""
Pada pengguan code di atas kita menggunakan import re yang dimana import re berguna sebagai untuk mengakses modul regular expression yang berguna untuk melakukan manipulasi teks, pencarian pola, dan penggantian teks. Serta pada code di atas menggunakan 3 variable
pada variable ke 1 berguna sebagai data utama pada variable ke 2 yang dimana berguna sebagai pencarian data pada variable pertama ke di inputkan. Dan pada variable ke 3 yang dimana kita menggunakan fitur arry pada elemen len yang dimana len() digunakan untuk menghitung jumlah 
elemen dalam suatu objek seperti string, daftar (list), tuple, atau struktur data lainnya. Setelah itu tulislah lagi modul re bersama finddall yang dimana findall() pada Python digunakan untuk mencari semua kemunculan suatu pola atau regular expression dalam sebuah string dan 
mengembalikan hasilnya dalam bentuk list,  dari modul re. Hasilnya adalah list yang berisi dua kemunculan kata (variable) yaitu "testing" dan "Data"
"""

print("\t")

# Untuk penggunaan method encode pada importan string yang dimana akan di pisahkan dari kelompoknya dikarnakan pembahasan yang sangat rumit + kompolek kalau tidak di bahas

# Contoh penggunan method endswitch tanpa parameter pada import string
"""
Method endswith() adalah metode bawaan Python yang digunakan untuk memeriksa apakah string berakhir dengan karakter atau substring tertentu.
Metode ini mengembalikan nilai True jika string berakhir dengan karakter atau substring yang ditentukan dan False jika tidak.
"""

Data = "Muhammad Fadel."
print(Data.endswith("Muhammad Fadel."))
print(Data.endswith("Fadel."))
print(Data.endswith("Muhammd Fadel"))

"""
pada penggunaan method endswitch pada import string yang dimana cara kerjanya hanya menghasilkan outputan berupa True atau false semata  ketika kita melakukan penginputan terhadap value pada suatu variable. 
Method endswith() pada string di Python bersifat case sensitive atau memperhatikan huruf besar-kecil dari karakter yang dibandingkan. Jika Anda ingin melakukan pencarian yang tidak memperhatikan huruf besar-kecil, 
Anda dapat mengubah kedua string menjadi huruf kecil menggunakan method lower() atau huruf besar menggunakan method upper() 

Sintaksnya endswith()adalah:
                                str.endswitch(suffix[, start[, end]])

endswith() Parameters :
                            1. suffix - String atau tupel sufiks yang akan diperiksa.
                            2. start (opsional) - Posisi awal di mana akhiran harus diperiksa dalam string.
                            3. end (opsional) - Posisi akhir di mana sufiks harus diperiksa dalam string.

Multiple suffix pada Python adalah kemampuan untuk menentukan lebih dari satu ekstensi file pada saat menyimpan file. Manfaat dari penggunaan multiple suffix pada Python adalah untuk memberikan informasi tentang tipe data yang 
terkandung dalam file tersebut. Dengan mengetahui tipe data tersebut, kita dapat memilih alat yang tepat untuk membuka dan memproses file tersebut. Selain itu, penggunaan multiple suffix juga membantu dalam mengorganisir file-file 
dalam sebuah proyek secara lebih efektif. Meskipun biasanya multiple suffix digunakan pada nama file, namun sebenarnya hal ini dapat digunakan pada string apa pun di Python.
"""

print("\t")

# Contoh penggunaan method endswith() Dengan parameter star dalam importan string

"""
Pada penggunaan method ini yang dimana hanya akan menghasilkan sebuah outputan boolean pada setiap hasil inputan pada parameter. 
Untuk hasil yang benar akan mengoutputkan True dan jika salah akan menginputakn hasil False
"""

Data = "saya suka makanan mama Saya"
print(Data.endswith("Saya", 23,)) # Start parameter: 23

"""
Pada code diatas yang dimana kita menggunakan sebuah parameter untuk melakukan pencarian terhadap inputan string 'Saya' yang dimana pada penggunaan code ini kita hanya menggunakan sebuah parameter star, dan parameter star itu sendiri 
adalah angkah '23' yang dimana posisi dari awalan kalimat Saya yaitu 'S' berada pada posisi ke 23 dalam value pada sebuah variable (Data)
"""

# Contoh penggunaan method endswitch() Dengan parameter Star dan End dalam importan string
Data = "Muhammad Fadel"
print(Data.endswith("Fadel", 4, 14)) # Start parameter: 4. End parameter : 14

"""
Pada penggunaan code diatas yang dimana kita menggunakan 2 parameter, yang dimana parameter tersebut ialah star pada angka 1 dan end pada angka ke 2. Untuk cara kerja dari method endswitch menggunakan 2 parameter yang dimana.
Untuk star berguna sebagai pencarian posisi pada substring yang telah diinput, dan pada parameter yang kedua 'End' yang dimana sebagai tujuan akhir dari substring yang diinput atau lebih gampangnya, ialah hasil dari keseluruan 
string yang berada pada value dalam sebuah variable. Sehingga pada contoh inputan numerik dalam parameter Star dan End ialah '4' dan '14', '4' sebagai tujuan yang ingin dicari dan '14' sebagai hasil keseluruan string (jumlah abjadnya)
"""

print("\t")

# Untuk penggunaan method format pada importan string yang dimana akan di pisahkan dari kelompoknya dikarnakan pembahasan yang sangat rumit + kompolek kalau tidak di bahas

# Contoh penggunaan method index dalam importam string

"""
index syintax :

                str.index(sub[, start[, end]] )

Kegunaan substring yaitu                       : string (isian) yang akan dicari.
Kegunaan star (defaultm :0) yaitu              : Menentukan posisi awal pencarian. 
Kegunaan end (default : panjang string ) yaitu : Menentukan posisi akhir pencarian.
Kegunaan return (Opsional) yaitu               : Mengembalikan posisi pertama substring yang ditemukan.

Method index() dalam pemrograman python yang dimana untuk mengetahui posisi elemen pada array list '[]', serta dalam array list. Yang dimana dalam setiap elemen indeks yang memungkinkan kita untuk mengakses atau memodifikasi nilainya. 
Untuk mengakases nilai dalam list, kita dapat menggunakan tanda kurung siku dengan indeks elemen yang ingin diakses. Dan jika ingin mengetahui posisi karakter tertentu dalam sebuah kalimat anda dapat menggunakan fungsi index dengan 
menambahkan karakter sebagai argument '("muhammad")'.

Dalam penggunaan index kita dapat untuk melakukan menggelola data dalam list seperti halnya,  ( mengambil, mengubah, menambah, menghapus) pada ke empat fungsi tersebut yang dimana hal mempermudah manipulasi dan pengelolaan data dalam python.
"""

a = 'muhammad fadel'
print("cari lah subtring",a.index('fadel')) # Contoh implementasi penggunaan pencarian substring dalam method index pada importan string method menggunakan 1 variable.


x = "berusah menjadi consultan cyber"
y = x.index('menjadi')
print("cari lah substring", y) # Contoh implementasi penggunaan pencarian substring dalam method index pada importan string method menggunakan 2 variable.


a = "muhammad fadel"
b = 'fadel'
c = a.index(b)
print("mencari substring dari kata 'fadel'", c) # Contoh implementasi penggunaan pencarian substring dalam method index pada importan stringg method menggunakan 3 variable. 

"""
Pada code yang menggunakan 1 variable. Yang dimana kita melakukan 1 kali deklarasi, serta melakukan pengouputan (pengoperasian) dan penggabungan pencarian subsring dalam satu perintah print.

Pada code yang menggunakan 2 variable. Yang dimana pada variable 'x' kita jadikan sebagai sample (data) yang akan di analisis/cari, dan untuk variable 'y' yang dimana berperan sebagai penggabungan dari variable 'x' dan dari penggabungan 
variable 'x' setelah itu kita menuliskan method importan string di sampingnya, serta kita menuliskan simbol string '()' dan menuliskan code single quote yang dimana dari simbol string dan code single quote '' berguna untuk melakukan pencarian 
data yang kita ingin cari. Dan setelah itu kita mencari substring yang ingin kita eksekusi di dalam simbol string dan code single qoute di dalamnya.
Setelah mengurutkan struktur datanya, jangan lupa untuk menuliskan sytanx 'print' berserta kata-kata yang ingin di outputkan dari sytanx print, dan tidak lupa pulah menaruh simbol koma ',' yang berguna untuk memisahkan data dari data yang lain
jangan lupa untuk menuliskan kembali variable 'y', yang dimana berguna untuk output dari melakukan pengoperasian struktur datanya. 

Pada code yang menggunakan 3 variable. Yang dimana pada variable 'a' kita jadikan sebagai sample (data) yang akan di analisis/cari, dan untuk variable 'b' berguna sebagai pencarian substring  data pada variable 'a'. 
Dan untuk variable 'c' yang dimana yang dimana berperan sebagai penggabungan dari variable 'x' dan dari penggabungan variable 'a' dan 'b' setelah itu kita menuliskan method importan string di sampingnya, serta kita menuliskan simbol string '()' 
Dan tidak pulah kita memasukan variable b didalam simbol string '()' fungsi dari b didalam string yang dimana berguna untuk melakukan penggabungan terhadap variable 'a' yang telah disingkronkan dengan method 'index' pada importan string.
Jangan lupa untuk menulisakan sytanx 'print' berserta kata-kata yang ingin di outputkan dari sytanx print, dan tidak lupa pulah menaruh simbol koma ',' yang berguna untuk memisahkan data dari data yang lain 
jangan lupa untuk menuliskan kembali variable 'y', yang dimana berguna untuk output dari melakukan pengoperasian struktur datanya. 
"""

