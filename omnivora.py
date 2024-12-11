from animal import animal

class omnivora(animal):
    def __init__(self, name, makanan, habitat, berkembang_biak, struktur_gigi, memangsa, jenis_kulit):
        super().__init__(name, makanan, habitat, berkembang_biak)
        self.struktur_gigi = struktur_gigi
        self.memangsa = memangsa
        self.jenis_kulit = jenis_kulit

    def info_omnivora(self):
        super().info_animal(),
        print("Struktur Gigi \t\t\t :", self.struktur_gigi,
              "\nMemangsa Menggunakan \t\t :", self.memangsa,
              "\nJenis Kulit \t\t\t :", self.jenis_kulit)
        
ayam = omnivora("Ayam", "Serangga,Biji-bijian, dan Bekatul", "Hutan, Kebun, dan Pekarangan Rumah", "Bertelur", "Tidak Memiliki Gigi", "Paruh", "Berbulu")
ayam.info_omnivora()
print("================================================================")
tupai = omnivora("Tupai", "Buah-buahan, Biji-bijian, Serangga, dan Sayuran", "Hutan", "Melahirkan", "4 Gigi seri, 4 Gigi geraham depan, 12 gigi geraham", "Gigi seri untuk mengunyah makanan", "Berbulu")
tupai.info_omnivora()
print("================================================================")
tikus = omnivora("Tikus", "Biji-bijian, Buah, Benih, dan Serangga", "Sawah, Atap, Gorong-gorong, dan Rumpun tanaman", "Melahirkan", "2 Gigi seri atas, 2 Gigi seri bawah, 8 Gigi rahang atas, 8 Gigi rahang bawah", "Gigi serinya", "Sedikit Berbulu")
tikus.info_omnivora()