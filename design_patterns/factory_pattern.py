from abc import ABCMeta, abstractmethod, abstractstaticmethod

''''
Factory Method is a Creational Design Pattern that allows an interface or a class 
to create an object, but let subclasses decide which class or object to instantiate.
We can easily add the new types of products without disturbing the existing client code.
Generally, tight coupling is being avoided between the products and the creator classes
'''


class ICarSupplier(metaclass=ABCMeta):

    @abstractmethod
    def get_car_model(self):
        '''Interface method'''


class HondaCar(ICarSupplier):
    def __init__(self):
        super().__init__()
        self.name = 'Honda Car'

    def get_car_model(self):
        return self.name


class SuzukiCar(ICarSupplier):
    def __init__(self):
        super().__init__()
        self.name = 'Suzuki Car'

    def get_car_model(self):
        return self.name


class TataCar(ICarSupplier):
    def __init__(self):
        super().__init__()
        self.name = 'Tata Car'

    def get_car_model(self):
        return self.name


class TestCar(ICarSupplier):
    def __init__(self):
        super().__init__()
        self.name = 'Demo Car'

    def get_car_model(self):
        return self.name


'''Factory class that instantiates the child classes'''


class CarFactory:

    @staticmethod
    def get_car_instance(type):
        if type == 'honda':
            return HondaCar()
        elif type == 'tata':
            return TataCar()
        elif type == 'suzuki':
            return SuzukiCar()
        else:
            return TestCar()


if __name__ == '__main__':
    choice = str(
        input("Select the type of car\nHonda\nTata\nSuzuki\n\n")).lower()
    car = CarFactory.get_car_instance(choice)
    print(car.get_car_model())
