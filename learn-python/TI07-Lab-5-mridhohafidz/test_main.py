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
# Disclaimer: Unit test ini hanya menguji
# fungsi hitung_kesamaan() dan fungsi hitung()

import main

def test_hitung_kesamaan_normal1():
  assert main.hitung_kesamaan('masak', 'masuk') == 4

def test_hitung_kesamaan_normal2():
  assert main.hitung_kesamaan('masak', 'makanan') == 3

def test_hitung_kesamaan_normal3():
  assert main.hitung_kesamaan('masak', 'masak') == 5

def test_hitung_kesamaan_empty1():
  assert main.hitung_kesamaan('', 'masuk') == 0

def test_hitung_kesamaan_empty2():
  assert main.hitung_kesamaan('masak', '') == 0

def test_hitung_kesamaan_nomatches():
  assert main.hitung_kesamaan('payung', 'belalang') == 0

def test_hitung_tambah():
  assert main.hitung(5, 9, '+') == 14

def test_hitung_kurang():
  assert main.hitung(5, 9, '-') == -4

def test_hitung_kali():
  assert main.hitung(5, 9, '*') == 45

def test_hitung_optoperator():
  assert main.hitung(5, 9) == 14
