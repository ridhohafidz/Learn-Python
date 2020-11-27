#Mendefiniskan nama fungsi sebagai fungsi
def fungsi(a): 
  #kata kunci yaitu nf
  has_nf = "nf"  
  #jika parameter a diakhiri dengan kata .nf, maka balikan nilai False. Fungsi lower agar menyetarakan huruf menjadi kecil agar mudah dideteksi
  if a.lower().endswith("."+has_nf):  #fungsi endswith untuk memeriksa kondisi akhiran pada nilai
    return False
  #jika kata nf tidak diawali dengan titik maka balikan nilai True.  
  elif a.lower().endswith(has_nf): 
    return True
  #Jika kondisi diatas tidak lolos, balikan nilai False  
  else:
    return False

#panggil dan cetak fungsi dengan parameter "lalalaNF" akan balikan nilai True
print(fungsi("lalalNF"))
#panggil dan cetak fungsi dengan parameter "abc.nfxy" akan balikan nilai False
print(fungsi("abc.nfxy"))
#panggil dan cetak fungsi dengan parameter "lalal.nfNF" akan balikan nilai True
print(fungsi("lalal.nfNf")) 