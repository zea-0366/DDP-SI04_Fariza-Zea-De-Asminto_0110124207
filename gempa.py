class Gempa:
  # Konstruksi Inisialisasi atribut
  def __init__(self,lokasi, skala):
    self.lokasi = lokasi
    self.skala = skala
    
  # Method penentu skala gempa
  def dampak(self):
    # logika/statement
    if self.skala < 2:
      print("Gempa tidak berasa")
    elif 2 <= self.skala <= 4:
      print("Gempa berdampak banguna retak-retak")
    elif 4 <= self.skala <= 6:
      print("Gempa Berdampak bangunan roboh")
    elif self.skala > 6:
      print("Gempa besar berpotensi tsunami")
      
    # Menampilkan lokasi dan skala gempa
    print(f"Lokasi Gempa: {self.lokasi}")
    print(f"Skala Gempa: {self.skala}")
  