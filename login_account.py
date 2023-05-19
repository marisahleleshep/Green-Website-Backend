class Signup:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
    def create_account(self):
        # code to create a new user account using self.email, self.username, and self.password
        print(f"Account with email '{self.email}', username '{self.username}', and password '{self.password}' has been created.")
signup = Signup('chep@gmail.com', 'mercy', '454532')
signup.create_account()
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
