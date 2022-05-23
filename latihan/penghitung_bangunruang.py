from abc import ABC , abstractmethod

class HitungBangunRuang(ABC):
    
    def __init__(self, rusuk):
        self.rusuk = rusuk
        
    def get_rusuk(self, rusuk):
        self.rusuk = rusuk
        
    @abstractmethod
    def hitung_keliling(self):
        pass
    
    @abstractmethod
    def hitung_luas(self):
        pass
    
    @abstractmethod
    def hitung_volume(self):
        pass