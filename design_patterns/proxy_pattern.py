from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def get_person():
        '''interface method'''


class Person(IPerson):
    def get_person(self):
        print('I am a Person')


class ProxyPerson(IPerson):
    def __init__(self):
        super().__init__()
        self.person = Person()

    def get_person(self):
        print('I am a Person Proxy')
        self.person.get_person()


if __name__ == '__main__':
    proxy = ProxyPerson()
    proxy.get_person()
