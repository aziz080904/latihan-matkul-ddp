# 1. buatkan program phyton dgn list dengan nilai [kodekendaraan,namakendaraan,cc,warna]
kendaraan = ['B','Innova Reborn','2000cc','hitam']
print(kendaraan)

# 2. dari list nomor 1 tambahkan : diakhir tambah harga dan jumlah roda, disisipkan setelah nama kendaraan merk dan jenis kendaraan
kendaraan.append('470juta')
kendaraan.append('roda empat')
kendaraan.insert(2,'toyota')
kendaraan.insert(3, 'mobil')
print(kendaraan)

# 3. buat program phyton dgn match case i=untuk menghitung luas bangun datar

ket = '''selamat datang di aplikasi menghitung luas bangun datar
pilihan :
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas segitiga
'''
print(ket)
luas = (input('masukkan pilihan :'))

match luas:
    case '1':
        sisi = int(input('masukkan sisi :'))
        luasP = sisi * sisi
        print('maka luas persegi adalah',luasP)
    case '2':
        r = int(input('masukkan jari-jari :'))
        luasL = 3.14 * r * r
        print('maka luas lingkaran adalah',luasL)
    case '3':
        a = int(input('masukkan alas :'))
        t = int(input('masukkan tinggi :'))
        luasS = 0.5 * a * t
        print('maka luas segitiga adalah',luasS)
    case _:
        print('input tidak valid')







