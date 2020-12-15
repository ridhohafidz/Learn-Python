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

def test_convert_list_1():
  assert main.convert_list([[9, 9, 9]]) == [9,9,9]

def test_convert_list_2():
  assert main.convert_list([[9, 9, 9], ['a', 'b'], [1, 2, 'x', 'y']]) == [9,9,9,'a','b',1,2,'x','y']

def test_convert_list_3():
  assert main.convert_list([[1,2,3],[9, 9, 9]]) == [1,2,3,9,9,9]

def test_get_nilai_1():
  assert main.get_nilai('nilai1.txt','PUTRA') == 58

def test_get_nilai_2():
  assert main.get_nilai('nilai2.txt','PUTRA') == 59

def test_get_nilai_3():
  assert main.get_nilai('nilai1.txt','agus') == None

def test_get_nilai_4():
  assert main.get_nilai('nilai2.txt','Lina') == None
