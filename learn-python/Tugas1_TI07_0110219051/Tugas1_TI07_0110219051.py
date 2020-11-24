#Nama   : Muhammad Ridho Hafidz
#NIM    : 0110219051
#Kelas  : TI 07 - Weekend

print("Fitur Input Nilai Mahasiswa")
#Menginput NIM
nim = input("Masukan NIM: ")
kondisi = True
#Perulangan variabel kondisi dengan tipe data Boolean [True or False]
while kondisi:
    #Menginput jumlah mata kuliah yang diambil untuk melakukan perulangan, misalkan menginput 2 maka perulangan menjadi 2 kali
    jumlahmatkul = int(input("Berapa Jumlah Mata Kuliah yang diambil ? "))
    #inisialisasi suatu variabel index dipakai setelah menginput jumlah mata kuliah
    i = 0
    #inisialisasi suatu variabel totalsks untuk menampung nilai total sks
    totalsks = 0
    #inisialisasi suatu variabel ip untuk menampung nilai total index prestasi
    ip = 0
    # melakukan validasi jumlah mata kuliah yang dimasukkan
    if jumlahmatkul < 1 or jumlahmatkul > 8:
        print("Jumlah Mata Kuliah antara 1 sampai 8")
        print("\n")
    # Jika pengguna memasukan jumlah mata kuliah 1 sampai 8, jalankan percabangan else
    else:
        #melakukan perulangan ketika kondisi index lebih kecil dari jumlah matkul
        while i < jumlahmatkul:
            #index akan bertambah ketika melakukan perulangan
            i = i+1
            print("Nilai Mata Kuliah", i)
            #menginput nama mata kuliah
            matkul = input("Nama Mata Kuliah: ")
            #menginput beban sks mata kuliah
            sks = int(input("Beban SKS mata kuliah: "))
            #menginput nilai kuis
            kuis = eval(input("Nilai Kuis: "))
            #menginput nilai tugas1
            tugas1 = eval(input("Nilai Tugas 1: "))
            #menginput nilai tugas2
            tugas2 = eval(input("Nilai Tugas 2: "))
            #menginput nilai uts
            uts = eval(input("Nilai UTS: "))
            #menginput nilai uas
            uas = eval(input("Nilai UAS: "))
            #menjumlahkan nilai sks mulai dari mata kuliah pertama dan seterusnya dalam variabel total
            totalsks = totalsks+sks   
            #melakukan penjumlahan bobot nilai untuk setiap mata kuliah dari masing-masing kuis, tugas, uts, dan uas        
            nilai = 0.15*kuis+0.15*tugas1+0.20*tugas2+0.25*uts+0.25*uas
            #untuk mencari index prestasi dan nilai sesuai dengan variabel nilai
            if 85 <= nilai <= 100: #jika variabel nilai antara 85 sampai 100 maka buat variabel grade dengan value A
                grade = "A"
                #index prestasi nya 4.0 dengan tipe data float
                index = float(4.0)
            elif 70 <= nilai < 85: #lain jika variabel nilai antara 70 sampai 85 maka buat variabel grade dengan value B
                grade = "B"
                #index prestasi nya 3.0 dengan tipe data float
                index = float(3.0)
            elif 55 <= nilai < 70: #lain jika variabel nilai antara 55 sampai 70 maka buat variabel grade dengan value C
                grade = "C"
                #index prestasi nya 2.0 dengan tipe data float
                index = float(2.0)
            elif 40 <= nilai < 55: #lain jika variabel nilai antara 40 sampai 55 maka buat variabel grade dengan value D
                grade = "D"
                #index prestasi nya 1.0 dengan tipe data float
                index = float(1.0)
            elif nilai < 40: #lain jika variabel nilai kurang dari 40 maka buat variabel grade dengan value E
                grade = "E"
                #index prestasi nya 0 dengan tipe data float
                index = float(0.0)
            #mencetak nilai mata kuliah
            print("Nilai untuk mata kuliah", matkul,":", nilai, "( grade", grade, ")")
            #melakukan perhitung untuk mendapatkan hasil ip
            ip = ip+(sks*index)
            print("\n")
        #Jika pada perulangan index tidak lebih kecil dari Jumlah Mata kuliah, ubahlah kondisi menjadi False agar perulangan awal berhenti
        kondisi = False

print("Rangkuman")
#Mencetak NIM
print("NIM :", nim)
#Mencetak Total SKS
print("Total SKS :", totalsks)
#Mencetak nilai Index Prestasi dibagi total sks
print("Index prestasi :", round(ip/totalsks, 2)) #fungsi round ini untuk membulatkan suatu bilangan desimal berkoma
