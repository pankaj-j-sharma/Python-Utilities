class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

    def print_relation(self):
        print('Grandfather : ', self.grandfathername)


class Father(Grandfather):
    def __init__(self, fathername='Pa', grandfathername='Grandpa'):
        self.fathername = fathername
        super().__init__(grandfathername)

    def print_relation(self):
        print('Father : ', self.fathername)


class Mother:
    def __init__(self, mothername='Mom'):
        self.mothername = mothername

    def print_relation(self):
        print('Mother : ', self.mothername)


class School:
    def __init__(self, schoolname='Litle Angels'):
        self.schoolname = schoolname

    def print_relation(self):
        print('School : ', self.schoolname)


class FirstChild(Father, Mother, School):
    def __init__(self, firstchildname='', fathername='Pa', grandfathername='Grandpa', mothername='Mom', schoolname='Litle Angels'):

        Father.__init__(self, fathername=fathername,
                        grandfathername=grandfathername)
        Mother.__init__(self, mothername=mothername)
        School.__init__(self, schoolname=schoolname)
        self.firstchildname = firstchildname
        self.print_relation()

    def print_relation(self):
        Grandfather.print_relation(self)
        Father.print_relation(self)
        Mother.print_relation(self)
        School.print_relation(self)
        print('Name : ', self.firstchildname)


class SecondChild(Father, Mother):
    def __init__(self, secondchildname, fathername='Pa', grandfathername='Grandpa', mothername='Mom'):
        Father.__init__(self, fathername=fathername,
                        grandfathername=grandfathername)
        Mother.__init__(self, mothername=mothername)
        self.secondchildname = secondchildname
        self.print_relation()

    def print_relation(self):
        print('Name : ', self.secondchildname)


if __name__ == '__main__':
    child = FirstChild('Arun', 'Rajesh', 'Anand', 'Priya', 'R.A.U.B.S')
