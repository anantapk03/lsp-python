from abc import ABC , abstractmethod 

class HitungBangunDatar(ABC) :
    def __init__(self, sisi:float) :
        self.__sisi = sisi 
    
    def get_sisi (self) -> float :
        return self.__sisi 
    
    @abstractmethod
    def hitung_keliling (self) :
        pass
    
    @abstractmethod
    def hitung_luas (self) :
        pass
    
    