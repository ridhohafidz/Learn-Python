#Mendefiniskan nama fungsiku sebagai fungsi
def fungsiku(a):
  #Buat string a jadi lowercase  
  string = a.lower() 
  #Ini berfungsi untuk menampung index untuk huruf NF saat perulangan
  total = 0 
  #Ini berfungsi untuk menggabungkan value dari variabel string (temporary)
  container = ""  
  #Frase wajib NF
  keyword = "nf"  
  #Perulangan i  dengan range 0 sampai panjang variabel string
  for i in range(0, len(string)):
    #Pecahkan string sesuai index iteration lalu gabungkan kedalam variabel container 
    container += string[i]
    #Jika nantinya variabel container mengandung frasa NF, hentikan perulangan dengan break  
    if "nf" in container:
      #Untuk memberhentikan operasi   
      break
    #Jika tidak, lewatkan saja pakai pass 
    else: 
      pass
    #Selama perulangan berjalan, tambahkan 1 nilai (value) dari variabel total
    total += 1 
  #Jika string[index-2] (output = .) tidak sama dengan string "."  
  if string[total-2] != ".":
    #Mengembalikan nilai true    
    return True 
  #atau string[index+1:index+3] (output: nf) sama dengan keyword yang sudah ditentukan.  
  elif string[total+1:total+3] == keyword: 
    #Mengembalikan nilai true  
    return True
  #Jika tidak   
  else: 
    #Mengembalikan nilai false  
    return False  

#panggil dan cetak fungsi dengan parameter "Halo nNf xyz" akan bernilai True
print(fungsiku("Halo nNf xyz"))
#panggil dan cetak fungsi dengan parameter "abc.nfxy" akan bernilai false
print(fungsiku("abc.nfxy"))
#panggil dan cetak fungsi dengan parameter "abc.nfNf" akan balikan nilai True
print(fungsiku("abc.nfNf"))