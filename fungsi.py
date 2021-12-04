def luas(): # luas = nama fungsi
    print('Hello World')  #  Mengeksekusi perintah

luas()  # Cara memanggil funsi

# Fungsi dengan argumen atau parameter

def selamat_datang(nama):  # nama = parameter atau argumen
    print(f'Halo {nama}, Selamat datang')

selamat_datang('Budi')  # ('Budi') lempar ke parameter (nama)
selamat_datang('Windy')

# parameter wajib

def perkenalan(nama, asal): # 2 parameter yang waktu pemanggilan wajib diisi
    print(f'Halo nama saya {nama}, Saya berasal dari {asal}')

perkenalan('Budi', 'Arab Saudi')  # budi = nama Arab Saudi = asal


# Parameter opsional

def suhu(daerah, derajat, satuan= 'celsius'):  # daerah dan derajat wajib diisi satuan tidak
    print(f'Suhu didaerah {daerah} adalah {derajat} {satuan}')

suhu('Bali', 30)
suhu('Jakarta', 86, 'Farenheit')

# mengembalikan nilai

def luas_persegi(sisi):
    return sisi * sisi

luas_persegi(6)  # tidak mencetak ke layar
print(f' luas dari persegi adalah dengan sisi 6 adalah {luas_persegi(6)} cm')  # mencetak ke layar

#simpan ke dalam variabel
persegi_besar = luas_persegi(10)
persegi_kecil = luas_persegi(7)
print(f'Total luas persegi besar dan kecil adalah {persegi_besar + persegi_kecil} cm')






