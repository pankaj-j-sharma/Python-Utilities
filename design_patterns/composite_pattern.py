from abc import ABCMeta, abstractmethod, abstractstaticmethod


class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        '''Interface method to be implemented'''

    @abstractstaticmethod
    def print_department():
        '''Interface method to be implemented'''


class AccountingDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting Department employees : {self.employees}")


class HRDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"HR Department employees : {self.employees}")


class DevelopmentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development Department employees : {self.employees}")


class ParentDepartment(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print(f"Parent Department base employees : {self.base_employees}")
        print(f"Parent Department employees : {self.employees}")


if __name__ == '__main__':
    accounts = AccountingDepartment(120)
    hrs = HRDepartment(15)
    developers = DevelopmentDepartment(350)

    parent = ParentDepartment(3)
    parent.add(accounts)
    parent.add(hrs)
    parent.add(developers)

    parent.print_department()
