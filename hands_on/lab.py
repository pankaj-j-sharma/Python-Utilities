class MyLab:
    def __init__(self, name):
        self.__name = name
        self._protected = name


mylab = MyLab('new hands on')
print(dir(mylab))
print(mylab._protected)
print(mylab.__init__('new'))
