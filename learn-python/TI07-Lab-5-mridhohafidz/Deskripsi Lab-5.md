# Deskripsi Lab-5
Pada Lab-5, kalian diminta untuk membuat fungsi-fungsi berikut. Kode fungsi tersebut dapat dituliskan dalam file main.py di tempat yang sudah disediakan.
**Untuk setiap fungsi yang dibangun, berikan penjelasan mengenai alur jalannya fungsi. Tulis penjelasan tersebut dalam bentuk komentar pada fungsi.**


## Soal 1. Fungsi cetak_nama()
Buatlah fungsi `cetak_nama()` yang menerima sebuah parameter string `nama` dan mencetak `nama` berulang kali mulai dari satu karakter pertama hingga semua karakter `nama` terlihat. Di akhir, cetak `nama` ditambah karakter `'!'`.
Sebagai contoh, pemanggilan `cetak_nama('Nurul')` akan mencetak `N`, `Nu`, `Nur`, `Nuru`, `Nurul`, dan `Nurul!`.


Fungsi `cetak_nama()` dapat dipanggil tanpa parameter.
Dalam kasus ini, parameter `nama` akan memiliki nilai default berupa string kosong.
Jika `nama` merupakan string kosong, maka cetak pesan `'Tidak ada nama yang dicetak'`.


Fungsi `cetak_nama()` dapat diadopsi dari program yang dibangun di Lab-4.


### Contoh 1.1
Contoh pemanggilan dan luaran fungsi:
```sh
>>> cetak_nama('Fikri')
F
Fi
Fik
Fikr
Fikri
Fikri!
```


### Contoh 1.2
Contoh pemanggilan dan luaran fungsi:
```sh
>>> cetak_nama()
Tidak ada nama yang dicetak
```


## Soal 2. Fungsi hitung_kesamaan()
Buatlah fungsi `hitung_kesamaan()` yang menerima dua parameter string `kata1` dan `kata2` dan mengembalikan banyaknya karakter pada `kata1` dan `kata2` yang posisi dan nilainya sama.
Jika tidak ada karakter yang posisi dan nilainya sama di antara `kata1` dan `kata2`, maka fungsi akan mengembalikan `0`.


### Contoh 2.1
Contoh pemanggilan dan luaran fungsi:
```sh
>>> hitung_kesamaan('python', 'path')
3
```
Penjelasan contoh 2.1:
String `'python'` dan `'path'` memiliki kesamaan posisi dan nilai karakter di indeks `0`, `2`, dan `3`.
Dengan demikian, fungsi `hitung_kesamaan()` akan mengembalikan `3`.


### Contoh 2.2
Contoh pemanggilan dan luaran fungsi:
```sh
>>> hitung_kesamaan('python', 'cacaca')
0
```
Penjelasan contoh 2.2:
String `'python'` dan `'cacaca'` tidak memiliki kesamaan posisi dan nilai karakter di indeks manapun, sehingga fungsi `hitung_kesamaan()` akan mengembalikan `0`.


## Soal 3. Fungsi hitung()
Buatlah fungsi `hitung()` yang menerima tiga parameter yaitu bilangan `bil1`, bilangan `bil2`, dan string `operator`.
Fungsi `hitung()` akan mengembalikan hasil operasi antara `bil1` dan `bil2`.
Parameter `operator` berisi operator yang digunakan untuk mengoperasikan `bil1` dan `bil2`.
Operator bisa berupa `'+'`, `'-'`, atau `'*'`.
- Jika operator bernilai `'+'`, maka fungsi akan mengembalikan `bil1 + bil2`
- Jika operator bernilai `'-'`, maka fungsi akan mengembalikan `bil1 - bil2`
- Jika operator bernilai `'*'`, maka fungsi akan mengembalikan `bil1 * bil2`


Fungsi `hitung()` dapat dipanggil tanpa parameter `operator`.
Dalam kasus ini, parameter `operator` memiliki nilai default `'+'`.


### Contoh 3.1
Contoh pemanggilan dan luaran fungsi:
```sh
>>> hitung(12, 8, '-')
4
```
Penjelasan contoh 3.1:
Karena `operator` bernilai `'-'`, maka fungsi mengembalikan `12 - 8 = 4`.


### Contoh 3.2
Contoh pemanggilan dan luaran fungsi:
```sh
>>> hitung(12, 8)
20
```
Penjelasan contoh 3.2:
Karena pemanggilan fungsi `hitung()` tidak menyertakan parameter `operator`, maka secara default `operator` bernilai `'+'`, sehingga fungsi mengembalikan `12 + 8 = 20`.
