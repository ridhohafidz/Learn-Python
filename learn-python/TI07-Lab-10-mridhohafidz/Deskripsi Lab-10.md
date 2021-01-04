# Deskripsi Lab-10
Pada Lab-10, kalian diberikan sebuah implementasi struktur data Linked List. Linked List tersebut menyimpan data berupa sekumpulan bilangan bulat. Kalian diminta untuk mengimplementasikan dua fungsi berikut pada struktur data Linked List tersebut.
**Berikan penjelasan mengenai alur jalannya fungsi. Tulis penjelasan tersebut dalam bentuk komentar pada fungsi.**


## Soal 1. Fungsi sum_odd()
Buatlah fungsi `sum_odd()` yang mengembalikan hasil penjumlahan semua elemen linked list yang merupakan bilangan ganjil. Jika tidak ada bilangan ganjil di dalam linked list tersebut atau linked list tersebut kosong, maka fungsi akan mengembalikan 0.


## Soal 2. Fungsi get_max()
Buatlah fungsi `get_max()` yang mengembalikan bilangan terbesar yang ada di dalam linked list. Jika linked list kosong, maka fungsi akan mengembalikan `None`.


## Contoh 1
Linked list `list1` berisi bilangan 1, 2, 3, 4, 5.
Contoh pemanggilan dan luaran fungsi:
```sh
>>> list1.sum_odd()
9
>>> list1.get_max()
5
```

### Penjelasan Contoh 1
Pada `list1`, terdapat bilangan ganjil 1, 3, dan 5.
Penjumlahan bilangan tersebut adalah 9, sehingga fungsi `sum_odd()` akan mengembalikan 9.
Pada `list1`, bilangan paling besar adalah 5, sehingga fungsi `get_max()` akan mengembalikan 5.


## Contoh 2
Linked list `list2` merupakan list kosong.
Contoh pemanggilan dan luaran fungsi:
```sh
>>> list2.sum_odd()
0
>>> list2.get_max()
None
```

### Penjelasan Contoh 2
Pada `list2`, tidak ada bilangan ganjil, sehingga fungsi `sum_odd()` akan mengembalikan 0.
Linked list `list2` tidak memiliki elemen dengan nilai terbesar, sehingga fungsi `get_max()` akan mengembalikan `None`.