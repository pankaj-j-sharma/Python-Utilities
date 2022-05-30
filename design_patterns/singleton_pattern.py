from abc import ABCMeta, abstractclassmethod


class IDBConnector(metaclass=ABCMeta):

    @abstractclassmethod
    def get_connection():
        ''''implement the get connection in the child class'''


class OracleDbConnector(IDBConnector):

    __connection = None

    @staticmethod
    def get_connection():
        if not OracleDbConnector.__connection:
            data = OracleDbConnector.__get_required_inputs()
            return OracleDbConnector(*data)
        else:
            return OracleDbConnector.__connection

    @staticmethod
    def __get_required_inputs():
        hostname = input("Please enter your db hostname\n")
        sid = input("Please enter your db sid\n")
        port = input("Please enter your db port\n")
        username = input("Please enter your db username\n")
        password = input("Please enter your db password\n")

        return [username, password, hostname, sid, port]

    def __init__(self, username, password, hostname, sid, port=1521):
        if OracleDbConnector.__connection != None:
            self = OracleDbConnector.__connection
            print('Already connected to Oracle DB')
        else:
            self.username = username
            self.password = password
            self.hostname = hostname
            self.portnumber = port
            self.sid = sid
            OracleDbConnector.__connection = self
            print('successsfully connected to database')


if __name__ == '__main__':
    dbcon = OracleDbConnector.get_connection()
