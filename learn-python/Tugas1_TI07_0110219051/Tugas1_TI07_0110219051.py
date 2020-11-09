#Nama   : Muhammad Ridho Hafidz
#NIM    : 0110219051
#Kelas  : TI 07 - Weekend

print("Fitur Input Nilai Mahasiswa")
nim = input("Masukan NIM: ")
while True:
    jmatkul = int(input("Berapa Jumlah Mata Kuliah yang diambil ? "))
    print("\n")
    i = 0
    total = 0
    ipk = 0
    if jmatkul < 1 or jmatkul > 8:
        print("Jumlah Mata Kuliah antara 1 sampai 8")
    else:
        while i < jmatkul:
            i = i+1
            print("Nilai Mata Kuliah", i)
            matkul = input("Nama Mata Kuliah: ")
            sks = int(input("Beban SKS mata kuliah: "))
            kuis = eval(input("Nilai Kuis: "))
            tugas1 = eval(input("Nilai Tugas 1: "))
            tugas2 = eval(input("Nilai Tugas 2: "))
            uts = eval(input("Nilai UTS: "))
            uas = eval(input("Nilai UAS: "))
            nilai = 0.15*kuis+0.15*tugas1+0.20*tugas2+0.25*uts+0.25*uas
            total = total+sks
            if 85 <= nilai <= 100:
                grade = "A"
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
            print("Nilai untuk mata kuliah", matkul,":", nilai, "( grade", grade, ")")
            ipk = ipk+(sks*index)
            print("\n")
        break

print("Rangkuman")
print("NIM :", nim)
print("Total SKS :", total)
print("Index prestasi :", ipk/total)
