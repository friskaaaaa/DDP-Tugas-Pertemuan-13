from animal import animal

class carnivora(animal):
    def __init__(self, name, makanan, habitat, berkembang_biak, memangsa, racun, kecepatan):
        super().__init__(name, makanan, habitat, berkembang_biak)
        self.memangsa = memangsa
        self.racun = racun
        self.kecepatan = kecepatan

    def info_carnivora(self):
        super().info_animal(),
        print("Memangsa dengan \t\t :", self.memangsa,
              "\nMemiliki Racun/tidak \t\t :", self.racun,
              "\nKecepatan \t\t\t :", self.kecepatan)
        
harimau = carnivora("Harimau", "Daging", "Hutan", "Melahirkan", "Taring dan Cakar", "Tidak Memiliki Racun", "49-65 Km/Jam")
harimau.info_carnivora()
print("================================================================")
cheetah = carnivora("Cheetah", "Daging", "Hutan", "Melahirkan", "Menjatuhkan, mencekik, dan menggigit leher mangsanya", "Tidak Memiliki Racun", "80-130 Km/Jam")
cheetah.info_carnivora()
print("================================================================")
ular = carnivora("Ular", "Daging", "Hutan", "Bertelur dan Melahirkan", "Menelan", "Memiliki Racun", "29 Km/Jam")
ular.info_carnivora()