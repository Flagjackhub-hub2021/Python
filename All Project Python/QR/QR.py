
# Importing library
import qrcode
 
# Data to be encoded
data = 'QR Code using make(https://kota-palu.kpu.go.id/berita/baca/8168/pengumuman-nomor-163-tahun-2024-tentang-pendaftaran-dan-persyaratan-pemantau-dan-lembaga-survei-pilkda-wali-kota-dan-wakil-wali-kota-palu-tahun-2024/) function'
 
# Encoding data using make() function
img = qrcode.make('https://kota-palu.kpu.go.id/berita/baca/8168/pengumuman-nomor-163-tahun-2024-tentang-pendaftaran-dan-persyaratan-pemantau-dan-lembaga-survei-pilkda-wali-kota-dan-wakil-wali-kota-palu-tahun-2024/')
 
# Saving as an image file
img.save('KPU.png')