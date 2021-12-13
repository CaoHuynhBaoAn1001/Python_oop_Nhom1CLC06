class ConNguoi:
    def __init__(self):
        self.__ChieuCao = "1.7"
        self._DoTuoi=18
        self.CanNang = "50" + "kg"
    def printInfo(self):
        print("Chieu cao cua nguoi nay la {}".format(self.__ChieuCao))
        print("Can nang cua nguoi nay la {}".format(self.CanNang))
    def SetHeight(self,Height): #ham setter
        self.__ChieuCao=Height
    pass
class Hocsinh(ConNguoi):
    def __init__(self):
        ConNguoi.__init__(self)
        print("Chieu cao cua hoc sinh la ")
        print(self.__ChieuCao)
    pass
HocSinh1 = ConNguoi()
HocSinh1.printInfo()
HocSinh1.__ChieuCao="1.8"
HocSinh1.printInfo()
HocSinh1.SetHeight("1.8")
HocSinh1.printInfo()
HocSinh2= Hocsinh()



  
