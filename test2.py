class animal:
    stt = 1 #Class attribute
    def __init__(self,CanNang : float,ChieuCao : float,DoAn : str) :
        self.CanNang = CanNang
        self.ChieuCao = ChieuCao      
        self.DoAn = DoAn  
    def printInfo(self): 
        print("Can nang cua con vat la :",self.CanNang)
        print("Chieu cao cua con vat la :",self.ChieuCao)
        print("Do an cua con vat la :",self.DoAn) 
    pass
    

Cat = animal(2.3,3.4,"Ca")
Cat.printInfo()








