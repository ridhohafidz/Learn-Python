# DDP LAB-4
# Nama: Muhammad Ridho Hafidz
# NIM: 0110219051

# SOAL 1 - Mencetak nama
# Tuliskan program untuk Soal 1 di bawah ini
print("--------------------------------------------------------------")
print("SOAL 1 - Mencetak Nama")
print("--------------------------------------------------------------")
# variabel menginput nama
x = input("Masukkan Nama : ")
# fungsi len untuk mengitung panjang string
y = len(x)
# start looping dari 0
z = 0

# variabel z lebih kecil dari hitungan panjang string pada variabel x
while z < y:
  # variabel z akan terus bertambah setia perulangan
  z = z + 1
  # mencetak hasil dengan string slicing
  print(x[0:z])
print('\n')







# SOAL 2 - Validasi teks
# Tuliskan program untuk Soal 2 di bawah ini
print("--------------------------------------------------------------")
print("SOAL 2 - Validasi Teks")
print("--------------------------------------------------------------")
# inisialisasi variabel
belumValid = True
# perulangan while
while (belumValid) :
  #variabel menginput sebuah teks
    teks = str(input("Masukkan sebuah teks: "))
    # operator in digunakan untuk memeriksa apakah suatu string mengandung sesuatu dan menggunakan method string endswith
    if (len(teks) >= 8 and ('nf' in teks.lower()) and (teks.endswith('YYY') or teks.endswith('yyy'))):
        daftarAngka = '123456789'
        mengandungAngka = False
        # perulangan for menggunakan fungsi operator in pada string
        for angka in daftarAngka:
            if angka in teks:
                mengandungAngka = True
                belumValid = False
        if not mengandungAngka:
            print('Teks tidak valid.')
    else:
        print('Teks tidak valid.')
print('Teks valid. Program berhenti.') 
print('\n')