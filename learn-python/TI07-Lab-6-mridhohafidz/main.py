# Nama: Muhammad Ridho Hafidz
# NIM: 0110219051
# Kelas: TI 07

def jumlah_batas(nums, batas):
    # itteration (start looping dari 0)
    i = 0
    total = 0
    # perulangan while
    while i < len(nums):
        # jika variabel nums lebih besar batas
        if nums[i] > batas:
            total += nums[i]
        else:
            pass
        i += 1
    # jika selesai perulangan akan mengembalikan nilai variabel total
    return total


def list_nonvokal(s):
    huruf_vocal = ['a', 'i', 'u', 'e','o']
    penguraian = []
    #itteration (start looping)
    i = 0
    parameter1 = s
    while i <len(parameter1):
        if parameter1[i].lower() not in huruf_vocal:
            penguraian += parameter1[i]
        else:
            pass
        i += 1
    return penguraian


def list_modify(alist, command, position, value=None):
    # Tulis kode fungsi list_modify() di bawah ini
    # Hapus pass jika implementasi sudah dibuat
    if command == 'add':
        if position == 'start':
            alist.insert(0, value)
            return alist
        elif position == 'end':
            alist.append(value)
            return alist
        else:
            pass
    elif command == 'remove':
        if position == 'start':
            del(alist[0])
            return alist
        elif position == 'end':
            del(alist[-1])
            return alist
        else:
                pass
    else:
        pass


# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi
# yang seharusnya.
def test():
    r = jumlah_batas([8, 7, 6, 10, 1], 5)
    print(f"jumlah_batas([8, 7, 6, 10, 1], 5) = {r} \n(solusi: 31)")
    print()
    r = jumlah_batas([1, -7, -10, 1], -5)
    print(f"jumlah_batas([1, -7, -10, 1], -5) = {r} \n(solusi: 2)")
    print()
    r = list_nonvokal('Halo')
    print(f"list_nonvokal('Halo') = {r} \n(solusi: ['H', 'l'])")
    print()
    r = list_nonvokal('AAAAAooooo')
    print(f"list_nonvokal('AAAAAooooo') = {r} \n(solusi: [])")
    print()
    r = list_nonvokal('Saya cinta programming')
    print(
        f"list_nonvokal('Saya cinta programming') = {r} \n(solusi: ['S', 'y', ' ', 'c', 'n', 't', ' ', 'p', 'r', 'g', 'r', 'm', 'm', 'n', 'g'])")
    print()
    r = list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek')
    print(
        f"list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek') = {r} \n(solusi: ['bebek', 'ayam', 'ikan', 'kucing'])")
    print()
    r = list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek')
    print(
        f"list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek') = {r} \n(solusi: ['ayam', 'ikan', 'kucing', 'bebek'])")
    print()
    r = list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start')
    print(
        f"list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start') = {r} \n(solusi: ['ikan', 'kucing'])")
    print()
    r = list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end')
    print(
        f"list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end') = {r} \n(solusi: ['ayam', 'ikan'])")
    print()


if __name__ == '__main__':
    test()
