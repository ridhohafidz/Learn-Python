# Bagian ini adalah unit test.
# Unit test digunakan untuk melakukan pengujian
# otomatis terhadap program yang dibangun.
# Jangan lakukan perubahan apapun pada bagian ini.
# Unit test ini akan digunakan oleh dosen/asisten
# sebagai acuan dalam mengoreksi 
# hasil pekerjaan mahasiswa.
# Jika ingin mencoba menjalankan unit test ini,
# tekan Ctrl+Shift+S untuk membuka terminal shell
# di bagian kanan bawah layar.
# Ketik perintah pytest, lalu enter.
# Jika masih ada AssertionError, berarti fungsi yang
# dibuat belum benar.
# Jika tidak ada AssertionError dan hasil pengujian
# menunjukkan 100% sukses, berarti fungsi sudah benar.


import main

def test_sort_desc_1():
  assert main.sort_desc([3, 6, 2, 7, 1]) == [7, 6, 3, 2, 1]

def test_sort_desc_2():
  assert main.sort_desc([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]

def test_sort_desc_3():
  assert main.sort_desc([5]) == [5]

def test_sort_desc_4():
  assert main.sort_desc([]) == []

def test_sort_desc_5():
  assert main.sort_desc([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1]

def test_sort_desc_6():
  assert main.sort_desc([9, 6, 3, 1]) == [9, 6, 3, 1]
