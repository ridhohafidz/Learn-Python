# Nama: Muhammad Ridho Hafidz
# NIM: 0110219051
# Kelas: TI 07 - Weekend

def sort_desc(arr):
    # Melakukan perulangan range dimana panjang array dikurang 1
    for i in range(len(arr)-1):
        # Buat variabel max_idx digunakan untuk set elemen terbesar 
        max_idx = i
        # Melakukan perulangan dari array index ke 1 sampai panjang dari array tersebut
        for j in range (i+1, len(arr)):
            # Jika nilai array pada index ke (value dari variabel J) lebih besar dari array pada index ke (value dari max_idx)
            if arr[j] > arr[max_idx]:
                # Maka ubah value dari max_idx menjadi nilai dari variabel J
                max_idx = j
        # Swap variabel array ke (value dari variabel i) dan variabel array ke (value dari variabel max_idx)        
        arr[i], arr[max_idx] = arr[max_idx], arr[i]            
    # Fungsi sort_desc mengembalikan array yang terurut    
    return arr


# Algoritma yang digunakan ialah selection_sort 
# Modifikasi yang dilakukan yaitu mengubah variabel min_idx menjadi max_idx, lalu mengubah operator pada percabangan dengan kondisi menjadi lebih besar dari variabel array max_idx





# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = sort_desc([2, 3, 1, 0, 4])
  print(f"sort_desc([2, 3, 1, 0, 4]) = {r} \n(solusi: [4, 3, 2, 1, 0]")
  print()
  r = sort_desc([1, 2, 3])
  print(f"sort_desc([1, 2, 3]) = {r} \n(solusi: [3, 2, 1]")
  print()

if __name__ == '__main__':
  test()