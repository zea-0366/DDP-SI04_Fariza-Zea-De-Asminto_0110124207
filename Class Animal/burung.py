from Animals import *

class Burung(animal):
  def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
    super().__init__(nama, makanan, hidup, berkembang_biak)
    self.jenis_bulu = jenis_bulu
    self.bunyi = bunyi
    
  def cetak_burung(self):
    super().cetak()
    print(f"hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}")
    
print("-------Cetak Burung-------")
beo = Burung("Burung beo", "Biji-bijian", "udara", "bertelur" , "blue and orange", "Hai Kamu Cantik")
beo.cetak_burung()

# object kedua
merpati = Burung("Burung Merpati", "Biji-bijian", "udara", "bertelur" , "putih", "Berdekut")
merpati.cetak_burung()