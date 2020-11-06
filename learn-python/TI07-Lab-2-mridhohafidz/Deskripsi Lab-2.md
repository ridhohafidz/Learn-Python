# Deskripsi Lab-2
Pada Lab-2, kalian diminta untuk menuliskan program yang dapat menangani permasalahan-permasalahan berikut.
Program dapat dituliskan dalam file main.py yang sudah tersedia.
**Untuk setiap program yang ditulis, berikan penjelasan mengenai alur jalannya program. Tulis penjelasan tersebut dalam bentuk komentar pada program.**


## Soal 1. Mencetak bilangan
Gunakan perulangan FOR untuk mencetak bilangan ```100, 98, 96, ..., 4, 2```.



## Soal 2. Menghitung rata-rata (_average_)
Buatlah program yang menghitung rata-rata dari sekumpulan angka dengan langkah penyelesaian sebagai berikut:
- Program meminta pengguna memasukkan jumlah bilangan yang akan dihitung rata-ratanya. Jumlah bilangan diasumsikan pasti bilangan bulat.
- Program secara berulang meminta pengguna untuk memasukkan angka yang akan disertakan dalam perhitungan rata-rata. Angka boleh berupa bilangan bulat maupun desimal.
- Program mencetak nilai rata-rata ke layar.

Rata-rata dari sekumpulan bilangan dihitung dengan rumus total_penjumlahan_bilangan / banyaknya_bilangan.


### Contoh 2.1
Contoh masukan 2.1:
```sh
Masukkan banyaknya angka: 5
Masukkan angka: 10
Masukkan angka: 12.5
Masukkan angka: -4.2
Masukkan angka: 123.9
Masukkan angka: -3
```

Contoh luaran 2.1:
```sh
Rata-rata = 27.840000000000003
```

Penjelasan contoh 2.1:
Karena pengguna memasukkan bilangan 5, maka program secara berulang sebanyak 5 kali meminta pengguna memasukkan angka.
Angka yang dimasukkan pengguna adalah ```10```, ```12.5```, ```-4.2```, ```123.9```, dan ```-3```.
Rata-rata dari bilangan tersebut adalah ```27.840000000000003```, didapat dari
```(10 + 12.5 + (-4.2) + 123.9 + (-3)) / 5```.

### Contoh 2.2
Contoh masukan 2.2:
```sh
Masukkan banyaknya angka: 7
Masukkan angka: 10
Masukkan angka: -12
Masukkan angka: 12.5
Masukkan angka: -4.2
Masukkan angka: 123.9
Masukkan angka: -3
Masukkan angka: 30
```

Contoh luaran 2.2:
```sh
Rata-rata = 22.45714285714286
```

Penjelasan contoh 2.2:
Karena pengguna memasukkan bilangan 7, maka program secara berulang sebanyak 7 kali meminta pengguna memasukkan angka.
Angka yang dimasukkan pengguna adalah ```10```, ```-12```, ```12.5```, ```-4.2```, ```123.9```, dan ```-3```, dan ```30```.
Rata-rata dari bilangan tersebut adalah ```22.45714285714286```, didapat dari
```(10 + (-12) + 12.5 + (-4.2) + 123.9 + (-3) + 30) / 7```.



## Soal 3. Mencetak persegi
Buatlah program yang meminta masukan bilangan bulat dan mencetak bentuk persegi berdasarkan masukan pengguna tersebut.
Gunakan '#' dipisahkan spasi sebagai karakter untuk membangun persegi.


### Contoh 3.1
Contoh masukan 3.1:
```sh
Masukkan sebuah bilangan bulat: 5
```

Contoh luaran 3.1:
```sh
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # 
```

Penjelasan Contoh 3.1:
Karena pengguna memasukkan bilangan 5, maka program mencetak 5 baris, di mana setiap baris berisi 5 buah karakter '#' yang dipisahkan spasi.


### Contoh 3.2
Contoh masukan 3.2:
```sh
Masukkan sebuah bilangan bulat: 3
```

Contoh luaran 3.2:
```sh
# # #
# # #
# # #
```

Penjelasan Contoh 3.2:
Karena pengguna memasukkan bilangan 3, maka program mencetak 3 baris, di mana setiap baris berisi 3 buah karakter '#' yang dipisahkan spasi.
