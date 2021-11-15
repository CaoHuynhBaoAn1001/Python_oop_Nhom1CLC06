class Vehicle:
   def __init__(self,name,people,kilomet):
        self.__name = name
        self.people = people
        self.kilomet = kilomet
   def doXang(self):
        if(self.kilomet >= 100):
            print("Phai di do xang")
        else:
            print("Khong can di do xang")
   def printInfo(self):
        print("Ten cua xe la :",self.__name)
        print("So nguoi co the cho duoc la:",self.people)
        print("So kilomet co the di duoc la:",self.kilomet)
class Car(Vehicle):
   def XuPhat(self):
        if(self.people > 4):
            print("Xe bi pham loi")
        else:
            print("Xe khong loi")
   def __init__(self, name, people, kilomet,type):
        super().__init__(name, people, kilomet)
        self.Type = type
   def printInfo(self):
        super().printInfo()
        print("Kieu xe di chuyen la:",self.Type)     
   pass
class Commerce:
   def __init__(self,money,thue):
      self.money = money
      self.thue = thue
   def BaoHanh(self):
      print("Xe can phai bao hanh hang thang")
   def printInfo(self):
      print("Gia tri chiec xe la:",self.money)
      print("Tien thue de nhap xe ve la:",self.thue)
      pass
class Bike(Vehicle,Commerce):
   def __init__(self, name, people, kilomet):
       super().__init__(name, people, kilomet)  
   pass  
Car = Car("O to",5,65,"Thuong mai")
bike = Bike("Xe dap",2,50)
Car.printInfo()
Car.XuPhat()
bike.printInfo()
bike.BaoHanh()