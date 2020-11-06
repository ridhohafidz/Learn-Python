# DDP LAB-2

# SOAL 1 - Mencetak bilangan
# Tuliskan program untuk Soal 1 di bawah ini
print("=============================================")
print("Mencetak Bilangan")
print("=============================================")
# Perulangan menggunakan fungsi range()dengan 3 parameter yaitu (nilai_awal, nilai_akhir, selang).
for i in range(100,0,-2):
    print(i, end=",")
print("")  



# SOAL 2 - Menghitung rata-rata
# Tuliskan program untuk Soal 2 di bawah ini
# Pada program soal 2
print("=============================================")
print("Menghitung rata-rata")
# Variable untuk menginput banyaknya angka
num = eval(input("Masukkan banyaknya angka:"))
# Variable 
total = 0
# Perulangan untuk menginput banyaknya angka yang diinput sebelumnya 
for i in range (num):
# Variable untuk menginput angka
  angka= eval(input("Masukkan angka:"))
# Varible yang digunakan untuk mengitung secara keseluruhuan (total) angka yang di masukkan
  total += angka
# Mencetak hasil rata-rata
print("Rata-rata= ", total/num)



# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini
print("=============================================")
print("Mencetak Persegi")
# Variable untuk menginput sebuah bilangan bulat
bilangan = eval(input("Masukkan sebuah bilangan bulat : "))
# Perulangan untuk mencetak dengan sebuat karakter (#) dalam bentuk persegi yang dipisahkan oleh spasi
for i in range(bilangan):
  for j in range(bilangan):
      print("#", end=' ')
  print()
  