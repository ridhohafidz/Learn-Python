#Nama   : Muhammad Ridho Hafidz
#NIM    : 0110219051
#Kelas  : TI 07 - Weekend

print("Fitur Input Nilai Mahasiswa")
#Menginput NIM
nim = input("Masukan NIM: ")
kondisi = True
#Perulangan variabel kondisi dengan tipe data Boolean [True or False]
while kondisi:
    #Menginput jumlah mata kuliah yang diambil akan melakukan perulangan, misalkan menginput 2 maka perulangan menjadi 2 kali
    jmatkul = int(input("Berapa Jumlah Mata Kuliah yang diambil ? "))
    print("\n")
    #inisialisasi suatu variabel index dipakai setelah menginput jumlah mata kuliah
    i = 0
    #inisialisasi suatu variabel total untuk menampung nilai total sks
    total = 0
    #inisialisasi suatu variabel ip untuk menampung nilai total index prestasi
    ip = 0
    # melakukan validasi jumlah mata kuliah yang dimasukkan
    if jmatkul < 1 or jmatkul > 8:
        print("Jumlah Mata Kuliah antara 1 sampai 8")
    else:
        #melakukan perulangan kedua ketika kondisi index lebih kecil dari jumlah matkul
        while i < jmatkul:
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
            total = total+sks   
            #melakukan penjumlahan bobot nilai untuk setiap mata kuliah dari masing-masing kuis, tugas, uts, dan uas        
            nilai = 0.15*kuis+0.15*tugas1+0.20*tugas2+0.25*uts+0.25*uas
            #untuk mencari nilai sesuai dengan variabel
            if 85 <= nilai <= 100:
                grade = "A"
                #index prestasi
                index = float(4.0)
            elif 70 <= nilai < 85:
                grade = "B"
                index = float(3.0)
            elif 55 <= nilai < 70:
                grade = "C"
                index = float(2.0)
            elif 40 <= nilai < 55:
                grade = "D"
                index = float(1.0)
            elif nilai < 40:
                grade = "E"
                index = float(0)
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
print("Total SKS :", total)
#Mencetak nilai Index Prestasi dibagi total sks
print("Index prestasi :", ip/total)
