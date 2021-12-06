class ConNguoi:
    def __init__(self,DoTuoi,ChieuCao:float,CanNang):
        self.__ChieuCao =ChieuCao + "m"
        self.CanNang =CanNang + "kg"
        self.DoTuoi=DoTuoi
    def printInfo(self):
        print("Nguoi nay cao {} ".format(self.__ChieuCao))
        print("Nguoi nay nang {} ".format(self.CanNang))
        print("Nguoi nay {} tuoi".format(self.DoTuoi))
    @staticmethod
    def CheckTuoi(DoTuoi):
        if(DoTuoi>"60"):
            print("Nguoi nay da gia")
        else:
            print("Nguoi nay con tre")
    pass
NguoiA=ConNguoi("61","1.78","60")
NguoiA.printInfo()
NguoiA.CheckTuoi(NguoiA.DoTuoi)