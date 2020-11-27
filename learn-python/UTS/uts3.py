#Mendefiniskan nama fungsiku sebagai fungsi
def fungsiku(a):
  string = a.lower()
  total = 0
  container = ""
  keyword = "nf"
  for i in range(0, len(string)):
    container += string[i]
    if "nf" in container:
      break
    else:
      pass
    total += 1
  if string[total-2] != ".":
    return True
  elif string[total+1:total+3] == keyword:
    return True
  else:
    return False

#panggil dan cetak fungsi dengan parameter "Halo nNf xyz" akan bernilai True
print(fungsiku("Halo nNf xyz"))
#panggil dan cetak fungsi dengan parameter "abc.nfxy" akan bernilai false
print(fungsiku("abc.nfxy"))
#panggil dan cetak fungsi dengan parameter "abc.nfNf" akan balikan nilai True
print(fungsiku("abc.nfNf"))