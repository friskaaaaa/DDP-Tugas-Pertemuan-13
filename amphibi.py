from animal import animal

class amphibi(animal):
    def __init__(self, name, makanan, habitat, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, habitat, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self):
        super().info_animal(),
        print("Jenis Air \t\t\t :", self.jenis_air,
              "\nBernapas dengan \t\t :", self.bernapas)
        
amphibi = amphibi("Katak", "Serangga", "Dua alam", "Bertelur", "Air tawar", "Kulit dan Paru-paru")
amphibi.info_amphibi()