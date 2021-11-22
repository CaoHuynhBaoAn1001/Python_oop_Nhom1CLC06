from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print("Running")
    pass
class programmer:
    def work(self,dom):
        print("Solving Bugs")
        dom.process()
#com = Computer()
com1 = Laptop()
#com1.process()
pg1 = programmer()
pg1.work(com1)