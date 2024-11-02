# Buat variabel list dengan value : [namaKendaraan, JenisKendaraan, ccKendaraan, warnaKendaraan,rodaKendaraan]
kendaraan = {"NamaKendaraan": "Toyota Camry", 
             "JenisKendaraan": "Sedan",
             "ccKendaraan": "2.494 cc" , 
             "WarnaKendaraan": "Hitam", 
             "RodaKendaraan": 4}
print(kendaraan)
print(kendaraan["NamaKendaraan"])
# menambahkan hargakendaraan
kendaraan["HargaKendaraan"] = "800.000.000"
kendaraan["TipeKendaraan"] = "Tipe G"
print(kendaraan)
print(kendaraan["NamaKendaraan"])
print(kendaraan["HargaKendaraan"])
print(kendaraan["TipeKendaraan"])
# menambahkan merk kendaraan
kendaraan["MerkKendaraan"] = "Toyota"
print(kendaraan["MerkKendaraan"])

# Buat program python dengan match case untuk menghitung luas bangun datar:
pilih = int(input("""Selamat datang diaplikasi menghitung
1. Untuk menghitung luas persegi
2. Untuk menghitung luas lingkaran
3. Untuk menghitung luas segitiga 
masukkan pilihan anda : """))

match pilih:
  case 1 :
    print("Kamu memilih 1 untuk menghitung luas persegi")
    sisi = int(input("masukkan sisi persegi: "))
    luaspsg = sisi*sisi
    print("luas persegi yang sisinya", sisi, "adalah", luaspsg)
  case 2 :
    print("Kamu memilih 1 untuk menghitung luas lingkaran")
    jari2 = int(input("masukkan jari-jari: "))
    luasLkr = 3.14*jari2*jari2
    print("luas lingkaran yang jari-jarinya", jari2, "adalah", luasLkr)
    
  case 3 :
    print("Kamu memilih 1 untuk menghitung luas segitiga")
    alas = int(input("masukkan alas: "))
    tinggi = int(input("masukkan tinggi: "))
    luasSegitiga = 0.5 * alas * tinggi 
    print("luas segitiga yang alas", alas, "dan tinggi", tinggi, "adalah", luasSegitiga)
  case _:
    print("Anda Salah Pilih")