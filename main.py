import math 

def l_persegi(sisi):
  luas = sisi*sisi
  keliling = sisi*sisi*sisi*sisi
  print(f"Luas Persegi {sisi} * {sisi} = {luas}")
  print(f"Keliling Persegi adalah {keliling}")

def l_segitiga(alas,tinggi):
 luas = 0.5 * alas * tinggi
 print(f"Luas Segitiga {0.5} * {alas} * {tinggi} = {luas}")

  
def l_lingkaran(jari2,luasLkr):
  luas = 3.14*jari2*jari2
  print(f"Luas Lingkaran {3.14} * {jari2} * {jari2} = {luas}")

def l_jajargenjang(alas,tinggi):
 luas = alas*tinggi
 print(f"Luas Jajargenjang {alas} * {tinggi} = {luas}")

def l_trapesium(tinggi, AB, CD) :
  luas = 0.5 * tinggi * AB * CD
  print(f"Luas Trapesium {0.5} * {tinggi} * {AB} * {CD} = {luas}")

  