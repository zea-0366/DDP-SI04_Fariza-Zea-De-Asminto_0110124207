class animal:
  def __init__(self, nama, makanan, hidup, berkembang_biak):
    self.nama = nama
    self.makanan = makanan
    self.hidup = hidup
    self.berkembang_biak = berkembang_biak
    
  def cetak (self):
    print(f"Hewan ini bernama {self.nama}, dia memakan {self.makanan}, hewan ini juga hidup di {self.hidup} dan berkembang biak dengan cara {self.berkembang_biak}")
    
# C1 = animal("Burung Cendrawasih", "buah-buahan dan artropoda", "hutan tropis", "bertelur")
# C1.cetak()

# C2 = animal("Ikan Arwana", "jangkrik", "air", "bertelur")
# C2.cetak()