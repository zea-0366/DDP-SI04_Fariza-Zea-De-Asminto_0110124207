import math

def v_balok(panjang,lebar,tinggi):
  volume =  panjang * lebar * tinggi
  print(f"Volume balok {panjang} * {lebar} * {tinggi} = {volume}")

def v_kubus(sisi):
  volume = sisi * sisi * sisi
  print(f"Volume Kubus {sisi} * {sisi} * {sisi} = {volume}")
  
def v_tabung(jari2,tinggi):
  volume = 3.14 * jari2 * jari2 * tinggi
  print(f"Volume Tabung {3.14} * {jari2} * {jari2} * {tinggi} = {volume}")
  
def v_prisma(luas_alas, tinggi):
  volume = luas_alas * tinggi
  print(f"Volume Prisma {luas_alas} * {tinggi} = {volume}")

def v_limassegitiga(luas_alas,tinggi):
  volume = 1/3 * luas_alas * tinggi
  print(f"Volume limassegitiga {1/3} * {luas_alas} * {tinggi} = volume")
  