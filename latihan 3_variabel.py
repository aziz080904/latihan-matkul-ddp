# Nama sendiri
nama = 'Aziz Maulana Hakim'
nim = '0110223208'
kelas = 'TI07'
no_telp = '081210034200'
alamat = '''Jalan Mandala RT 001 RW 002 Kelurahan Cijantung
Kecamatan Pasar Rebo 
Kota Jakarta Timur Kode Pos 13770
''' 
print(nama)
print(nim)
print(kelas)
print(no_telp)
print(alamat)

# Nama teman
nama_teman = 'Khoirusyamil yahya'
nim_teman = '0110223226'
kelas_teman = 'TI07'
no_telp_teman = '081905287897'
alamat_teman = '''Jl Masjid Bendungan 2 Rt 02 Rw 07 No.21
''' 
print(nama_teman)
print(nim_teman)
print(kelas_teman)
print(no_telp_teman)
print(alamat_teman)

#berat badan ideal
tinggi_badan = 170
berat_badan_ideal = (tinggi_badan - 100) - (tinggi_badan - 100) * 0.10
print('berat badan yang cocok untuk tinggi badan 170 adalah',berat_badan_ideal)

#celcius ke fahrenheit
celcius = int(input('Masukkan derajat celcius :'))
fahrenheit = celcius * 1.8 + 32
print(fahrenheit)

#luas dan keliling tabung
r = int(input('Masukkan jari-jari :'))
t = int(input('Masukkan tinggi :'))
pi = 3.14
luas_permukaan = 2 * pi * r * (r + t)
keliling = 2 * pi * r 
print(luas_permukaan)
print(keliling)