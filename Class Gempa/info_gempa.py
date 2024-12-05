from gempa import*

# Membuat objek Gempa dengan lokasi dan skala
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)


# Info gempa
print("## Gempa Bumi ##")
print()
gempa1.dampak() # memanggil method dampak()

print("## Gempa Bumi ##")
print()
gempa2.dampak()

print("## Gempa Bumi ##")
print()
gempa3.dampak()

print("## Gempa Bumi ##")
print()
gempa4.dampak()

print("## Gempa Bumi ##")
print()
gempa5.dampak()