"""
    method vs @classmethod vs @statcmethod
    method - self, método de instácia
    @classmethod - cls, método de classe
    @statcmethod - método estático ((X)self, (X)cls)
"""
class Connection:
    def __init__(self, host='localhost') -> None:
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('LOG:', msg)


# c1 = Connection()
c1 = Connection.create_with_auth("Bruno", '123')
# c1.set_user('Bruno')
# c1.set_password('123')
print(Connection.log('Essa mensagem de log'))
print(c1.user)
print(c1.password)
