# DDP LAB-3

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini
print("--------------------------------------------------------------")
print("SOAL 1 - Gunting-Batu-Kertas")
print("--------------------------------------------------------------")
x = input("Masukan pilihan Player-1 : ")  #buat player1
y = input("Masukan pilihan Player-2 : ")  #buat player2
arr = ['gunting', 'batu', 'kertas']       #array buat validasi input

if x and y in arr:
  if  x == arr[0] and y == arr[1]:
    print("Player 2 menang")
  elif x == arr[1] and y == arr[2]:
    print("Player 2 menang")
  elif x == arr[2] and y == arr[0]:
    print("Player 2 menang")
  elif x == y in arr:
    print("Pertandingan seri")
  else:
    print("Player 1 menang")
else:
  print("Hanya boleh masukan gunting batu kertas")


# SOAL 2 - Toko Buku Bekas
# Tuliskan program untuk Soal 2 di bawah ini
print("--------------------------------------------------------------")
print("SOAL 2 - Toko Buku Bekas")
print("--------------------------------------------------------------")
x = int(input("Masukkan banyaknya buku yang akan dibeli : "))
if x > 1:
  if x <= 10:
    print("Harga yang harus dibayar =", x*20000, "Rupiah")
  elif x <= 25:
    print("Harga yang harus dibayar =", x*18000, "Rupiah")
  elif x <= 50:
    print("Harga yang harus dibayar =", x*15000, "Rupiah")
  elif x > 50:
    print("Harga yang harus dibayar =", x*10000, "Rupiah")
else:
  print("Tidak boleh dibawah dari 1")




# SOAL 3 - Mencetak Persegi
# Tuliskan program untuk Soal 3 di bawah ini
print("--------------------------------------------------------------")
print("SOAL 3 - Mencetak Persegi")
print("--------------------------------------------------------------")
x = int(input("Masukkan sebuah bilangan bulat : "))
for i in range(1, x+1):
  if(i%2==0):
    print("$ "*x)
  else:
    print("# "*x)


