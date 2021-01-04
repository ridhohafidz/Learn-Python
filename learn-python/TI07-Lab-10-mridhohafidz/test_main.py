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

from main import LinkedList, Node

list1 = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
list2 = LinkedList(Node(5, Node(5, Node(5, Node(5)))))
list3 = LinkedList(Node(1, Node(51, Node(5, Node(7, Node(9, Node(3)))))))
list4 = LinkedList()
list5 = LinkedList(Node(13))
list6 = LinkedList(Node(200))

def test_sum_odd_1():
  assert list1.sum_odd() == 9

def test_sum_odd_2():
  assert list2.sum_odd() == 20

def test_sum_odd_3():
  assert list3.sum_odd() == 76

def test_sum_odd_4():
  assert list4.sum_odd() == 0

def test_sum_odd_5():
  assert list5.sum_odd() == 13

def test_sum_odd_6():
  assert list6.sum_odd() == 0

def test_get_max_1():
  assert list1.get_max() == 5

def test_get_max_2():
  assert list2.get_max() == 5

def test_get_max_3():
  assert list3.get_max() == 51

def test_get_max_4():
  assert list4.get_max() is None

def test_get_max_5():
  assert list5.get_max() == 13

def test_get_max_6():
  assert list6.get_max() == 200
