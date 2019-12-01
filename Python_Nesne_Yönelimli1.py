class Araba():
    def __init__(self):
        self.__Marka = ""
        self.__Hacim = 0
        self.__Model = 0
    #           Kapsülleme
    # Set Fonksiyonları
    
    def setMarka(self,marka):
        self.__Marka = marka
    def setMHacim(self,hacim):
        self.__Hacim = hacim
    def setModel(self,model):
        self.__Model = model

    # Get Fonksiyonları
    
    def getMarka(self):
        return self.__Marka 
    def getHacim(self):
        return self.__Hacim
    def getModel(self):
        return self.__Model

    def AracBilgileriGoster(self):
        print("""
                Arac Marka:        {}
                Arac Motor Hacim : {}
                Arac Model:        {}  
              """.format(self.getMarka(),self.getHacim(),self.getModel()))
    
    

if __name__ == "__main__":
    yeni = Araba()
    eski = Araba()
    eski.AracBilgileriGoster()
    yeni.setMarka("Audi")
    yeni.setModel("A8L")
    yeni.setMHacim(3.5)
    yeni.AracBilgileriGoster()
