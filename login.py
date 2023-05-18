class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def check_details(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False
login = Login('username', 'password')
valid = login.check_details('username', 'password')
if valid:
    print('Login successful')
else:
    print('Invalid username or password')
    