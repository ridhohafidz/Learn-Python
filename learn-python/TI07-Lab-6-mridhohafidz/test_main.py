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

def test_jumlah_batas_1():
  assert main.jumlah_batas([9, 9, 9], 10) == 0

def test_jumlah_batas_2():
  assert main.jumlah_batas([9, 9, 9], 5) == 27

def test_jumlah_batas_3():
  assert main.jumlah_batas([0.5, 1.5, -3, -0.5], -1) == 1.5

def test_jumlah_batas_4():
  assert main.jumlah_batas([1, 1.5, 2, 2.5, 3, 3.5], 2.1) == 9.0

def test_list_nonvokal_1():
  assert main.list_nonvokal('jalan-jalan') == ['j', 'l', 'n', '-', 'j', 'l', 'n']

def test_list_nonvokal_2():
  assert main.list_nonvokal('au-au') == ['-']

def test_list_nonvokal_3():
  assert main.list_nonvokal('BY XXX') == ['B', 'Y', ' ', 'X', 'X', 'X']

def test_list_nonvokal_4():
  assert main.list_nonvokal('good bye!') == ['g', 'd', ' ', 'b', 'y', '!']

def test_list_modify_1():
  assert main.list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek') == ['bebek', 'ayam', 'ikan', 'kucing']

def test_list_modify_2():
  assert main.list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek') == ['ayam', 'ikan', 'kucing', 'bebek']

def test_list_modify_3():
  assert main.list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start') == ['ikan', 'kucing']

def test_list_modify_4():
  assert main.list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end') == ['ayam', 'ikan']

def test_list_modify_5():
  assert main.list_modify([10, 30, 50, 70, 90], 'add', 'start', 100) == [100, 10, 30, 50, 70, 90]

def test_list_modify_6():
  assert main.list_modify([10, 30, 50, 70, 90], 'add', 'end', 100) == [10, 30, 50, 70, 90, 100]

def test_list_modify_7():
  assert main.list_modify([10, 30, 50, 70, 90], 'remove', 'start') == [30, 50, 70, 90]

def test_list_modify_8():
  assert main.list_modify([10, 30, 50, 70, 90], 'remove', 'end') == [10, 30, 50, 70]
