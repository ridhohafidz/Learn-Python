# Deskripsi Lab-6
Pada Lab-6, kalian diminta untuk membuat fungsi-fungsi yang dideskripsikan pada soal-soal di bawah. Kode fungsi tersebut dapat dituliskan dalam file main.py di tempat yang sudah disediakan.
Terdapat dua soal yang wajib dikerjakan (Soal 1 dan Soal 2) dan satu soal bonus (Soal 3) yang tidak wajib dikerjakan.
**Untuk setiap fungsi yang dibangun, berikan penjelasan mengenai alur jalannya fungsi. Tulis penjelasan tersebut dalam bentuk komentar pada fungsi.**


## Soal 1. Fungsi jumlah_batas()
Buatlah fungsi `jumlah_batas()` yang menerima dua buah parameter, yaitu list bilangan `nums` dan bilangan `batas`. Fungsi mengembalikan hasil penjumlahan semua bilangan pada list `nums` yang nilainya lebih dari `batas`.


### Contoh 1.1
Contoh pemanggilan dan luaran fungsi:
```sh
>>> jumlah_batas([1,2,3,4,5,6], 2)
18
```

Penjelasan Contoh 1.1:
Dalam list `[1,2,3,4,5,6]`, bilangan yang lebih dari `2` adalah 3, 4, 5, dan 6. Hasil penjumlahan 3, 4, 5, dan 6 adalah 18, sehingga fungsi akan mengembalikan 18.


### Contoh 1.2
Contoh pemanggilan dan luaran fungsi:
```sh
>>> jumlah_batas([10,2,23,41,15,6], 200)
0
```

Penjelasan Contoh 1.2:
Dalam list `[10,2,23,41,15,6]`, tidak ada bilangan yang lebih dari `200`, sehingga fungsi akan mengembalikan 0.


## Soal 2. Fungsi list_nonvokal()
Buatlah fungsi `list_nonvokal()` yang menerima sebuah parameter string `s` dan mengembalikan sebuah list yang berisi daftar karakter string `s` yang bukan merupakan huruf vokal (a, i, u, e, o, A, I, U, E, O).


### Contoh 2.1
Contoh pemanggilan dan luaran fungsi:
```sh
>>> list_nonvokal('python')
['p', 'y', 't', 'h', 'n']
```

Penjelasan contoh 2.1:
Dalam string `'python'`, karakter yang bukan huruf vokal adalah p, y, t, h, dan n, sehingga fungsi akan mengembalikan list yang berisi karakter-karakter tersebut.


### Contoh 2.2
Contoh pemanggilan dan luaran fungsi:
```sh
>>> list_nonvokal('uiuiuiuiui')
[]
```

Penjelasan contoh 2.2:
Dalam string `'uiuiuiuiui'`, semua karakter merupakan huruf vokal, sehingga fungsi akan mengembalikan list kosong.


### Contoh 2.3
Contoh pemanggilan dan luaran fungsi:
```sh
>>> list_nonvokal('I LOVE YOU')
[' ', 'L', 'V', ' ', 'Y']
```

Penjelasan contoh 2.3:
Dalam string `'I LOVE YOU'`, karakter yang bukan huruf vokal adalah sebagai berikut:
- Karakter spasi antara I dan L
- L
- V
- Karakter spasi antara E dan Y
- Y


Dengan demikian, fungsi akan mengembalikan list yang berisi karakter-karakter tersebut.


## [BONUS] Soal 3. Fungsi list_modify()
Buatlah fungsi `list_modify()` yang menerima empat parameter sebagai berikut:
- `alist`, data bertipe list yang akan dimodifikasi
- `command`, perintah yang ingin dikenakan terhadap `alist`, dapat bernilai: `'add'` atau `'remove'`
- `position`, posisi pada `alist` yang akan dikenai operasi modifikasi, dapat bernilai: `'start'`, `'end'`
- `value`, nilai baru yang akan ditambahkan ke dalam `alist`


Perintah (_command_) `add` digunakan untuk menambahkan elemen baru ke dalam `alist`. Parameter `value` berisi nilai yang akan ditambahkan ke dalam `alist`. Posisi (_position_) `start` mengindikasikan bahwa `value` akan ditambahkan sebagai elemen pertama `alist`, sedangkan posisi `end` mengindikasikan bahwa `value` akan ditambahkan sebagai elemen terakhir `alist`.

Perintah (_command_) `remove` digunakan untuk menghapus elemen pada `alist`. Perintah `remove` tidak memerlukan parameter `value`, sehingga parameter `value` dapat diberi nilai default `None`. Posisi (_position_) `start` mengindikasikan bahwa penghapusan dilakukan terhadap elemen pertama `alist`, sedangkan posisi `end` mengindikasikan bahwa penghapusan dilakukan terhadap elemen terakhir `alist`.


Di akhir, fungsi akan mengembalikan `alist` yang telah dimodifikasi.


### Contoh 3.1
Contoh pemanggilan dan luaran fungsi:
```sh
>>> list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek')
['bebek', 'ayam', 'ikan', 'kucing']
```
Penjelasan contoh 3.1:
Karena `command` bernilai `'add'` dan `position` bernilai `'start'`, maka elemen baru akan ditambahkan sebagai elemen pertama `alist`. Elemen yang akan ditambahkan bernilai `'bebek'`. Dengan demikian, isi list yang sudah dimodifikasi adalah `['bebek', 'ayam', 'ikan', 'kucing']`.


### Contoh 3.2
Contoh pemanggilan dan luaran fungsi:
```sh
>>> list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek')
['ayam', 'ikan', 'kucing', 'bebek']
```
Penjelasan contoh 3.2:
Karena `command` bernilai `'add'` dan `position` bernilai `'end'`, maka elemen baru akan ditambahkan sebagai elemen terakhir `alist`. Elemen yang akan ditambahkan bernilai `'bebek'`. Dengan demikian, isi list yang sudah dimodifikasi adalah `['ayam', 'ikan', 'kucing', 'bebek']`.


### Contoh 3.3
Contoh pemanggilan dan luaran fungsi:
```sh
>>> list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start')
['ikan', 'kucing']
```
Penjelasan contoh 3.3:
Karena `command` bernilai `'remove'` dan `position` bernilai `'start'`, maka elemen pertama pada `alist` akan dihapus. Dengan demikian, isi list yang sudah dimodifikasi adalah `['ikan', 'kucing']`.


### Contoh 3.4
Contoh pemanggilan dan luaran fungsi:
```sh
>>> list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end')
['ayam', 'ikan']
```
Penjelasan contoh 3.4:
Karena `command` bernilai `'remove'` dan `position` bernilai `'end'`, maka elemen terakhir pada `alist` akan dihapus. Dengan demikian, isi list yang sudah dimodifikasi adalah `['ayam', 'ikan']`.
