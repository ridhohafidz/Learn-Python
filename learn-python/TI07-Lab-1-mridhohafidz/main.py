# SOAL 1 - Menghitung rata-rata
# Tuliskan program untuk Soal 1 di bawah ini
print("=====================================================")
print("Menghitung rata-rata (average)")
print("=====================================================")
angka1=int(input("Masukan Bilangan Pertama:"))
angka2=int(input("Masukan Bilangan Kedua:"))
angka3=int(input("Masukan Bilangan Ketiga:"))

hasil=int(angka1 + angka2 + angka3)/3
print("Rata-Rata dari", angka1, ",", angka2, ",", "dan", angka3, "hasilnya : ", hasil)

print("=====================================================")

# SOAL 2 - Menulis kelipatan bilangan
# Tuliskan program untuk Soal 2 di bawah ini
x = int(input("Masukan Bilangan Bulat : "))
z = x
while (x < 30 ):
  print(x, end="---")
  x += z 