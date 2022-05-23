from penghitung_bangunruang import HitungBangunRuang

class Kubus(HitungBangunRuang):
    
    def __init__(self, rusuk):
        super().__init__(rusuk)
    
    
        
    def hitung_luas(self):
        print(6 * self.get_rusuk() * self.get_rusuk())
        
    def hitung_keliling(self):
        print(12 * self.get_rusuk())
        
    def hitung_volume(self):
        print(self.get_rusuk() * self.get_rusuk() * self.get_rusuk())