# Nama: 
# NIM: 
# Kelas: 

def convert_list(multilist):
  # inisialisasi untuk menampung data list saat perulangan selesai
  result = []
  # perulangan for a (multilist), untuk mengekstrak data yang ada di parameter (multilist)
  for a in multilist:
    # perulangan for b dalam data yang sudah diekstark yaitu variabel a, isi dari variabel a itu diekstrak lagi menjadi variabel b
    for b in a:
      # fungsi result dipanggil lalu dihubungkan dengan fungsi insert untuk memasukkan value variabel b sesuai dari nomor index
      result.append(b)
  # mengembalikan nilai variabel result
  return result

def get_nilai(filename, nama):
  # buat variabel baru dengan nama file dan value nya adalah sebuah kumpulan data teks mentah
  file = open(filename)
  # lalu variabel file itu dilakukan perulangan lalu disimpan sementara pada variabel data 
  for data in file:
    # variabel data lalu displit agar teks tersebut menjadi list lalu diindexing dengan urutan ke 0 dan ubah value yang sudah diindexing tersebut menggunakan lower agar menjadi lowercase.
    # jika proses atas sudah dilaksanakan maka masuk ke perkondisian, jika data nilainya sama dengan parameter nama yang sudah dimodifikasi dengan fungsi lower.
    if data.split()[0].lower() == nama.lower(): 
      # maka buat variabel result untuk menampung sejumlah data yang sudah dimodifikasi dengan fungsi split dan index ke 1
      result = float(data.split()[1])
      # maka variabel result itu ditimpa dengan value yang baru yaitu nilai result yang sudah dibulatkan dengan fungsi round
      result = round(result)
      # ketika sudah dibulatkan maka mengembalikan nilai result
      return result
    # jika tidak lewatkan saja agar program dapat fokus mencari nilai true  
    else:
      pass
  # untuk menutup jika pengolaan file sudah selesai pada python
  file.close()

def nilai_max(filename):
  # buat variabel baru dengan nama file dan value nya adalah sebuah kumpulan data teks mentah
  file = open(filename)
  # inisialisasi untuk menampung data list saat perulangan selesai
  result = []
  # lalu variabel file itu dilakukan perulangan untuk mengekstrak variabel data 
  for data in file:
    # value dari variabel data yang sudah displit dan sudah di indexing lalu disimpan dalam variabel nama dan nilai 
    nama, nilai = data.split()[0], data.split()[1]
    # maka variabel result ditambah nilainya menggunakan fungsi append dengan value dari variabel nilai dan nama 
    result.append([float(nilai), nama])
  # ketika perulangan selesai maka menutup pengolaan file pada python  
  file.close()
  # cari nilai maksimal dari variabel result lalu simpan kedalam variabel itu sendiri
  result = max(result)
  # jika nilai terbesar sudah didapat maka balikan urutan nilai dari variabel result menggunakan fungsi reverse
  result.reverse()
  # variabel result diindexing di posisi ke 0 dan 1 (sting nama, nilai) lalu simpan ke dalam variabel itu sendiri  
  result = result[0], result[1]
  # mengembalikan nilai result
  return(result)



# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = convert_list([[1,2], [3,4], [5,6]])
  print(f"convert_list([[1,2], [3,4], [5,6]]) = {r} \n(solusi: [1, 2, 3, 4, 5, 6])")
  print()
  r = get_nilai('nilai1.txt','joni')
  print(f"get_nilai('nilai1.txt','joni') = {r} \n(solusi: 76)")
  print()
  r = get_nilai('nilai2.txt','joni')
  print(f"get_nilai('nilai2.txt','joni') = {r} \n(solusi: None)")
  print()
  r = nilai_max('nilai1.txt')
  print(f"nilai_max('nilai1.txt') = {r} \n(solusi: ('Zack', 88.05)")
  print()
  r = nilai_max('nilai2.txt')
  print(f"nilai_max('nilai2.txt') = {r} \n(solusi: ('Arya', 90.00)")
  print()

if __name__ == '__main__':
  test()