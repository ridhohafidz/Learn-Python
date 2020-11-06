# Deskripsi Lab-3
Pada Lab-3, kalian diminta untuk menuliskan program yang dapat menangani permasalahan-permasalahan berikut. Manfaatkan materi kuliah yang sudah dipelajari dari awal.
Program dapat dituliskan dalam file main.py yang sudah tersedia.
**Untuk setiap program yang ditulis, berikan penjelasan mengenai alur jalannya program. Tulis penjelasan tersebut dalam bentuk komentar pada program.**


## Soal 1. Gunting-Batu-Kertas
Buatlah program yang menyimulasikan permainan Gunting-Batu-Kertas dengan langkah penyelesaian sebagai berikut:
- Program meminta pemain pertama untuk memasukkan pilihannya (gunting, batu, atau kertas)
- Program meminta pemain kedua untuk memasukkan pilihannya (gunting, batu, atau kertas)
- Tentukan pemenang permainan tersebut berdasarkan pilihan setiap pemain. Dalam permainan Gunting-Batu-Kertas, Gunting mengalahkan Kertas, Kertas mengalahkan Batu, dan Batu mengalahkan Gunting. Jika pilihan kedua pemain sama, maka hasil akhirnya adalah seri.

### Contoh 1.1
Contoh masukan 1.1:
```sh
Masukkan pilihan Player-1: gunting
Masukkan pilihan Player-2: kertas
```

Contoh luaran 1.1:
```sh
Player-1 menang.
```

Penjelasan contoh 1.1:
Karena Player-1 memilih gunting dan Player-2 memilih kertas, maka Player-1 menang karena gunting mengalahkan kertas.


### Contoh 1.2
Contoh masukan 1.2:
```sh
Masukkan pilihan Player-1: batu
Masukkan pilihan Player-2: kertas
```

Contoh luaran 1.2:
```sh
Player-2 menang.
```

Penjelasan contoh 1.2:
Karena Player-1 memilih batu dan Player-2 memilih kertas, maka Player-2 menang karena kertas mengalahkan batu.


### Contoh 1.3
Contoh masukan 1.3:
```sh
Masukkan pilihan Player-1: kertas
Masukkan pilihan Player-2: kertas
```

Contoh luaran 1.3:
```sh
Pertandingan seri.
```

Penjelasan contoh 1.3:
Karena Player-1 dan Player-2 sama-sama memilih kertas, maka pertandingan seri.



## Soal 2. Toko Buku Bekas
Sebuah toko buku bekas menjual buku-buku bekas dengan harga seragam. Harga yang dikenakan terhadap buku tergantung pada jumlah buku yang dibeli.
Ketentuan harga buku:
- Jika seseorang membeli kurang dari 10 buku, maka harga yang dikenakan adalah Rp20.000,-/buku.
- Jika seseorang membeli 11-25 buku, maka harga yang dikenakan adalah Rp18.000,-/buku.
- Jika seseorang membeli 26-50 buku, maka harga yang dikenakan adalah Rp15.000,-/buku.
- Jika seseorang membeli lebih dari 50 buku, maka harga yang dikenakan adalah Rp10.000,-/buku.

Buatlah program yang menerima banyaknya buku yang akan dibeli dan mengembalikan total harga yang harus dibayar. Jika masukan pengguna berupa bilangan negatif, maka tampilkan pesan kesalahan.


### Contoh 2.1
Contoh masukan 2.1:
```sh
Masukkan banyaknya buku yang akan dibeli: 15
```

Contoh luaran 2.1:
```sh
Harga yang harus dibayar = 270000 rupiah
```

Penjelasan contoh 2.1:
Karena pelanggan akan membeli 15 buku, maka pelanggan dikenakan harga Rp18.000,-/buku. Dengan demikian, total harga yang harus dibayar adalah 15 x 18000 = 270000.


### Contoh 2.2
Contoh masukan 2.2:
```sh
Masukkan banyaknya buku yang akan dibeli: 100
```

Contoh luaran 2.2:
```sh
Harga yang harus dibayar = 1000000 rupiah
```

Penjelasan contoh 2.2:
Karena pelanggan akan membeli 100 buku, maka pelanggan dikenakan harga Rp10.000,-/buku. Dengan demikian, total harga yang harus dibayar adalah 100 x 10000 = 1000000.



## Soal 3. Mencetak persegi
Buatlah program yang meminta masukan bilangan bulat dan mencetak bentuk persegi berdasarkan masukan pengguna tersebut.
Persegi dicetak menggunakan karakter '#' untuk baris ganjil (baris pertama, ketiga, kelima, dst.) dan menggunakan karakter '$' untuk baris genap (baris kedua, keempat, keenam, dst.).


### Contoh 3.1
Contoh masukan 3.1:
```sh
Masukkan sebuah bilangan bulat: 5
```

Contoh luaran 3.1:
```sh
# # # # # 
$ $ $ $ $ 
# # # # # 
$ $ $ $ $ 
# # # # # 
```

Penjelasan Contoh 3.1:
Karena pengguna memasukkan bilangan 5, maka program mencetak 5 baris, di mana setiap baris ganjil berisi 5 buah karakter '#' yang dipisahkan spasi dan setiap baris genap berisi 5 buah karakter '$' yang dipisahkan spasi.


### Contoh 3.2
Contoh masukan 3.2:
```sh
Masukkan sebuah bilangan bulat: 4
```

Contoh luaran 3.2:
```sh
# # # # 
$ $ $ $ 
# # # # 
$ $ $ $ 
```

Penjelasan Contoh 3.2:
Karena pengguna memasukkan bilangan 4, maka program mencetak 4 baris, di mana setiap baris ganjil berisi 4 buah karakter '#' yang dipisahkan spasi dan setiap baris genap berisi 4 buah karakter '$' yang dipisahkan spasi.
