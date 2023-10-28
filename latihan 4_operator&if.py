# 1. Buat program phyton untuk menambahkan waktu dan nama ke dalam pesan selamat menggunakan assignment operator dan di print.
pesan = 'Assalamualaikum, selamat '
waktu = 'Pagi '
nama = 'Aziz'

pesan += waktu
pesan += nama
print(pesan)

# 2. Buat program phyton untuk mencari tahu apakah makanan ada dalam list makanan favorit.
list_makanan_favorit = ('ayam bakar','mie goreng','sate padang')
makanan = ('semur jengkol')
print(makanan in list_makanan_favorit)

# 3. Buat program phyton untuk menentukan jika akun login adalah admin, user, atau, bukan keduanya.
akun = 'admin'
if akun == 'admin':
    print('anda adalah admin')
elif akun == 'user':
    print('anda adalah user')
else:
    print('anda bukan siapa - siapa')

# 4. Buat program phyton untuk mengecek apakah angka adalah kelipatan 5.
angka = 2050
if angka % 5 == 0:
    print(angka, 'adalah kelipatan 5')
else:
    print(angka, 'bukan kelipatan 5')

# 5. Buat shorthand if else menentukan untuk naik kora2, "tidak bisa naik" jika tinggi dibawah 150cm.
tinggi_badan = 170
if tinggi_badan >= 150:
    print('anda bisa naik')
elif tinggi_badan < 150:
    print('anda tidak bisa naik')
    