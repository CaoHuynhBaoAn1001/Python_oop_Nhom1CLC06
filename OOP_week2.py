class ConNguoi:
    def __init__(self):
        self.__ChieuCao = "1.7"
        self.CanNang = "50" + "kg"
    pass
class Hocsinh(ConNguoi):
    def __init__(self):
        ConNguoi.__init__(self)
        print("Chieu cao cua hoc sinh la ")
        print(self.__ChieuCao)
    pass
# Driver code
HocSinh1 = ConNguoi()
print(HocSinh1.CanNang)
HocSinh2= Hocsinh()



  
