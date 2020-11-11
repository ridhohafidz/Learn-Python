def cetak_nama(nama=''):
  # Tulis kode fungsi cetak_nama di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  # jika parameter cetak_nama kosong, maka cetak print dibawah ini
  if not(nama):
    print("Tidak ada nama yang dicetak")
  # jika parameter tersebut ada, maka jalankan fungsi seperti dibawah ini
  else:
    #disini menambahkan value dari parameter yaitu dengan menambahkan tanda seru(!)
    x = nama+"!"
    #fungsi len menghitung panjang string
    y = len(x)
    #iteraton (start looping dari 0)
    z = 0
    #perulangan dimulai
    while z < y:
      #variabel z akan ditambah nilainya 1
      z += 1
      #mencetak hasil dengan string slicing
      print(x[0:z])

def hitung_kesamaan(kata1, kata2):
  # Tulis kode fungsi hitung_kesamaan di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  #ini percabangan untuk mencari mana teks yang lebih kecil, akan melakukan perulangan sesuai dengan dari kata yang terkecil. jika variabel kata2 tidak lebih kecil dari panjang kata1, maka masuk ke else
  if len(kata2) < len(kata1):
    #itteraton (start looping dari 0)
    c = 0 
    #untuk menampung nilai awal
    total = 0
    #perulangan disesuaikan panjang dari variabel kata2
    while c < len(kata2):
      #jika isi kata2 sesuai dengan isi dari kata1, maka jalankan statement true
      if kata2[1] == kata1[c]:
        #jika benar, ubah variabel total jadi +1
        total += 1
      #jika tidak lewatin   
      else:
        pass
      #tiap perulangan variabel i akan bertambah 1
      c += 1
      #mengembalikan nilai akhir ke function test()
    return total
  else:
    #itteraton (start looping dari 0)
    c = 0 
    #untuk menampung nilai awal
    total = 0
    #perulangan disesuaikan panjang dari variabel kata1
    while c < len(kata1):
      #jika isi kata1 sesuai dengan isi dari kata2, maka jalankan statement true
      if kata1[c] == kata2[c]:
        #jika benar, ubah variabel total jadi +1
        total += 1
      #jika tidak lewatin
      else: 
        pass
      #tiap perulangan variabel c akan bertambah 
      c += 1
    #mengembalikan nilai akhir ke function test()  
    return total 

def hitung(bil1, bil2, operator='+'):
  # Tulis kode fungsi hitung() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  #Jika operator bernilai '+', maka fungsi akan mengembalikan bil1 + bil2
  if operator =="+":
    count = bil1 + bil2
    return  count
  #Jika operator bernilai '-', maka fungsi akan mengembalikan bil1 - bil2  
  elif operator == "-":
    count = bil1 - bil2
    return count
  #Jika operator bernilai '*', maka fungsi akan mengembalikan bil1 * bil2
  elif operator == "*":
    count = bil1 * bil2 
    return count 


# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya
# (untuk fungsi hitung_kesamaan() dan fungsi hitung()).
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  print("Hasil cetak_nama('Mawar'):")
  cetak_nama("Mawar")
  print()
  print("Hasil cetak_nama(''):")
  cetak_nama("")
  print()
  r = hitung_kesamaan('python', 'path')
  print(f"hitung_kesamaan('python', 'path') = {r} \t(solusi: 3)")
  r = hitung_kesamaan('masak', 'cuci')
  print(f"hitung_kesamaan('masak', 'cuci') = {r} \t(solusi: 0)")
  r = hitung_kesamaan('python', '')
  print(f"hitung_kesamaan('python', '') = {r} \t\t(solusi: 0)")
  print()
  r = hitung(4, 8)
  print(f'hitung(4, 8) = {r} \t\t(solusi: 12)')
  r = hitung(4, 8, '-')
  print(f"hitung(4, 8, '-') = {r} \t(solusi: -4)")
  r = hitung(4, 8, '*')
  print(f"hitung(4, 8, '*') = {r} \t(solusi: 32)")

if __name__ == '__main__':
  test()