class KimonuDetail:
    def __init__(self):
        print("D E T A I L   H A S I L   J U A L !!!")
        x = input("Penghasilan hari ini (180000) :")
        self.pemisah()
        self.modalUtama(x)
        self.pemisah()
        self.p20(x)
        self.pemisah()
        self.modalCadangan(x)
        self.pemisah()
        self.bagiHasil()

    def modalUtama(self, x):
        modal_utama = float(x) * 0.8
        print("M O D A L   U T A M A")
        print("==>>>")
        print("Modal Utama ( 80% Penghasilan ) = Penghasilan * 80%")
        print("Modal Utama ( 80% Penghasilan ) =", x, "* 80%")
        print("Modal Utama ( 80% Penghasilan ) ///=", int(modal_utama))

    def p20(self, x):
        self.duapuluh = float(x) * 0.2
        print("2 0 %   d a r i   P E N G H A S I L A N")
        print("==>>>")
        print("20% Penghasilan = Penghasilan * 20%")
        print("20% Penghasilan =", x, "* 20%")
        print("20% Penghasilan ////=", int(self.duapuluh))

    def modalCadangan(self, x):
        modal_cadangan = self.duapuluh * 0.1
        print("M O D A L   C A D A N G A N")
        print("==>>>")
        print("Modal Cadangan ( 10% dari (20% Penghasilan) ) = (20% Penghasilan) * 10%")
        print("Modal Cadangan ( 10% dari (20% Penghasilan) ) =", int(self.duapuluh), "* 10%")
        print("Modal Cadangan ( 10% dari (20% Penghasilan) ) ////=", int(modal_cadangan))
        
    def bagiHasil(self):
        bagi_hasil = self.duapuluh * 0.9
        hasil = bagi_hasil / 2
        print("B A G I   H A S I L")
        print("==>>>")
        print("Bagi penghasilan = (20% penghasilan) * 90%")
        print("Bagi penghasilan =", self.duapuluh, "* 90%")
        print("Bagi penghasilan ////=", int(bagi_hasil))
        print("==>>>")
        print("A B A H")
        print(int(hasil))
        print("==>>>")
        print("B A P A K")
        print(int(hasil))
        print("==>>>")
        input("\t\t\t\tE   X   I   T   !!!")

    def pemisah(self):
        print("---")
        input("enter")
        print("----->")

if __name__ == "__main__":
    KimonuDetail()