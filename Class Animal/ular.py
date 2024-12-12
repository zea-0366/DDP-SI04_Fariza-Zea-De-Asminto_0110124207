from Animals import *

class ular(animal):
   def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, jenis_ular):
    super().__init__(nama, makanan, hidup, berkembang_biak)
    self.warna = warna_ular
    self.jenis = jenis_ular
    
   def cetak_ular(self):
     super().cetak()
     print(f"hewan ini berwarna {self.warna} dan termasuk hewan {self.jenis}")
     
print("-------Cetak Ular-------")
Cobra = ular("Ular Cobra", "tikus", "darat", "bertelur", "hitam","berbisa" )
Cobra.cetak_ular()

# objek kedua
Python = ular("Ular Python", "tikus" , "darat" , "bertelur", "coklat", "tidak berbisa")
Python.cetak_ular()