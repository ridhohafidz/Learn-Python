def hurufvokal( a='BNDG CKP' , b='AIUEOaiueo'): #parameter 1 parameter 2 dibuat menjadi variabel a dan b 
    total = 0 # untuk menampung nilai jika parameter pertama memiliki huruf vokal 
    teks1=len(a) #menghitung panjang string variabel a
    teks2=len(b) #menghitung panjang string variabel b
    
    for i in range(0, teks1): #banyaknya perulangan tergantung dari panjangnya parameter pertama 
        for j in range(0, teks2): #banyaknya perulangan tergantung dari panjangnya parameter kedua
            if a[i]  == b[j] : #jika parameter pertama sama dengan parameter kedua maka tambahkan value dari variabel total
                total += 1 #mengubah value sebelumnya
            else :
                pass #lewati jika kondisi false
    return total #mengembalikan nilai total 
print(hurufvokal()) #mencetak dan memanggil function hurufvokal