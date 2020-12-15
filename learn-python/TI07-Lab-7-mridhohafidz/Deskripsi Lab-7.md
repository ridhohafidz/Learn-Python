# Deskripsi Lab-7
Pada Lab-7, kalian diminta untuk membuat fungsi-fungsi yang dideskripsikan pada soal-soal di bawah. Kode fungsi tersebut dapat dituliskan dalam file main.py di tempat yang sudah disediakan.
Terdapat dua soal yang wajib dikerjakan (Soal 1 dan Soal 2) dan satu soal bonus (Soal 3) yang tidak wajib dikerjakan.
**Untuk setiap fungsi yang dibangun, berikan penjelasan mengenai alur jalannya fungsi. Tulis penjelasan tersebut dalam bentuk komentar pada fungsi.**


## Soal 1. Fungsi convert_list()
Buatlah fungsi `convert_list()` yang menerima parameter `multilist` yang berupa list dua-dimensi (list yang berisi list) dan mengembalikan list baru yang merupakan hasil perubahan `multilist` menjadi list satu dimensi.


### Contoh 1.1
Contoh pemanggilan dan luaran fungsi:
```sh
>>> convert_list([[1,2],[3,4],[5,6]])
[1,2,3,4,5,6]
```

Penjelasan Contoh 1.1:
Parameter pemanggilan fungsi tersebut adalah sebuah list yang berisi list sebagai berikut:
```
[[1,2],
 [3,4],
 [5,6]]
```
Setiap elemen dalam list dua-dimensi tersebut digabungkan dalam list satu-dimensi `[1,2,3,4,5,6]`.


### Contoh 1.2
Contoh pemanggilan dan luaran fungsi:
```sh
>>> convert_list([[1,2,3], ['apel', 'jeruk']])
[1,2,3,'apel','jeruk']
```

Penjelasan Contoh 1.2:
Parameter pemanggilan fungsi tersebut adalah sebuah list yang berisi list sebagai berikut:
```
[[1,2,3],
 ['apel','jeruk']]
```
Setiap elemen dalam list dua-dimensi tersebut digabungkan dalam list satu-dimensi `[1,2,3,'apel','jeruk']`.


## Soal 2. Fungsi get_nilai()
Diberikan file `nilai1.txt` dan `nilai2.txt` yang berisi daftar nama mahasiswa dan nilai UTS mahasiswa tersebut.
Isi file `nilai1.txt` dan `nilai2.txt` terlampir pada daftar file. Jangan mengubah isi file-file tersebut.


Buatlah fungsi `get_nilai()` yang menerima dua buah parameter, yaitu string `filename` dan string `nama`, dan mengembalikan hasil pembulatan nilai UTS mahasiswa dengan nama tersebut berdasarkan data pada file yang namanya sesuai parameter `filename`.
Parameter `nama` harus dapat diabaikan case-nya.
Artinya, 'Joni', 'joni', dan 'JONI' dianggap sebagai nama yang sama.
Jika `nama` tidak ditemukan dalam file `filename`, fungsi akan mengembalikan `None`.


### Contoh 2.1
Contoh pemanggilan dan luaran fungsi:
```sh
>>> get_nilai('nilai1.txt', 'joni')
76
```

Penjelasan contoh 2.1:
Dalam file `nilai1.txt`, terdapat data `Joni` dengan nilai `75.50`. Hasil pembulatan 75.50 adalah 76, sehingga fungsi akan mengembalikan 76.


### Contoh 2.2
Contoh pemanggilan dan luaran fungsi:
```sh
>>> get_nilai('nilai2.txt', 'joni')
None
```

Penjelasan contoh 2.2:
Dalam file `nilai2.txt`, tidak ada data mahasiswa atas nama Joni, sehingga fungsi akan mengembalikan `None`.


## [BONUS] Soal 3. Fungsi nilai_max()
Buatlah fungsi `nilai_max()` yang menerima parameter string `filename` dan mengembalikan pasangan nama dan nilai yang merupakan nilai paling tinggi di antara data pada file tersebut.
Catatan: nilai dikembalikan dalam tipe float (bukan string)


### Contoh 3.1
Contoh pemanggilan dan luaran fungsi:
```sh
>>> nilai_max('nilai1.txt')
('Zack', 88.05)
```

Penjelasan contoh 3.1:
Pada file `nilai1.txt`, data dengan nilai tertinggi adalah data Zack, yaitu dengan nilai 88.05. Oleh karena itu, fungsi mengembalikan ('Zack', 88.05).


### Contoh 3.2
Contoh pemanggilan dan luaran fungsi:
```sh
>>> nilai_max('nilai2.txt')
('Arya', 90.00)
```

Penjelasan contoh 3.2:
Pada file `nilai2.txt`, data dengan nilai tertinggi adalah data Arya, yaitu dengan nilai 90.00. Oleh karena itu, fungsi mengembalikan ('Arya', 90.00).
