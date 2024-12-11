from animal import animal

class herbivora(animal):
    def __init__(self, name, makanan, habitat, berkembang_biak, struktur_gigi, memangsa, jenis_kulit):
        super().__init__(name, makanan, habitat, berkembang_biak)
        self.struktur_gigi = struktur_gigi
        self.memangsa = memangsa
        self.jenis_kulit = jenis_kulit
    
    def info_herbivora(self):
        super().info_animal(),
        print("Struktur Gigi \t\t\t :", self.struktur_gigi,
              "\nMemangsa Menggunakan \t\t :", self.memangsa,
              "\nJenis Kulit \t\t\t :", self.jenis_kulit)
        
kelinci = herbivora("Kelinci", "Rumput, Jerami, Buah, dan Sayur", "Rumput dan Hutan", "Melahirkan", "6 Gigi seri, 12 Gigi pipi bawah, 10 Gigi pipi bawah", "Gigi seri untuk mengunyah makanan", "Berbulu")
kelinci.info_herbivora()
print("================================================================")
kambing = herbivora("Kambing", "Rumput", "Hutan dan di pelihara di peternakan", "Melahirkan", "4 pasang gigi seri, 3 gigi premolar, 3 gigi molar", "Gigi depan untuk mengunyah rumput", "sedikit berbulu")
kambing.info_herbivora()
print("================================================================")
jerapah = herbivora("Jerapah", "Daun, Ranting, dan Buah", "Hutan", "Melahirkan", "32 Gigi geraham", "Gigi geraham untuk mengunyah makanan", "Sedikit berbulu")
jerapah.info_herbivora()