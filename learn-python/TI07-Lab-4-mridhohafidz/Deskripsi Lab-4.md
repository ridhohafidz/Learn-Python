# Deskripsi Lab-4
Pada Lab-4, kalian diminta untuk menuliskan program yang dapat menangani permasalahan-permasalahan berikut. Program dapat dituliskan dalam file main.py yang sudah tersedia.
**Untuk setiap program yang ditulis, berikan penjelasan mengenai alur jalannya program. Tulis penjelasan tersebut dalam bentuk komentar pada program.**


## Soal 1. Mencetak nama
Buatlah program yang menerima sebuah nama dan mencetak nama tersebut berulang kali mulai dari satu karakter pertama hingga semua karakter nama terlihat.
Sebagai contoh, hasil cetak nama Nurul adalah N, Nu, Nur, Nuru, dan Nurul.
Program yang dibuat diharapkan hanya mengandung perulangan while dan string slicing.

### Contoh 1.1
Contoh masukan 1.1:
```sh
Masukkan nama: Fikri
```

Contoh luaran 1.1:
```sh
F
Fi
Fik
Fikr
Fikri
```

### Contoh 1.2
Contoh masukan 1.2:
```sh
Masukkan nama: SEMANGKA
```

Contoh luaran 1.2:
```sh
S
SE
SEM
SEMA
SEMAN
SEMANG
SEMANGK
SEMANGKA
```

## Soal 2. Validasi teks
Buatlah sebuah program yang menerima sebuah teks dan melakukan validasi terhadap teks tersebut.
Jika teks belum valid, maka program akan terus meminta pengguna memasukkan teks. Program berhenti saat teks valid dimasukkan.


Kriteria sebuah teks valid adalah sebagai berikut:
- Panjang teks minimal 8
- Teks mengandung minimal sebuah frase 'NF' (tidak harus kapital semua)
- Teks diakhiri dengan 'YYY' atau 'yyy' (kapital semua atau huruf kecil semua)
- Teks mengandung minimal sebuah angka (0-9)

### Contoh 2.1
Contoh masukan dan luaran 2.1:
```sh
Masukkan sebuah teks: 123lalalyyy
Teks tidak valid.
Masukkan sebuah teks: NF00yyy
Teks tidak valid.
Masukkan sebuah teks: nF1nNFnlyYy
Teks tidak valid.
Masukkan sebuah teks: NFpppppppyyy
Teks tidak valid.
Masukkan sebuah teks: nF1nNfnlyYYY
Teks valid. Program berhenti.
```

Penjelasan contoh 2.1:
- Teks 123lalalyyy tidak valid karena tidak mengandung frase NF
- Teks NF00yyy tidak valid karena panjang teks kurang dari 8
- Teks nF1nNFnlyYy tidak valid karena tidak diakhiri dengan 'YYY' atau 'yyy'
- Teks NFpppppppyyy tidak valid karena tidak mengandung angka
