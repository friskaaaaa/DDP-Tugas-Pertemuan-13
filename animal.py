#Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

class animal:
    def __init__(self, name, makanan, habitat, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.habitat = habitat
        self.berkembang_biak = berkembang_biak

    def info_animal(self):
        print("Nama Hewan \t\t\t :", self.name,
               "\nMakanan \t\t\t :", self.makanan,
               "\nHabitat \t\t\t :", self.habitat,
               "\nBerkembang_Biak \t\t :", self.berkembang_biak)

#buat minimal 3 class child (Amphibi,  Mamalia, Carnivora, dll) setiap class child itu memiliki 2 properti dan method  
#buat 3 objek dari masing masing class child.

