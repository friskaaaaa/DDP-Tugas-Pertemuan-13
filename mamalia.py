from animal import animal

class mamalia(animal):
    def __init__(self, name, makanan, habitat, berkembang_biak, ukuran_tubuh, jenis_kulit, bernapas):
        super().__init__(name, makanan, habitat, berkembang_biak)
        self.jenis_kulit = jenis_kulit
        self.ukuran_tubuh = ukuran_tubuh
        self.bernapas = bernapas

    def info_mamalia(self):
        super().info_animal(),
        print("Jenis Kulit \t\t\t :", self.jenis_kulit,
              "\nUkuran Tubuh \t\t\t :", self.ukuran_tubuh,
              "\nBernapas dengan \t\t :", self.bernapas)

gajah = mamalia("Gajah", "Tumbuh-tumbuhan", "Darat", "Melahirkan", "Sangat Besar", "Sedikit Berbulu", "Paru-Paru")
gajah.info_mamalia()
print("================================================================")
kucing = mamalia("Kucing", "Ikan", "Darat", "Melahirkan", "Kecil", "Berbulu", "Paru-Paru")
kucing.info_mamalia()
print("================================================================")
lumba_lumba = mamalia("Lumba-Lumba", "Ikan", "Air", "Melahirkan", "Besar", "Tidak Berbulu", "Paru-Paru")
lumba_lumba.info_mamalia()